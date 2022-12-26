# shortener_app/main.py
from . import schemas, models, crud, database,config
import validators
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from starlette.datastructures  import URL

# from .database import SessionLocal, engine

# configure API
app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)


# Aceess to root file  or index
@app.get("/")
def read_root():

    return "Welcome to the URL shortener API of LFW :)"


""" Raise bad request exception"""
def raise_bad_request(message):
    
    raise HTTPException(status_code=400, detail=message)


""" Raise not found exception"""
def raise_not_found(message):

    return HTTPException(status_code=404, detail=message)



""""Raise not valid"""
def raise_not_valid(message):

    return HTTPException(status_code=404, detail=message)


""" Access database as defined in database.py """
def get_db():
    ''' function to create connection with database
    '''
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""   Create route from post request and create short code for this URL if its valid """
@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):

    if not validators.url(url.target_url):

        raise_bad_request(message="Your provided URL is not valid")

    db_url = crud.create_db_url(db=db, url=url)

    return add_admin_info (db_url)


""" forward the shortened URL to the database for storing in table  """
@app.get("/{url_key}")
def forward_to_target_url(
    url_key: str,
    request: Request,
    db: Session = Depends(get_db)
):
    # TODO: check if this is working
     
        
        if db_url := crud.get_db_url_by_key(db=db, url_key=url_key):
            crud.update_visitor_count_db(db=db, db_url=db_url)
            return RedirectResponse(db_url.target_url)
        else:
            raise_not_found(request)
     



"""Define a new API endpoint  administration info"""
@app.get("/admin/{secret_key}", name = "administration info", response_model= schemas.URLInfo,)

# 
def get_url_info(secret_key: str, request: Request, db: Session= Depends(get_db)):
    
    # get url information if the corrosponding secret key exists in the database
    if db_url := crud.get_db_url_by_secret_key(db, secret_key):
        return add_admin_info(db_url)
    else:
        raise_not_found(request)
    

""" create a function to render url which joins  shortened key and secret key (i.e. after doamin: port / of the server)"""
def add_admin_info(db_url:models.URL) -> schemas.URLInfo:
    
    #access the base URL as specified in the config file 
    base_url = URL(config.get_settings().base_url)
    # cretae admin_endpoint path to add to base URL 
    admin_endpoint = app.url_path_for("administration info", secret_key= db_url.secret_key)
    # update the db_url (an entry in data base in this case) by joining the keys to host  
    db_url.url  =  str(base_url.replace(path=db_url.key))
    db_url.admin_url = str(base_url.replace(path=admin_endpoint))
    return db_url


""" function to delete an entry from the database"""
@app.delete("/admin/{secret_key}")

def delete_url(secret_key: str, request: Request, db: Session = Depends(get_db)):

    if db_url := crud.deactivate_db_url_by_secret_key(db, secret_key=secret_key):

        message = f"Successfully deleted shortened URL for '{db_url.target_url}'"

        return {"detail": message}

    else:

        raise_not_found(request)