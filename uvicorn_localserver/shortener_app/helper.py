# shortener_app/helper.py

import secrets
import string

from sqlalchemy.orm import Session

from . import crud

"""function to genearte  a key randomly using letter and digits """
def create_key(length: int = 5) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for i in range(length))


"""keep creating keys till it is unique"""
def create_unique_key(db: Session) -> str:
    key = create_key() # create a key 
    while crud.get_db_url_by_key(db, key): #check if  key generated exists and if no, create a new one
        key = create_key()
    return key
                   
                   
