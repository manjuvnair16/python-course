import requests


'''
*********************************************************************************
1a. Sign up for an API key for a news site
    You can test that your api key works using this snippet: 
    query_params = {'api-key': 'your-api-key-here'} 
    response = requests.get("https://content.guardianapis.com/search", params=query_params)
    print(response.status_code)

*********************************************************************************
'''

query_params = {'api-key': '0b5c1be8-9695-4aa9-be95-d52483109ec9'} 
response = requests.get("https://content.guardianapis.com/search", params=query_params)
print(response.status_code)



'''
*********************************************************************************
1b. Find a url to any article about clouds.
*********************************************************************************
'''

#https://content.guardianapis.com/search?q=clouds&api-key=test
query_params = {'api-key': '0b5c1be8-9695-4aa9-be95-d52483109ec9',
                'q'      : 'clouds'
               } 
response = requests.get("https://content.guardianapis.com/search", params=query_params)
url = response.json()['response']['results'][3]['webUrl']
print(url)



'''
*********************************************************************************
1c. Find a url to any article 5 years or older about bitcoin. 
*********************************************************************************
'''

#https://content.guardianapis.com/search?to-date=2016-01-01&q=bitcoin&api-key=test
query_params = {'api-key': '0b5c1be8-9695-4aa9-be95-d52483109ec9',
                'to-date': '2016-01-01',
                'q'      : 'bitcoin'
               } 
response = requests.get("https://content.guardianapis.com/search", params=query_params)
url = response.json()['response']['results'][0]['webUrl']
print(url)



'''
*********************************************************************************
1d. Count the number of articles written this year about 3D printing (hint: use the tag "technology/3d-printing" for The Guardian). 
*********************************************************************************
'''

#https://content.guardianapis.com/search?to-date=2016-01-01&q=bitcoin&api-key=test
query_params = {'api-key': '0b5c1be8-9695-4aa9-be95-d52483109ec9',
                'from-date': '2021-01-01',
                'q'      : '3d printing'
               } 
response = requests.get("https://content.guardianapis.com/search", params=query_params)
count = response.json()['response']['total']
print(count)



'''
*********************************************************************************
1e. Find the first article written in the science section about the landing of the Mars Rover Perseverance. The landing was on 18 Feb 2021. Don't try too hard, the search function isn't the best.
*********************************************************************************
'''

#https://content.guardianapis.com/search?section=science&from-date=2021-02-18&to-date=2021-02-18&order-by=oldest&q=mars&api-key=test

query_params = {'api-key': '0b5c1be8-9695-4aa9-be95-d52483109ec9',
                'from-date': '2021-02-18',
                'to-date': '2021-02-18',
                'q'      : 'mars',
                'order-by': 'oldest',
                'section' : 'science'
               } 
response = requests.get("https://content.guardianapis.com/search", params=query_params)
url = response.json()['response']['results'][0]['webUrl']
print(url)
