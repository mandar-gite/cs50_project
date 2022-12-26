## Example Usage

```
uvicorn shortener_app.main:app --reload
INFO:     Will watch for changes in these directories: ['/home/mandar/Desktop/SHORTNER FOR LFW/lfw_url']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [322468] using statreload
Loading settings for: Development
INFO:     Started server process [322470]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

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

| Code | Description |
| --- | --- |
| 200 | Successful Response|


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

| Code | Details |
| --- | --- |
| 200 | 
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



#### Responses

| Code | Description         | 
| ---- | ------------------- |
| 200  | Successful Response |


 
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

