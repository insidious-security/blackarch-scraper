import os
import json 
import psycopg2

from dotenv import load_dotenv
from typing import Optional
from fastapi import FastAPI, Response
from psycopg2.extras import RealDictCursor

load_dotenv()
app = FastAPI()

@app.get("/black/{tool_id}")
def read_item(tool_id): 
    try:
        conn=psycopg2.connect(
        database=os.getenv('ss_database'),
        user=os.getenv('ss_user'),
        password=os.getenv('ss_password'),
        host=os.getenv('ss_host'))
        cur = conn.cursor(cursor_factory=RealDictCursor)
        sql1 = "SELECT id,appver,appname,appdesc FROM pentest WHERE id = %s;"
        cur.execute(sql1,[tool_id,])
        payload = json.dumps(cur.fetchall(), indent=2, default=str)
    
    except Exception as error:
        print(error)
    
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return Response(content=payload, media_type="application/json")
  
