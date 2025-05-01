#!/usr/bin/env python3
"""Ce module contient une méthode utilisée pour implémenter mongodb"""


def schools_by_topic(mongo_collection, topic):
    """Renvoie la liste des écoles ayant un sujet spécifique"""
    return mongo_collection.find({"topics": {"$all": [topic]}})
