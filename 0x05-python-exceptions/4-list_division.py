#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    res = []
    j = 0
    for i in range(0, list_length):
        try:
            j = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            j = 0
            pass
        except (ZeroDivisionError):
            print("division by 0")
            j = 0
            pass
        except IndexError:
            print("out of range")
            j = 0
            pass
        finally:
            res.append(j)
    return res
