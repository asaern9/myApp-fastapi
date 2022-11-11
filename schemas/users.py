from pydantic import BaseModel, EmailStr
from uuid import UUID


class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class Users(BaseModel):
    id: int     # UUID - for auto generated ID's
    name: str
    username: str
    email: EmailStr
    address: Address
    phone: str
    website: str
    company: Company
