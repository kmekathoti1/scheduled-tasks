import requests
import os
from twilio.rest import Client





API_KEY=os.environ.get("API_KEY_RAIN")
MY_LAT=10.783600
MY_LONG=79.133598

auth_token = os.environ.get("AUTH_TOKEN")

account_sid = os.environ.get("ACCOUNT_SID")


parameters={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":API_KEY,
    "cnt":4
}
response=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
data=response.json()["list"]

print(data[0]['weather'])
raining=False
for i in data:
    weather_data=i["weather"][0]["id"]
    if weather_data <= 600:
        raining=True
if raining:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body="its going to rain",
        from_=os.environ.get("TWILIO_NUMBER"),
        to=os.environ.get("MY_NUMBER"),
    )
    print(message.status)



