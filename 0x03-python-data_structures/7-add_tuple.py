#!/usr/bin/python3


for i in range(2):
    if len(tuple_a) < 2:
        tuple_a.append(0)
    if len(tuple_b) < 2:
        tuple_b.append(0)
    new_tuple.append(tuple_a[i]+tuple_b[i])
return(tuple(new_tuple))
