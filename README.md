Leap For Word is a social enterprise working to make India English Literate. The teachers from government schools are trained and certified to use the techniques designed to teach English to students. 

The acquisition of teachers involves digital marketing on WhatsApp groups and social media to drive traffic to digital properties.  

This consists in sharing campaign links with the audience. The campaigns are conducted weekly for the teachers' acquisition, onboarding, certification, and servicing. 

Once a year, a multi-state world power championship is arranged for students of 7 states of India, involving 1 million students. The event requires driving traffic to digital properties. 

# Motivation :
The LfW ops require substantial sharing of URLs for the acquisition and servicing of the teacher and students. LfW presently uses paid third-party URL shorteners. They are effieicnt and effective however  there is cost involved and lack of customisation .leads to subscribing features which are not required at all .  Need is felt of a simple in house shortner service 

# TODO 

There is scope for the integration of in-house shorteners with the CRM. 


# Project  Structure 

The url shortener has two distinct parts . The first part , a  back end,  which handles the long URL,  converts them into short URL and stores data of the URLs in the database . The second part is the front end which allows user to register, login , shorten URL and access the history of short  URLS created . This is UI for the user and needs to be aesthetically and functionally appealing 

## PART 1 - REST API 

#### Libraries Used

- WebFramework :   fastapi - 0.75.0 
- Development Server :  uvicorn: 0.17.6
- Validation - Validtors- 0.18.2
 - Database Toolkit - SQLAlchemy  - 1.4.32`
- Environment Variables- dotenv - 0.19.2`
- Database - SQLite3
- Random Alphanumerical Combination - Secrets


#### Files

##### 1. main.py
 
This file is key file of the folder  which acts as fulcrum around which entire project revolves . Sort of  entry point  for users to interact with the larger codebase .  Broadly , It does the following activities
* Defines endpoints
* Handles  interchanges between modules defined in constituent files    
* receives environment variables through config.py file 
* receives processed data from the functions and parses it to end points
* initiates database operations via crud.py file 

Following major functions are defined in the file :

| Function              | Purpose                                                        |
| --------------------- | -------------------------------------------------------------- |
| get_db                | function to establish connection with database                 |
| read_root             | GET Endpoint for index                                         |
| create_url            | POST Endpoint to receive long URL                              |
| get_url_info          | GET Endpoint for send the url Info if secret key is available  |
| forward_to_target_url | forward the shortend URL to Database using function in CRUD.py |
| delete                 |DELETE Endpoint to delete an entry in the Database                                                                |

##### 2. crud.py

This file predominantly uses Session class of sqlalchemy.orm module to open a data base . Database entry create , read , add and delete operations are carried out in the database using the following functions.  


| Function                        | Purpose                                                                       |
| ------------------------------- | ----------------------------------------------------------------------------- |
| get_db_url_by_key               |   check if a key already exists in your database                                                                            |
| create_db_url                   | Function to create url for data base                                          |
| update_visitor_count_db         | Update the visitor count in urls table of shortner.db database                |
| get_db_url_by_secret_key        | check database for an active database entry with the provided secret_key.     |
| deactivate_db_url_by_secret_key | Deactivate a link - Do Not Delete even if chosen by user- for future reference | 

##### 3. helper.py

This file handles key generation using secrets library  . Create_unique_key  checks if generated key exist in table and generates another key till this condition is satisfied. 

| Function          | Purpose                                                        |
| ----------------- | -------------------------------------------------------------- |
| create_key        | function to genearte a key randomly using letter and digits    |
| create_unique_key | keep creating keys till it is unique using create_key function |                                                                |

##### 4. schemas.py

This file defines what information is expected by the API from client ( user) . It uses BaseModel class of pydantic module.  The classes and sub-classes are defined  as follows:

| Class   | Parent Class | Vairable                  |
| ------- | ------------ | ------------------------- |
| URLBase | BaseModel    | target_url                |
| URL     | URLBase      | is_active, clicks, Config |
| URLInfo | URL          | url, admin_url                          |

##### 5. models.py


This file describes the content of tables in the database .   Class of  Column, Boolean,Integer, String   from sqlalchemy library are used to define the the table headings. This is similar to create  table command used in SQL 
	

##### 6. database.py

 In this file we define steps to creating database , where it will be stored , how it will be accessed and features of database ( autocommit, auto flush  etc)
 
- Database *URI* is fetched using the   get_settings function from config file . 
- engine is defined to embed this *URI*  using create_engine function of sqlalchemy . 
- sessionmaker class  of sqlalchemy.orm binds this engine to SessionLocal 


##### 7. config.py

fastAPI uses pydantic 

##### 8. .env


#### API Documentation 

 
## GET Read the root

#### Curl

```
curl -X 'GET' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json'
```

#### Request URL

#### Server response

| Code | Details |
| --- | --- |
| 200 | 
##### Response body


```
"Welcome to the URL shortener API of LFW :)"
```

##### Response headers

#### Responses

