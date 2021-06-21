import requests
from datetime import datetime
from datetime import timedelta


'''
******************************************
3a. Use the NASA APOD API (https://api.nasa.gov/) to get the url for today's image of the day
******************************************
'''
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
image_data = response.json()
#print(image_data)
print(f"URL of the APOD image: '{image_data['url']}' ")


'''
******************************************
3b. Use the NASA APOD API to get the url for yesterday's image of the day. (See the docs to
figure out how to provide a date)
Extension: 
Use the datetime module's functions strftime() to create a string that will always be the previous day's date and 
use this string in your API call.
******************************************
'''

'''
#Method 1 to state the api endpoint - specify the url with the parameters in a single string
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2021-06-20")
'''

'''
#Method 2 to state the api endpoint - specify the url separately, parameters in a separate string and concatenate them together
api = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
date = '&' + 'date=2021-06-20'
response = requests.get(api + date)
'''

'''
#Method 3 to state the api endpoint - specify parameters as a dictionary and pass them as a value to the params attribute
query_params = {'api_key': "DEMO_KEY", 'date': '2021-06-20'}
response = requests.get("https://api.nasa.gov/planetary/apod?", params = query_params)
'''


yesterday = datetime.now() - timedelta(days=1)
yesterday_date = yesterday.strftime("%Y-%m-%d")
query_params = {'api_key': "DEMO_KEY", 'date': yesterday_date}
response = requests.get("https://api.nasa.gov/planetary/apod?", params = query_params)

image_data = response.json()
#print(image_data)
print(f"URL of the APOD image: '{image_data['url']}' ")