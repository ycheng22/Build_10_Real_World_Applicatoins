# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 17:50:05 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

Reference:
"""
import psycopg2

def create_table():
    #conn = psycopg2.connect("dbname='db1' user='postgres' password='2020' host='localhost' port='5433'")
    conn = psycopg2.connect("host=127.0.0.1 port=5433 dbname=db1 user=postgres password=2020")
    cur = conn.cursor()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
    
def insert(item, quantity, price):
    conn = psycopg2.connect("host=127.0.0.1 port=5433 dbname=db1 user=postgres password=2020")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("host=127.0.0.1 port=5433 dbname=db1 user=postgres password=2020")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("host=127.0.0.1 port=5433 dbname=db1 user=postgres password=2020")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("host=127.0.0.1 port=5433 dbname=db1 user=postgres password=2020")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
#insert("Orange", 10, 1.5)
#delete("Orange")
update(20, 26.5, "Apple")
print(view())
#insert("Coffe Cup", 10, 5)
#update(11, 6,  "Coffe Cup")
#delete("Wine Glass")




