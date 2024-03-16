#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        a = None
        return a
    a = (len(sentence), sentence[0])
    return a
