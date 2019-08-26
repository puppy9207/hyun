import csv
import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

with open('dataset_2.csv','r', encoding="utf-8-sig") as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['Date'], i['predict']) for i in dr]

cur.executemany("INSERT INTO vegit_vegit (vegit_date, vegit_pred) VALUES (?, ?);", to_db)
conn.commit()
conn.close()
