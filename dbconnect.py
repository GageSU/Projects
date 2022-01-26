#
#       Heroku Linkage Software
#       Author: Stephen Coyne
#       Version: 2.1 --- Faster Connectivity
#

import psycopg2
from psycopg2 import Error

def connect(records):
    newRecords = []
    try:
        #Connect to database
        conn = psycopg2.connect(user="fyvfgbrmzsdxqv",
                                password="f9bd96ad063a4183904cc463789f189038c4a5fdab483a05001908ee40a36a30",
                                host="ec2-18-214-214-252.compute-1.amazonaws.com",
                                port="5432",
                                database="d2shnh1e69v774")
        for x in records:
            i_record = x
            id = i_record[0]
            name = i_record[1]
            if checkdb(id, conn):
                name = retrieveCode(id, conn)
            elif len(name) != 0:
                addRecord(i_record, conn)
            record = (id, name)
            newRecords.append(record)
    except (Exception, Error) as error:
        print('Error', error)
    finally:
        if conn:
            conn.close()
            return(newRecords)

def checkdb(id, conn):
    id_exists = False
    try:
        cur = conn.cursor()
        cur.execute('select * from player;')
        table = cur.fetchall()
        id_numbers = [f_tuple[0] for f_tuple in table]
        print(id_numbers)
        if isinstance(id, int):
            if id in id_numbers:
                id_exists = True
            else:
                id_exists = False
    except (Exception, Error) as error:
        print('Error', Error)
    cur.close()
    return(id_exists)

def retrieveCode(id, conn):
    try:
        cur = conn.cursor()
        cur.execute("select * from player;")
        for record in cur:
            if record[0] == id:
                result = record[3]
                break
    except (Exception, Error) as error:
        print('Error', error)
    cur.close()
    return(result)

def addRecord(record, conn):
    try:
        cur = conn.cursor()
        insert_query = """ Insert into player (id,first_name, last_name, codename) values (%s,'None','None',%s)"""
        cur.execute(insert_query, record)
        conn.commit()
    except (Exception, Error) as error:
        print('Error', error)
