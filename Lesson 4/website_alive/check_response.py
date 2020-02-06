"""Module with the function that checks response from site"""
from website_alive.make_request import get_url


def check_url(input_url):
    """Function takes URL and checks response from site"""
    response = get_url(input_url)
    if response.status_code == 200:
        return True
    return False
