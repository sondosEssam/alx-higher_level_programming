#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    res = []
    for i in range(0, list_length):
        try:
            res.append(my_list_1[i] / my_list_2[i])
            
        except (TypeError, ValueError):
            print("wrong type")
            res.append(0)
            pass
        except (ZeroDivisionError):
            print("division by 0")
            res.append(0)
            pass
        except IndexError:
            print("out of range")
            res.append(0)
            pass
    return res
