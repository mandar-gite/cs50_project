# shortener_app/crud.py

from sqlalchemy.orm import Session

from . import helper, models, schemas

""" Function to create url for data base """


def create_db_url(db: Session,
                  url: schemas.URLBase) -> models.URL:

    # create unique key using function in the helper file
    key = helper.create_unique_key(db)
    # create secret key by joing the unique with 8 char long random key
    secret_key = f"{key }_{helper.create_key(length=8)}"
    # create a variable to hold the generated key pass it on as URL defined in the models.URL
    db_url = models.URL(target_url=url.target_url,
                        key=key,
                        secret_key=secret_key)

    # CRUD action - add this to    table  of shortner.db database
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return db_url


 # TODO: see if this can be moved to helper file where other keys are generated
"""check if a key already exists in your database:"""


def get_db_url_by_key(db: Session, url_key: str) -> models.URL:
    return (
        db.query(models.URL)
        .filter(models.URL.key == url_key, models.URL.is_active)
        .first()
    )


""" Update the visitor count in urls table of shortner.db database"""


def update_visitor_count_db(db: Session, db_url: schemas.URL) -> models.URL:
    db_url.clicks += 1
    db.commit()
    db.refresh(db_url)
    return db_url


""" check database for an active database entry with the provided secret_key."""
def get_db_url_by_secret_key(db: Session, secret_key: str) -> models.URL:
    # function returns either first occurance of the secret key or if not found it return none
    return (db.query(models.URL)
            .filter(models.URL.secret_key == secret_key,
            models.URL.is_active)
            .first()
            )

""" Deactivate a link - Do Not Delete even if chosen by user- for future refernce"""
def deactivate_db_url_by_secret_key(db: Session, secret_key: str) -> models.URL:
    db_url = get_db_url_by_secret_key(db, secret_key)
    if db_url:

        db_url.is_active = False

        db.commit()

        db.refresh(db_url)

    return db_url
