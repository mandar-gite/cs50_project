# shortener_app/schemas.py
# we here define what data  API expects from  client and the server
# shortener_app/schemas.py


from pydantic import BaseModel


class URLBase(BaseModel):
    target_url: str

class URL(URLBase):

    is_active: bool
    clicks: int
    class Config:
        orm_mode = True

class URLInfo(URL):

    url: str
    admin_url: str