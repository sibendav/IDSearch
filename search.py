# -*- coding: utf-8 -*-

#search

"""
Efart Anconina 322796749
Simha Ben-David 209166773
"""
import state
import frontier
import time


def search(n):
    num=1
    maxi=0
    s=state.create(n)
    print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            return s
        ns=state.get_next(s)
        num+=len(ns)
        for i in ns:
            frontier.insert(f,i)
        if maxi<len(ns):
            maxi=len(ns)
    
    return 0

start = time.time()
example=search(3)
print(example)
print ('The script took {0} second !'.format(time.time() - start))

start = time.time()
example=search(4)
print(example)
print ('The script took {0} second !'.format(time.time() - start))