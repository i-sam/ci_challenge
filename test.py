import sys
import requests

def test(URL):
    response = requests.get(URL)
    print('%s' % response.status_code)
    return

if __name__ == "__main__":
    test(sys.argv[1])
