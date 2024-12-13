#!/usr/bin/env python3
"""This module contains a method use to implement mongodb"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    return mongo_collection.find({"topics": {"$all": [topic]}})
