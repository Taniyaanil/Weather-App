from .models import weatherData
from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 


def index(request): 
	if request.method == 'POST': 
		city = request.POST['city'] 
		''' api key might be expired use your own api_key 
			place api_key in place of appid ="your_api_key_here " '''

		# source contain JSON data from API 

		source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=ff244314644bb90897a1d8155efb8a1a').read() 

		# converting JSON data to a dictionary 
	
		list_of_data = json.loads(source)
		print(list_of_data) 
	

		# data for variable list_of_data 
		data = {
			'bdata': weatherData.objects.all().order_by('-timestamp'),
			"city":city,
			"country_code": str(list_of_data['sys']['country']), 
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']), 
			"temp": str(list_of_data['main']['temp']) + 'k', 
			"pressure": str(list_of_data['main']['pressure']), 
			"humidity": str(list_of_data['main']['humidity']), 
		} 
		wdata = weatherData()
		wdata.city = city
		wdata.country_code = str(list_of_data['sys']['country'])
		wdata.coord = str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat'])
		wdata.temp = str(list_of_data['main']['temp']) + 'k'
		wdata.pressure = str(list_of_data['main']['pressure'])
		wdata.humidity =  str(list_of_data['main']['humidity'])
		wdata.save()

		
		
		print(data) 
	else: 
		data ={} 
	return render(request, "main/index.html", data) 
