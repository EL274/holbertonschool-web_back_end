#!/usr/bin/env python3
"""This module contains a method use to implement mongodb"""
from pymongo import MongoClient


def display_information(mongo_collection):
    """Provides some stats about Nginx logs"""
    print("{} logs".format(mongo_collection.count_documents({})))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print("\tmethod {}: {}".format(
            method, mongo_collection.count_documents({"method": method})))

    print("{} status check".format(mongo_collection.count_documents(
        {"method": methods[0], "path": "/status"})))
