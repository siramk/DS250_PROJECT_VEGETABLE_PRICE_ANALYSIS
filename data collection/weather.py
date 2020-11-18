import pandas as pd 
import requests
import json

def get_response(start_date, end_date):
	api_key = "f972f525c49443af899142826200111"
	url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=" + api_key + "&q=Surat&format=json&tp=24&date=" + start_date + "&enddate=" + end_date
	res = json.loads(requests.get(url).content)
	return res

def insert_dict(weather_data):
	for data in weather_data:
		weather['date'].append(data['date'])
		weather['sunHour'].append(data['sunHour'])
		weather['uvIndex'].append(data['uvIndex'])
		weather['tempC'].append(data['hourly'][0]['FeelsLikeC'])
		weather['windspeedKmph'].append(data['hourly'][0]['windspeedKmph'])
		weather['winddirDegree'].append(data['hourly'][0]['winddirDegree'])
		weather['winddir16Point'].append(data['hourly'][0]['winddir16Point'])
		weather['precipMM'].append(data['hourly'][0]['precipMM'])
		weather['humidity'].append(data['hourly'][0]['humidity'])
		weather['visibility'].append(data['hourly'][0]['visibility'])
		weather['pressure'].append(data['hourly'][0]['pressure'])
		weather['cloudcover'].append(data['hourly'][0]['cloudcover'])
		weather['HeatIndexC'].append(data['hourly'][0]['HeatIndexC'])
		weather['DewPointC'].append(data['hourly'][0]['DewPointC'])
		weather['WindChillC'].append(data['hourly'][0]['WindChillC'])
		weather['WindGustKmph'].append(data['hourly'][0]['WindGustKmph'])

start_year = 2010
end_year = 2020
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

weather = {
	'date': [],
	'sunHour': [],
	'uvIndex': [],
	'tempC': [],
	'windspeedKmph': [],
	'winddirDegree': [],
	'winddir16Point': [],
	'precipMM': [],
	'humidity': [],
	'visibility': [],
	'pressure': [],
	'cloudcover': [],
	'HeatIndexC': [],
	'DewPointC': [],
	'WindChillC': [],
	'WindGustKmph': []
}

for year in range(start_year, end_year+1):
	for i in range(12):
		if year == 2020 and i >= 9 :
			break
		month = months[i]
		days = days_month[i]
		if year % 4 == 0 and days == 28:
			days = 29
		start_date = str(year) + '-' + month + '-01'
		end_date = str(year) + '-' + month + '-' + str(days)
		print(end_date)
		response = get_response(start_date, end_date)
		insert_dict(response["data"]["weather"])


df = pd.DataFrame(weather)
df.to_csv('weather.csv', index=False)