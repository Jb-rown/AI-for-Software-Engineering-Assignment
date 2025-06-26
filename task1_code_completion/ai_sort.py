def sort_dict_list_ai(dict_list, key):
    """
    Sort a list of dictionaries by a given key.
    Args:
        dict_list (list): List of dictionaries.
        key (str): Key to sort by.
    Returns:
        list: Sorted list of dictionaries.
    """
    try:
        return sorted(dict_list, key=lambda x: x[key])
    except KeyError:
        print(f"Key '{key}' not found in one or more dictionaries.")
        return dict_list