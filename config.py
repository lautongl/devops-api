# config.py

import os
from mongomock import MongoClient


class DevConfig:
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'port': 27017,
        'username': os.getenv('MONGODB_USER'),
        'password': os.getenv('MONGODB_PASSWORD')
    }


class ProdConfig:

    MONGODB_USER = os.getenv('MONGODB_USER')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
    MONGODB_HOST = os.getenv('MONGODB_HOST')
    MONGODB_DB = os.getenv('MONGODB_DB')
    MONGODB_CLUSTER = os.getenv('MONGODB_CLUSTER')

    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://%s:%s@%s/%s?retryWrites=true&w=majority'
                '&appName=%s' % (
                                    MONGODB_USER,
                                    MONGODB_PASSWORD,
                                    MONGODB_HOST,
                                    MONGODB_DB,
                                    MONGODB_CLUSTER
                )
    }


class MockConfig:
    MONGODB_SETTINGS = {
        'db': 'users',
        'mongo_client_class': MongoClient
    }
