# Python imports
import os.path
try:
    import sqlite3
except ImportError:
    from pysqlite2 import dbapi2 as sqlite3

# Zope imports
from Persistance import Persistent

# Naaya imports
from Products.NaayaCore.managers.utils import genRandomId, uniqueId

DBS_FOLDER_PATH = CLIENT_HOME

class DbMissing(Exception):
    pass

class NaayaSqlDb(Persistent):

    def __init__(self, db_id):
        pass

    def cursor(self):
        pass

    def drop(self):
        pass

def new_db():
    exists = lambda x: (os.path.exists(os.path.join(DBS_FOLDER_PATH, x))
                        or os.path.exists(os.path.join(DBS_FOLDER_PATH,
                                                       x + '-journal')))
    id = uniqueId(genRandomId(), exists)
    path = os.path.join(DBS_FOLDER_PATH, id)
    connection = sqlite3.connect(path)
    connection.close()
    return NaayaSqlDb(id)


