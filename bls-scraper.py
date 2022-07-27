#Author:sidious
import os
import psycopg2
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


def main():
    
    conn=None
    cur=None
    ssScrape='https://blackarch.org/tools.html'   
    ssCreate='CREATE TABLE IF NOT EXISTS "pentest" ( "id" serial NOT NULL, PRIMARY KEY ("id"), "appver" text NOT NULL, "appname" text NOT NULL, "appdesc" text NOT NULL )'
    ssStatement='INSERT INTO pentest (appver, appname, appdesc) VALUES (%s, %s, %s);'
    ssCheck='SELECT id,appver,appname,appdesc FROM pentest WHERE id=2107;'
    load_dotenv()
    
    try:
        data=requests.get(ssScrape)
        soup=BeautifulSoup(data.text, 'html.parser')
        pwnTools=soup.find('table', { 'id': 'tbl-minimalist'})
        tBody=pwnTools.find('tbody')

        conn=psycopg2.connect(
        database=os.getenv('ss_database'),
        user=os.getenv('ss_user'),
        password=os.getenv('ss_password'),
        host=os.getenv('ss_host'))
        cur=conn.cursor()

        for tr in tBody.find_all('tr'):
            spVersion=tr.find_all('td')[1].text.strip()
            spApplication=tr.find_all('td')[0].text.strip()
            spDescription=tr.find_all('td')[2].text.strip()
            cur.execute(ssCreate)
            sqlStatement=(ssStatement)
            cur.execute(sqlStatement,(spVersion, spApplication, spDescription))
            conn.commit()
        sqlCheck=(ssCheck)
        cur.execute(sqlCheck)
        tableRows=cur.fetchall()

        if not len(tableRows):
            print("Insert job failed.\n")
        else:
            print("Insert job completed.\n")
    
    except Exception as error:
        print(error)
    
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    main()
