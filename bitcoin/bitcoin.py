import sys
import requests

n=0.0

try:
    n=float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except TypeError:
    sys.exit("Command-line argument is not a number")
else:
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.RequestException:
        sys.exit("No connection")
    else:
        try:
            response = r.json()
        except requests.exceptions.JSONDecodeError:
            sys.exit("No connection")
        else:
            print(f"${format(float(response['bpi']['USD']['rate'].replace(',',''))*n,',')}")






