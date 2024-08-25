#!/ur/bin/python3
"""
comment
"""


def find_peak(list_of_integers):
    """
    comment
    """
    if (list_of_integers is None):
        return None
    length = len(list_of_integers)
    if (length == 1):
        return (list_of_integers[0])
    elif (length == 2):
        return (max(list_of_integers[0], list_of_integers[1]))
    return sorted(list_of_integers)[-1]
