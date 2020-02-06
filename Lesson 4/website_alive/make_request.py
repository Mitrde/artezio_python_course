"""Module with the function that checks response from site"""
import requests


def get_url(input_url):
    """Function makes a request to site """
    try:
        response = requests.get(input_url)
    except:
        print("Wrong URL!")
        return None
    return response
