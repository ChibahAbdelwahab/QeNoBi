def get_items_descriptions(x, items):
    """
    Returns a list of items description from a list of items ids
    """
    if isinstance(x, int):
        x = str(x)

    return items.loc[[int(i) for i in x.split()]].description.tolist()
