def sort_dict_list_manual(dict_list, key):
    """
    Sort a list of dictionaries by a specified key.
    Args:
        dict_list (list): List of dictionaries.
        key (str): Key to sort by.
    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(dict_list, key=lambda x: x[key])