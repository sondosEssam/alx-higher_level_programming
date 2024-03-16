#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        a = (len(sentence), sentence[0])
        return a
    return None
