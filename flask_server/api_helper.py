import requests
hosted_at = "http://127.0.0.1:8000"

def shorten_url(target_url: str):
    """ function to call lfw_url API

    :param target_url:
    :return: dictionary created from response json
            {
              "target_url": "string",
              "is_active": true,
              "clicks": 0,
              "url": "string",
              "admin_url": "string"
            }
    """
    payload = {"target_url": target_url}
    response_create_url = requests.post("http://127.0.0.1:8000" + "/url", json=payload)
    json_create_url = response_create_url.json()

    return json_create_url
