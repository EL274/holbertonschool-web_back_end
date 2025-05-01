#!/usr/bin/env python3

"""
12-log_stats.py
Script pour afficher des statistiques sur les logs Nginx stockés dans MongoDB
"""

from pymongo import MongoClient


def get_nginx_log_stats():
    """Affiche les statistiques des logs Nginx."""
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    # Nombre total de logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Comptage par méthode HTTP
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Requêtes GET vers /status
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_count} logs with method=GET")
    print("\tpath=/status")


if __name__ == "__main__":
    get_nginx_log_stats()
