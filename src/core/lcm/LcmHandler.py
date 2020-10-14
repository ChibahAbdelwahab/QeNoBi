import os
import subprocess
import sys
from functools import partial
from multiprocessing import Pool

import pandas as pd

from src.settings.settings import NB_THREADS, TMP_FOLDER, LCM_EXECUTABLE, RESULTS_FOLDER


class LcmHandler:
    """ This Class gives an api to use LCM algorithm """

    def dataset_property_split(self, df, frequency, properties, min_support, groupby_property="customer_id",
                               itemset_property="item_id", ):
        """
        Split dataset according to the given properties
        :param df: Dataframe
        :param frequency: D,W,M
        :param properties: list of str
            Ex: ["sex","Age"]
        :param min_support: int
        :param groupby_property: str
        :param itemset_property: str
        :param temp_folder
        :param indexation_folder:
        :return: file names generator
        """
        for period, i in df.groupby(pd.Grouper(freq=frequency)):
            for values, ii in i.groupby(properties):
                if len(properties) > 1:
                    values = '_'.join(str(z) for z in values)

                split_name = f"{TMP_FOLDER}/splits/{period}_{values}#{min_support}"
                index_file_name = f"{TMP_FOLDER}/index/{period}_{values}#{min_support}"
                ii = ii.groupby(groupby_property)[itemset_property].apply(lambda x: " ".join(str(z) for z in x))

                ii.to_csv(split_name, index=None, header=False)
                pd.DataFrame(ii.index).to_csv(index_file_name, header=False, index=None)
                yield str(split_name)

    def reformat_output(self, raw_result, split_name):
        """
        Reformat default output of lcm  to a dataframe with structure : min_support,itemsets,users
        """
        output = pd.DataFrame([raw_result[0::2], raw_result[1::2]]).T
        output = pd.concat([output.drop(0, axis=1), output[0].str.split('\(([0-9]+)\)', expand=True).drop(0, axis=1)],
                           axis=1)
        split_name = split_name.split("/")[-1]  # remove temp folder from name
        output["period"] = split_name.split("_")[0]
        output["property_values"] = "_".join(split_name.split("_")[1:]).split("#")[0]
        output.columns = ["customer_id", "support", "itemset", "period", "property_values"]
        indexes = pd.read_csv(f'{TMP_FOLDER}/index/{split_name}', header=None)[0].to_dict()
        output["customer_id"] = output["customer_id"].fillna("").map(lambda x: [indexes[int(i)] for i in x.split()])
        return output

    def run_lcm(self, split_name, itemsets_size, support, output_file):
        """Runs LCM (Single Thread)  and return the  result formated with format_output

        Example for parameters : input_file='1999',support=6, itemsets_size=[5,100]
        Executed command :  $ ./lcm C_QI -l 5 -u 100 1999 6 -

        Preconfigured parameters:
         C: enumerate closed frequent itemsets
         M: enumerate maximal frequent itemsets
         Q: output the frequency on the head of each itemset found,
         I: output ID's of transactions including each itemset; ID of a transaction is given by the number of line in which the transaction is written. The ID starts from 0.
         _: no output to standard output (including messages w.r.t. input data)
         -l,-u [num]: enumerate itemsets with size at least/most [num]

        Output:
            Replace file having name input_file with the result : support,itemset,users
            if no itemset found the input_file is deleted and output is empty string ""
        """

        support = int(support)
        if None in itemsets_size:
            command = f"""./ {LCM_EXECUTABLE} C_QI - l {itemsets_size[0]} "{split_name}" {support} -"""
        else:
            command = f"""{LCM_EXECUTABLE} C_QI -l {itemsets_size[0]} -u {itemsets_size[1]} "{split_name}" {support} -"""
        try:
            result = subprocess.check_output(command, shell=True).decode(sys.stdout.encoding).split('\n')
        except subprocess.CalledProcessError:
            print("No itemset", split_name)
            return
            # os.remove(split_name)
        if "there is no frequent item" in str(result) or result == []:
            print("No itemset", split_name)
            return

        # TODO Optimize bottleneck
        with open(output_file, "a+") as file:
            self.reformat_output(result, split_name).to_csv(file, header=False, index=None, mode="a+")
        return split_name

    def multithread_lcm(self, df, frequency, support, itemsets_size, properties, output_file):
        f = partial(self.run_lcm, itemsets_size=itemsets_size, support=support, output_file=output_file)
        p = Pool(NB_THREADS)
        res = p.imap_unordered(f, self.dataset_property_split(df, frequency, properties, support))
        p.close()
        p.join()
        return res

    def linear_closed_itemset_miner(self, df, frequency, min_support, itemsets_size, properties):
        output_file = self.format_output_name(frequency, min_support, itemsets_size, properties)
        try:
            os.remove(output_file)  # In case already existing
            print(f"Removed old {output_file}")
        except:
            print(f"No old file to remove for {output_file} ")

        a = self.multithread_lcm(df, frequency, min_support, itemsets_size, properties, output_file)
        total = len(a._items)
        print(a, total)
        a = [i for i in a if i is not None]
        print(f"---| {output_file} Done")
        print(f'---| #split total: {total}')
        print(f'---| #split having groups: {len(a)}')
        print(f'---| Average: {len(a) / total}')
        print(" ")

    def format_output_name(self, frequency, min_support, itemsets_size, properties):
        return f'{RESULTS_FOLDER}/{frequency}-{min_support}-[{itemsets_size[0]}-{itemsets_size[1]}]-[{",".join(str(i) for i in properties)}]-lcm.out'


if __name__ == "__main__":
    a = LcmHandler()
    print("Hello")
