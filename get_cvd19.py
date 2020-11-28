import requests
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument('-c', '--country', action='store', dest='country', help='Country', required=True)
parser.add_argument('-d', '--date', action='store', dest='date', help='DD-MM-YYYY', default=datetime.now().strftime('%d-%m-%Y'))

args = parser.parse_args()

# args.date = datetime.now().strftime('%m-%d-%Y')
# args.date = mDate.strftime('%m-%d-%Y')

print(args.date)

# url = "https://covid1910.p.rapidapi.com/data/confirmed/country/us&canada/date/03-02-2020&04-02-2020"

url = "https://covid1910.p.rapidapi.com/data/confirmed/country/" + args.country  + "/date/" + args.date

headers = {
    'x-rapidapi-key': "d3cd145a50mshef4eb7b5b1a13b5p198ed9jsn88bb49fd1ebc",
    'x-rapidapi-host': "covid1910.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
