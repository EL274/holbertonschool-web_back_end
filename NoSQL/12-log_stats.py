#!/usr/bin/env python3

"""
12-log_stats.py
Script pour afficher des statistiques sur les logs Nginx stockés dans MongoDB
"""

from pymongo import MongoClient

def get_nginx_log_stats():
    # Connexion à MongoDB (par défaut sur localhost:27017)
    client = MongoClient('mongodb://localhost:27017/')
    # Accès à la base de données 'logs'
    db = client['logs']
    # Accès à la collection 'nginx'
    collection = db['nginx']
    
    # Nombre total de logs dans la collection
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Comptage par méthode HTTP
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        # Compte le nombre de documents pour chaque méthode
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")  # \t pour la tabulation
    
    # Comptage spécifique pour GET /status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} logs with method=GET\n\tpath=/status")

if __name__ == "__main__":
    get_nginx_log_stats()
