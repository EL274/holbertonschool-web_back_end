#!/usr/bin/env python3
"""Ce module contient une méthode utilisée pour implémenter mongodb"""


def list_all(mongo_collection):
    """Renvoie une liste de tous les documents de la collection"""
    return mongo_collection.find()
