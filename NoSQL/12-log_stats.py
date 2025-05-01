#!/usr/bin/env python3

"""
12-log_stats.py
Script pour afficher des statistiques sur les logs Nginx stockés dans MongoDB
"""

from pymongo import MongoClient


def log_stats():
    """
    Fournit des statistiques sur les logs Nginx stockés dans MongoDB.
    Affiche :
    - Le nombre total de logs
    - Le nombre de requêtes pour chaque méthode HTTP
    - Le nombre de requêtes GET vers le chemin /status
    """
    # Connexion à la base de données MongoDB locale
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx
    
    # Compte le nombre total de documents dans la collection
    total = collection.count_documents({})
    print(f"{total} logs")
    
    # Affiche les statistiques par méthode HTTP
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        # Compte le nombre de requêtes pour chaque méthode
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")
    
    # Compte le nombre de requêtes GET vers /status
    status = collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{status} status check")


if __name__ == "__main__":
    log_stats()
