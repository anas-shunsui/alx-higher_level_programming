#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    score = None
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            if value > max:
                max = value
                score = key
        return (score)
    else:
        return (None)
