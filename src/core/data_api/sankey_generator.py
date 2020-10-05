import json
from itertools import groupby, product

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer

from core.data_api.dataset_handler import DatasetHandler
from settings.settings import STATS_FOLDER, LINKS_FOLDER, GROUPS_FOLDER, GROUPS_DEMOGRAPHICS
from tools.dataset_tools import get_items_descriptions
from tools.demographics import extract_demographics
from tools.lcm_tools import read_lcm_output


class SankeyGenerator:

    def format_links(self, x):
        res = []
        for i in x[0]:
            for idx in range(len(i) - 1):
                res.append([i[idx], i[idx + 1], x["index"]])
        return res

    def make_links(self, e, index):
        """Product of groups ids for each two consecutive groups periods"""
        prev = e[0]
        for i in e[1:]:
            yield from product(prev, i, [index])
            prev = i

    def sankey_preprocessing(self, input_file, user_apparition_threshold=0,
                             user_nunique_periods_threshold=3, keep_all_groups_in_periods=[]):

        le = LabelEncoder()
        demographics = extract_demographics(input_file)
        df = read_lcm_output(input_file).sort_values("period").reset_index(drop=True)

        file = f'{LINKS_FOLDER}/{input_file}'
        mlb = MultiLabelBinarizer(sparse_output=True)
        _df = mlb.fit_transform(df.user_ids.tolist()).astype(bool)
        _df = pd.DataFrame(_df.toarray(), columns=mlb.classes_)

        e = _df.sum()
        _df = _df[e[e > user_apparition_threshold].index]
        _df = _df.T.apply(lambda x: np.where(x)[0], axis=1)
        e = _df.to_frame()[0].apply(lambda x: list(list(z) for idx, z in groupby(x, lambda y: df.iloc[y].period)))
        e = e[e.apply(lambda x: len(x)) > user_nunique_periods_threshold]

        res = []
        e.to_frame().reset_index().apply(lambda x: [res.append(i) for i in self.make_links(x[0], x["index"])], axis=1)
        links = pd.DataFrame(res)

        links.columns = ["source", "target", "user_id"]
        links.groupby(["source", "target"])["user_id"].apply(lambda x: ','.join(str(i) for i in x)).to_frame().to_csv(
            file)

        # Keep groups appearing in at least one week
        file = f'{GROUPS_FOLDER}/{input_file}'
        groups_to_keep = np.unique(np.union1d(links.source.unique(), links.target.unique()))

        groups_to_keep = np.union1d(groups_to_keep, df[df.period.isin(keep_all_groups_in_periods)].index)
        df_groups = df.loc[groups_to_keep].dropna()
        df_groups['depth'] = le.fit_transform(df_groups.period) / df_groups.period.nunique()
        df_groups['size'] = df_groups.user_ids.apply(lambda x: len(x))
        if len(demographics) == 1:
            df_groups[demographics[0]] = df_groups.property_values
        else:
            df_groups[demographics] = df_groups.property_values.str.split("_", expand=True)

        # Encoding items to their initial ID + adding names
        self.dh = DatasetHandler()
        items = self.dh.get_items()
        df_groups.to_csv("test_csv.csv")
        df_groups["itemset_name"] = df_groups["itemsets"].apply(
            lambda x: get_items_descriptions(x, items))
        df_groups.to_csv(file)

        # Groups demographics stats
        file = f'{STATS_FOLDER}/{input_file}'
        stats = {}
        for i in np.intersect1d(GROUPS_DEMOGRAPHICS, demographics):
            b = df_groups.groupby(i).apply(lambda x: {"name": x[i].unique()[0], "value": x.index.shape[0],
                                                      "groups": ",".join(str(i) for i in x.index)}).values
            stats[i] = str(b.tolist())
        with open(file, 'w') as outfile:
            json.dump(stats, outfile)

        print("Done", input_file)
