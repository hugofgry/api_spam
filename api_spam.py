from fastapi import FastAPI
import uvicorn
import json
import sys
import os
from fastapi.responses import JSONResponse
import psycopg2 as pg

app = FastAPI()
# Connection a la base sqlite
conn = pg.connect(database="d9f6fj4b8b8dc8",
          user = "qeahfvfnzodzwp",
          password = "a94d8dac32348f111474ebc5c932172a1a28926cee300c5017579b7024c6cebe",
          host = "ec2-34-247-151-118.eu-west-1.compute.amazonaws.com",
          port = "5432")
c = conn.cursor()



@app.get("/spam")
async def spam_message ():
    c.execute("SELECT * FROM spam_message WHERE type= 'spam';")
    spam = c.fetchall()
    conn.commit()
    return spam

@app.get("/ham")
async def ham_message ():
    c.execute("SELECT * FROM spam_message WHERE type= 'ham';")
    ham = c.fetchall()
    conn.commit()
    return ham
