#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ret_list = []
    for idx in range(list_length):
        try:
            div = my_list_1[idx]/my_list_2[idx]
        except (ZeroDivisionError, TypeError, IndexError) as err:
            if isinstance(err, ZeroDivisionError):
                print("division by 0")
            elif isinstance(err, TypeError):
                print("wrong type")
            elif isinstance(err, IndexError):
                print("out of range")
            div = 0
        finally:
            ret_list.append(div)
    return ret_list