| Code | Description | Links |
| --- | --- | --- |
| 200 | 
Successful Response

## POST Create URL 


#### Curl

```
curl -X 'POST' \
  'http://127.0.0.1:8000/url' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "target_url": "https://twitter.com"
}'
```

#### Request URL

```
http://127.0.0.1:8000/url
```

#### Server response

| Code | Details             |
| ---- | ------------------- |
| 200  | Successful Response |
|                     |
##### Response body

```
{
  "target_url": "https://twitter.com",
  "is_active": true,
  "clicks": 0,
  "url": "http://127.0.0.1:8000/TqUut",
  "admin_url": "http://127.0.0.1:8000/admin/TqUut_oJsPQExn"
}
```

##### Response headers

```
 content-length: 157  content-type: application/json  date: Fri,09 Dec 2022 17:12:34 GMT  server: uvicorn 
```


 ## GET Forward to Target URL
 
 #### Curl

```
curl -X 'GET' \
  'http://127.0.0.1:8000/http%3A%2F%2F127.0.0.1%3A8000%2FTqUut' \
  -H 'accept: application/json'
```

#### Request URL

```
http://127.0.0.1:8000/http%3A%2F%2F127.0.0.1%3A8000%2FTqUut
```

#### Server response

| Code | Details        | Error |
| ---- | -------------- | ----- |
| 404  | _Undocumented_ | Not Found      |

##### Response body


```
{
  "detail": "Not Found"
}
```

 
#### Responses

| Code | Description         | 
| ---- | ------------------- | 
| 200  | Successful Response | 


```
"string"
```
 

```
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```



 ## GET Administration Info 

#### Curl

```
curl -X 'GET' \
  'http://127.0.0.1:8000/admin/TqUut_oJsPQExn%20' \
  -H 'accept: application/json'
```

#### Request URL

```
http://127.0.0.1:8000/admin/TqUut_oJsPQExn%20
```

#### Server response

| Code | Details |
| ---- | ------- |
| 200  |   Successful Response      | 
##### Response body

```
null
```

##### Response headers
 

#### Responses

| Code | Description | Links |
| ---- | ----------- | ----- |
| 200  | Successful Response            |       |

 

```
{
  "target_url": "string",
  "is_active": true,
  "clicks": 0,
  "url": "string",
  "admin_url": "string"
}
```


 

Validation Error
 
```
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```



 ## DELETE Delete URL

 

#### Curl

```
curl -X 'DELETE' \
  'http://127.0.0.1:8000/admin/TqUut_oJsPQExn' \
  -H 'accept: application/json'
```

#### Request URL

```
http://127.0.0.1:8000/admin/TqUut_oJsPQExn
```

#### Server response

| Code | Details |
| ---- | ------- |
| 200  |         |

##### Response body

 
```
{
  "detail": "Successfully deleted shortened URL for 'https://twitter.com'"
}
```

##### Response headers

 
#### Responses

| Code | Description         |
| ---- | ------------------- |
| 200  | Successful Response |Controls `Accept` header.

```
"string"
```

 

```
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

## PART 2 -  FRONT END WEBPAGE

The target end user needs a simple interface to access the shortening service . This is provided with webpage . The webpage has  signup  and login links. Presently one does not need to login to shorten any number of  url's . 


### Libraries Used

- Flask
- Flask_Sesssion
- werkzeug.security
- requests
- functools

### Front End 

##### - bootstrap  version 5.1.3
##### -  HTML
##### - CSS

### Files

##### 1. app.py

This file defines the Flask app and designs routes to connect with html pages of the web site.  Thge route define the journey of the visitor based on their actions on the web site.  It also pushes the long url  to the API endpoints and listens to render the data received from API to display the  shortened   url on website which is clickable . 

| Function | Purpose                                                                                                                |
| -------- | ---------------------------------------------------------------------------------------------------------------------- |
| shorten  | index page of the website , the first page                                                                             |
| signup   | parses the credentails from Signup page to database for storing the user details for future use                        |
| login    | parses the credentails from login page and checks if user id is present in data base . Initiaises session for the user |
| logout   | logs out the user and return to the index page                                                                         |
| url      | Parse the long URL and send it to shorened URL function from api_helper file                                           |


##### 2. helper.py

File defines a decorator function which ensure that the user is logged in . To be used in future versions to ensure that user logs in before the user gets to shorten an URL to keep track of the past URL .

##### 3. api_helper
 
This file accesses LFW URL SHortner API from which is hosted  www.digitalocean.com platform . The API provides various endpoints at  146.190..110.221    ip address and port 8000.

##### 4. templates

Based on behaviour of user , app.py file directs the flow to the various web pages . The web pages are  as follows :
- layout.html
- index.html
- signup.html
- login.html
- shortened.html

##### 5.Static

This folder contains the image  files, CSS files and favicon

## Future Development

#### 1.User History
#### 2.URL History
#### 3. Analytics
#### 4. Security 
#### 5. Delete Option to User 
