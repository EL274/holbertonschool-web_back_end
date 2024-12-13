#!/usr/bin/env python3
"""This module contains a method use to implement mongodb"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
