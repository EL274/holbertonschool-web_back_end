#!/usr/bin/env python3
"""Ce module contient une méthode utilisée pour implémenter mongodb"""


def update_topics(mongo_collection, name, topics):
    """modifie tous les sujets d'un document scolaire en fonction du nom"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
