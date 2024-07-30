#!/usr/bin/python3
""" script that takes in a URL, \
        sends a request to the URL and displays\
        the body of the response (decoded in utf-8)."""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
<<<<<<< HEAD
        pass
=======
        pass
>>>>>>> 0e89e1f2194e0fe4a117b83e6eccc52881dd93a1
