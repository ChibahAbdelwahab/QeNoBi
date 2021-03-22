import os
from ast import literal_eval

from sqlalchemy import create_engine
import pandas as pd


def format_links(links):
    links["value"] = links.user_id.apply(len)
    links["lineStyle"] = "{'color': '#a8dadc', 'opacity': 1}"
    links[["source", "target", "user_id", "label", "lineStyle"]]
    links = list(links.T.to_dict().values())
    return links


def format_groups(groups):
    groups = groups.loc[groups.index.dropna()]
    groups.index = groups.index.astype(str)
    groups.reset_index(inplace=True)
    groups = groups.replace({'None': "id"})
    groups = groups.rename(columns={"customer_id": "user_ids", "index": "name"})
    groups[""] = groups["name"]
    groups["user_ids"] = groups.user_ids.apply(literal_eval).apply(list)
    groups["size"] = groups.user_ids.apply(len)
    groups["itemset"] = groups.itemset.apply(literal_eval).apply(list)
    depth_dict = {i: idx * 100 / groups.period.nunique() for idx, i in enumerate(groups.period.unique())}
    groups["depth"] = groups.period.apply(lambda x: depth_dict[x])
    groups.period = pd.to_datetime(groups.period).dt.date.astype(str)
    periods = [str(i) for i in groups.period.unique()]
    groups = list(groups.T.to_dict().values())
    return groups, periods


def get_sankey_data(sankey_experiment_id, query=None):
    query = """
                Select * from "{}" where sankey_experiment_id='{}' 
        """
    engine = create_engine(os.environ.get('DATABASE_URL'))
    groups = pd.read_sql(query.format("mgb_groups", sankey_experiment_id), con=engine)
    links = pd.read_sql(query.format("mgb_links", sankey_experiment_id), con=engine).astype(str)
    engine.dispose()

    groups, periods = format_groups(groups)
    links.user_id = links.user_id.apply(literal_eval).apply(list)
    links = format_links(links)
    return groups, links, periods


def run_sankey_query(links_filter, sankey_experiment_id):
    assert len(links_filter) == 2
    query = f"""
                select l1.id id1 ,l2.id id2 
            from mgb_links l1
                     join mgb_links l2 on l2.source = l1.target
            where l1.sankey_experiment_id = '{sankey_experiment_id}'
              and l2.sankey_experiment_id = '{sankey_experiment_id}'
              and l1.label = '{links_filter[0]}'
              and l2.label = '{links_filter[1]}'
              
    """
    engine = create_engine(os.environ.get('DATABASE_URL'))
    links_ids = pd.read_sql(query, con=engine)
    links_ids = set(links_ids.id1.unique()).union(links_ids.id2.unique())

    query = f"""
                  Select * from "mgb_links" where sankey_experiment_id='{sankey_experiment_id}' and id in ({','.join(str(i) for i in links_ids)}) 
          """
    links = pd.read_sql(query, con=engine)
    query = """
              Select * from "{}" where sankey_experiment_id='{}' 
      """
    groups = pd.read_sql(query.format("mgb_groups", sankey_experiment_id), con=engine)
    groups = groups.loc[set(links.source.unique()).union(links.target.unique())]
    a = groups.reset_index().rename(columns={"index": "name"})
    engine.dispose()
    links.source = links.source.apply(lambda x: a[a.name == x].index[0])
    links.target = links.target.apply(lambda x: a[a.name == x].index[0])

    links = format_links(links)
    groups, periods = format_groups(groups)
    return groups, links, periods
