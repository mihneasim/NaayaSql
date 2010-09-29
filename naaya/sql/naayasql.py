# Python imports
import os.path
from os import remove
try:
    import sqlite3
except ImportError:
    from pysqlite2 import dbapi2 as sqlite3
import sha
import string
from base64 import b64encode
from random import choice

# Zope imports
from Globals import Persistent

DBS_FOLDER_PATH = CLIENT_HOME

class DbMissing(Exception):
    pass

class NaayaSqlDb(Persistent):

    def __init__(self, db_id):
        self.db_id = db_id

    def get_path(self):
        """Used by the other methods"""
        return os.path.join(DBS_FOLDER_PATH, self.db_id)

    def cursor(self, isolation_level=None):
        if not os.path.exists(self.get_path()):
            raise DbMissing
        connection = sqlite3.connect(self.get_path(),
                                     isolation_level=isolation_level)
        return connection.cursor()

    def drop(self):
        """Drop database, delete it from disk"""
        remove(self.get_path())


def new_db():
    exists = lambda x: (os.path.exists(os.path.join(DBS_FOLDER_PATH, x))
                        or os.path.exists(os.path.join(DBS_FOLDER_PATH,
                                                       x + '-journal')))
    unique = False
    while not unique:
        salt = ''.join([choice(string.letters) for i in range(10)])
        id = b64encode(sha.new(salt).digest(), '-_')[:8]
        unique = not exists(id)
    path = os.path.join(DBS_FOLDER_PATH, id)
    connection = sqlite3.connect(path)
    connection.close()
    return NaayaSqlDb(id)

