#!/usr/bin/env python3


from pymongo import MongoClient

# Connexion à la base de données MongoDB
client = MongoClient('localhost', 27017)
db = client.logs
collection = db.nginx

# Nombre total de documents
total_logs = collection.count_documents({})

# Nombre de documents par méthode
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

# Nombre de documents avec méthode GET et path /status
status_count = collection.count_documents({"method": "GET", "path": "/status"})

# Affichage des résultats
print(f'{total_logs} logs')
print('Methods:')
for method in methods:
    print(f'\tmethod {method}: {method_counts[method]}')
print(f'method=GET path=/status: {status_count}')
