#!/usr/bin/python3
"""
1-mylist module
"""


class MyList(list):
    """
    MyList
    """

    def print_sorted(self):
        """
        print sorted
        """
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
