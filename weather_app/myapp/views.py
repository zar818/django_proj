from django.shortcuts import render
import urllib.request  
import json
# Create your views here.

def index(request):
    return render(request,'misc/home.html')
def check_weather(request):
    if request.method=='POST':
        city=request.POST
        response=urllib.request.urlopen('').read()
        json_data=json.loads(response)
        data={
            'country_code':str(json_data['sys']['country']),
            'coordinate':str(json_data['coordinate'])
        }
    else:
        city=''
        data=()
    return render(request,'weather.html',{'city':city,'data':data})