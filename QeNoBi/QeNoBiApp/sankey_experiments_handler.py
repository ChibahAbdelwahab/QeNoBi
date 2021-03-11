import os
from ast import literal_eval

from sqlalchemy import create_engine


def get_sankey_data(sankey_experiment_id):
    import pandas as pd
    engine = create_engine(os.environ.get('DATABASE_URL'))

    query = """
            Select * from "{}" where sankey_experiment_id='{}' 
    """

    groups = pd.read_sql(query.format("mgb_groups", sankey_experiment_id), con=engine)
    groups = groups.loc[groups.index.dropna()]
    groups.index = groups.index.astype(str)
    groups.reset_index(inplace=True)
    groups = groups.replace({'None': ""})
    groups = groups.rename(columns={"customer_id": "user_ids", "index": "name"})
    groups[""] = groups["name"]
    groups["user_ids"] = groups.user_ids.apply(literal_eval).apply(list)
    groups["size"] = groups.user_ids.apply(len)
    groups["itemset"] = groups.itemset.apply(literal_eval).apply(list)
    depth_dict = {i: idx * 100 / groups.period.nunique() for idx, i in enumerate(groups.period.unique())}
    groups["depth"] = groups.period.apply(lambda x: depth_dict[x])
    groups.period = pd.to_datetime(groups.period).dt.date.astype(str)
    groups = list(groups.T.to_dict().values())
    print(query.format("mgb_links", sankey_experiment_id))
    links = pd.read_sql(query.format("mgb_links", sankey_experiment_id), con=engine).astype(str)
    links.user_id = links.user_id.apply(literal_eval).apply(list)
    links["value"] = links.user_id.apply(len)
    links["lineStyle"] = "{'color': '#1d3557', 'opacity': 1}}"
    links[["source", "target", "user_id", "label", "lineStyle"]]
    links = list(links.T.to_dict().values())
    engine.dispose()
    return groups, links
