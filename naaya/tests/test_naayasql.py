# Python imports
from unittest import TestSuite, makeSuite
import random

# Zope imports

# Naaya imports
from Products.Naaya.tests.NaayaTestCase import NaayaTestCase
from naaya.sql import new_db, NaayaSqlDb, DbMissing

class NaayaSqlTestCase(NaayaTestCase):
    
    generic_obj = Persistent()

    def afterSetup(self):
        db = getattr(self.generic_obj, "db", None)
        if db is None:
            self.generic_obj.db = new_db()
        self.c = self.generic_obj.db.cursor()

    def beforeTearDown(self):
        self.c.close()

    def test_queries(self):
        self.c.execute("CREATE TABLE t(x integer primary key)")
        self.c.execute("INSERT INTO t(x) values(?)", (13, ))
        self.c.execute("SELECT * from t")
        self.assertEqual(self.c.fetchall(), [(3,)])

    def test_changedb(self):
        self.generic_obj.db.drop()
        self.assertRaises(DbMissing, self.generic_obj.db.cursor)
        del self.generic_obj.db
        self.generic_obj.db = new_db()
        self.c = self.generic_obj.db.cursor()

    def test_new_db_stress_test(self):
        """Create 100 dbs, each with 1 table with 1 record,
        then test them and drop them in reverse order

        """
        pool = []
        size = 100
        for i in range(size):
            pool.append(new_db())
        for i in range(size):
            pool[i].cursor().execute("CREATE TABLE t(x integer primary key)")
            self.c.execute("INSERT INTO t(x) values(?)", (i, ))
        for i in range(size):
            crs = pool[size-i-1].cursor()
            crs.execute("SELECT * from t")
            self.assertEqual(crs.fetchall(), [(size-i-1, )])
            crs.close()
            pool[size-i-1].drop()

def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(NaayaSqlTestCase))
    return suite
