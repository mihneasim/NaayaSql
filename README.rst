Producte.NaayaSql - simple database connection interface for Naaya
==================================================================
This product provides the ability to ask and retrieve a connection
to an sqlite database.

Requirements
============
This is a product designed for Naaya ().
It requires pysqlite2 for python 2.4 since Naaya is currently running
the 2.4 version of python. Python includes sqlite3 since 2.5.
Visit pysqlite2 download page 
(http://docs.pysqlite.googlecode.com/hg/sqlite3.html) 
or install it via easy_install/pip. Documentation for pysqlite2 can be 
found here (http://code.google.com/p/pysqlite/downloads/list).

Usage
=====

Creating a database::

 db = naayasql.new_db()
 your_object.my_db = db

`db` or `my_db` property of `your_object` is an NSDb persistent object. 
You can later on retrieve a cursor for the same database.

Retrieving a cursor for a database, executing queries::

 cursor = your_object.my_db.cursor()
 cursor.execute("CREATE TABLE t(x INTEGER PRIMARY KEY ASC, y, z)")
 # or simply:
 your_object.my_db.cursor().execute("DROP TABLE t")

`NSDb.cursor()` raises `NSDb.DbMissing` exception if db is missing
or it hasn't been previously created.

Deleting a database::

 your_object.my_db.drop()
 del your_object.my_db
