#!/usr/bin/env python3
"""Ce module contient une méthode utilisée pour implémenter mongodb"""


def insert_school(mongo_collection, **kwargs):
    """Insère un nouveau document dans une collection basée sur kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
