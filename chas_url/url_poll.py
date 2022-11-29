import requests


def url_poll(valid_url: str) -> dict:
    response = requests.options(valid_url)
    available_methods = response.headers.get('Allow')
    poll_dict = {}
    if available_methods is not None:
        available_methods = available_methods.split(', ')
    else:
        available_methods = ['GET', 'OPTIONS', 'HEAD', 'POST', 'PUT',
                             'PATCH', 'DELETE', 'CONNECT', 'TRACE']
    for url_method in available_methods:
        r = requests.request(url_method, valid_url)
        if r.status_code != 405:
            poll_dict[url_method] = r.status_code

    return poll_dict
