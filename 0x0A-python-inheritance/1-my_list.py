#!/usr/bin/python3
"""
1-mylist module
"""

class MyList(list):
    """
    MyList
    """

    def __init__(self):
        """
        init
        """
        super().__init__

    def print_sorted(self):
        """
        print sorted
        """
        print(sorted(self))
