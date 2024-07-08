import os


class DevConfig:
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'port': 27017,
        'username': os.getenv('MONGODB_USER'),
        'password': os.getenv('MONGODB_PASSWORD')
    }


class MockConfig:

    {
        'db': 'users',
        'host': 'mongodb://localhost',
    }
