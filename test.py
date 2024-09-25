#!/usr/bin/python3
import mysql.connector
conn = mysql.connector.connect(host='localhost', password='@bienvenido45', user='root')

if conn.is_connected() :
    print("Connection established...")