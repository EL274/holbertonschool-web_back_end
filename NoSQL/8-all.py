#!/usr/bin/env python3
"""This module contains a method use to implement mongodb"""


def list_all(mongo_collection):
    """Returns a list of all documents in the collection"""
    return mongo_collection.find()
