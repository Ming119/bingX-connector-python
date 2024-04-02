import requests

base_url = "https://open-api.bingx.com"


def generate_listen_key(api_key):

    endpoint = "/openApi/user/auth/userDataStream"

    url = base_url + endpoint

    headers = {
        "X-BX-APIKEY": api_key
    }

    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        listen_key = data.get('listenKey')
        return listen_key
    else:
        return "Failed to get listenKey."


def delete_listen_key(listen_key):

    endpoint = "/openApi/user/auth/userDataStream?listenKey=" + listen_key

    url = base_url + endpoint

    response = requests.delete(url)

    if response.status_code == 200:
        return "ListenKey extended successfully."
    else:
        if response.status_code == 204:
            return "Not Content"
        elif response.status_code == 404:
            return "Not Find ListenKey"


def extend_listen_key(listen_key):

    endpoint = "/openApi/user/auth/userDataStream?listenKey=" + listen_key

    url = base_url + endpoint

    response = requests.put(url)

    if response.status_code == 200:
        return "ListenKey Deleted successfully."
    else:
        if response.status_code == 204:
            return "Not Content"
        elif response.status_code == 404:
            return "Not Find ListenKey"
