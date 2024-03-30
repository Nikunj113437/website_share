import MySQLdb
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'Nikunj@0562',
    'db': 'enquiry',
}

conn = MySQLdb.connect(**db_config)
