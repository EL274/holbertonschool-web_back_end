#!/usr/bin/python3

def make_multiplier(multiplier : float) ->float :
    def multiplier_function(value : float) -> float :
        return multiplier * value 
    return multiplier_function
