#!/usr/bin/env python

import m_log as log
import psycopg2 as pg
import m_conf as conf
import os

# Clean console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_space(item, size):
    item_len = len(str(item))
    item = str(item)
    if item_len >= size:
        return item
    for i in range(size - item_len):
        item = ' ' + item
    return item

def __pg_request(query):

    db_conf = conf.get_conf('db.conf')
    try:
        conn = pg.connect("dbname='" + str(db_conf['DB']) + "' user='" + str(db_conf['USER']) + "' host='" + str(db_conf['IP']) + "' password='" + str(db_conf['PWD']) +"'")
        cursor =  conn.cursor()
        cursor.execute(query)
        conn.commit()
        if query[:6:] == 'SELECT':
            data = cursor.fetchall()
        else:
            data='Query done : ' + query
        cursor.close()
    except ValueError:
        print 'Unable to connect database : \n' + ValueError
        m_log.write_log('appli.log','m_IO.__pg_request | Unable to manage the database link' + str(ValueError))
        return False
    return data
