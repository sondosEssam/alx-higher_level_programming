#!/usr/bin/python3
"""
1-mylist module
"""


class MyInt(int):
    """
    rectangle
    """

    def __eq__(self, otherself):
        """
        str method
        """
        if isinstance(self, int) is isinstance(otherself, int):
            return False
        else:
            return True

    def __ne__(self, otherself):
        """
        str method
        """
        if isinstance(self, int) is isinstance(otherself, int):
            return True
        else:
            return False
