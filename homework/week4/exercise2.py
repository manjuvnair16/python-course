from requests import get
from json import dumps

'''
*********************************************************************************
For this section, you may find it helpful to also use this page to help you find the name of the metric you are looking for: https://coronavirus.data.gov.uk/details/download

2a. Use the UK government's COVID API to create a list of daily cases in the UK, with each element in the list representing one day's cases.
*********************************************************************************
'''

#https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation;areaName=england&structure={"date":"date","name":"areaName","newCases":"newCasesByPublishDate"}

ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
AREA_TYPE = "overview"

filters = [
    f"areaType={ AREA_TYPE }"
]

structure = {
    "date": "date",
    "name": "areaName",
    "dailyCases": "newCasesByPublishDate"
}

api_params = {
    "filters": str.join(";", filters),
    "structure": dumps(structure, separators=(",", ":"))
}


response = get(ENDPOINT, params=api_params, timeout=10)

if response.status_code >= 400:
    raise RuntimeError(f'Request failed: { response.text }')

print(response.url)


data = response.json()
daily_cases_for_uk = []
dates_for_uk = []
for item in data['data']:
    daily_cases_for_uk.append(item['dailyCases'])
    dates_for_uk.append(item['date'])

print(len(daily_cases_for_uk), len(dates_for_uk), daily_cases_for_uk[0])



'''
*********************************************************************************
2b. Use list slicing on the above list to create a new list of the number of cases for the last 7 days, and print the 7 day average to the nearest whole number. You may find the inbuilt functions sum() and round() helpful. 
*********************************************************************************
'''

cases_for_last_seven_days = daily_cases_for_uk[:7]
print(cases_for_last_seven_days)
avg = sum(cases_for_last_seven_days)/7
avg = round(avg, 2)
print(avg)



'''
*********************************************************************************
2c. Plot the number of cases for the whole UK on a graph.You can use this code snippet as a reference:    
    import matplotlib.pyplot as plt
    import matplotlib.dates    
    cases = ["2", "3", "2", "4"]
    dates = ["2020-02-17", "2020-02-18", "2020-02-19", "2020-02-20"]
    converted_dates = matplotlib.dates.datestr2num(dates)
    plt.plot_date(converted_dates, cases, '-', color='red')
    plt.ylabel('Daily Cases')
    plt.xlabel('Date')
    plt.show()
*********************************************************************************
'''

import matplotlib.pyplot as plt
import matplotlib.dates  as mdates
cases = daily_cases_for_uk
converted_dates = mdates.datestr2num(dates_for_uk)
plt.plot_date(converted_dates, cases, '-', color='red')
plt.ylabel('Daily Cases')
plt.xlabel('Date')
plt.show()



'''
*********************************************************************************
2d. Plot the number of cases for your local area. 
*********************************************************************************
'''

#https://api.coronavirus.data.gov.uk/v2/data?areaType=utla&areaCode=E09000029&metric=cumCasesByPublishDate&format=json

ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
AREA_TYPE = "utla"
AREA_NAME = "sutton"

filters = [
    f"areaType={ AREA_TYPE }",
    f"areaName={ AREA_NAME }"
]

structure = {
    "date": "date",
    "name": "areaName",
    "dailyCases": "newCasesByPublishDate"
}

api_params = {
    "filters": str.join(";", filters),
    "structure": dumps(structure, separators=(",", ":"))
}


response = get(ENDPOINT, params=api_params, timeout=10)

if response.status_code >= 400:
    raise RuntimeError(f'Request failed: { response.text }')

print(response.url)


data = response.json()
daily_cases_for_local_area = []
dates_for_local_area = []
for item in data['data']:
    daily_cases_for_local_area.append(item['dailyCases'])
    dates_for_local_area.append(item['date'])

print(len(daily_cases_for_local_area), len(dates_for_local_area), daily_cases_for_local_area[0])

cases = daily_cases_for_local_area
converted_dates = mdates.datestr2num(dates_for_local_area)
plt.plot_date(converted_dates, cases, '-', color='red')
plt.ylabel('Daily Cases')
plt.xlabel('Date')
plt.show()



'''
*********************************************************************************
2e. Plot the number of cases for each nation (England, Scotland, Wales, Northern Ireland) on a graph.    hint: areaName for Northern Ireland is "northern%20ireland", " " is represented by "%20"
*********************************************************************************
'''

ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
AREA_TYPE = "nation"
area_name_list = ["england", "scotland", "wales", "northern%20ireland"]
for each_nation in area_name_list:
    AREA_NAME = each_nation

    filters = [
        f"areaType={ AREA_TYPE }",
        f"areaName={ AREA_NAME }"
    ]

    structure = {
        "date": "date",
        "name": "areaName",
        "dailyCases": "newCasesByPublishDate"
    }

    api_params = {
     "filters": str.join(";", filters),
     "structure": dumps(structure, separators=(",", ":"))
    }


    response = get(ENDPOINT, params=api_params, timeout=10)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')

    print(response.url)


    data = response.json()
    daily_cases_for_each_nation = []
    dates_for_each_nation = []
    for item in data['data']:
        daily_cases_for_each_nation.append(item['dailyCases'])
        dates_for_each_nation.append(item['date'])

    print(len(daily_cases_for_each_nation), len(dates_for_each_nation), daily_cases_for_each_nation[0])

    cases = daily_cases_for_each_nation
    converted_dates = mdates.datestr2num(dates_for_each_nation)
    plt.plot_date(converted_dates, cases, '-', color='red')
    plt.ylabel('Daily Cases')
    plt.xlabel('Date')
    plt.show()




'''
*********************************************************************************
2f. Write a csv with the number of daily cases for your local area with columns for dates and cases.
*********************************************************************************
'''
import csv


with open('dailyCasesForLocalArea.csv','w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Number of Daily Cases', 'Date'])
    for daily_case, date in zip(daily_cases_for_local_area, dates_for_local_area):
        csv_writer.writerow([daily_case, date])