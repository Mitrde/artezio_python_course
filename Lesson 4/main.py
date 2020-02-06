"""You can check is site alive with it"""
from website_alive.check_response import check_url


print("Enter URL")
URL = input()
if check_url(URL):
    print("{} is available".format(URL))
else:
    print("{} is not available".format(URL))
