from forecastiopy import *

#troy lat and long
lat = 42.6064
lon = -83.1498

apikey = '48417b85900035a878ea5d28fafd5a79'

fio = ForecastIO.ForecastIO(apikey,
                            units=ForecastIO.ForecastIO.UNITS_US,
                            lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                            latitude = lat, longitude=lon)

currently = FIOCurrently.FIOCurrently(fio)

#icon for weather todaoy
print(currently.icon)
print(',')
print(int(currently.temperature))
print(',')

daily = FIODaily.FIODaily(fio)


for day in range(0, 7):
        #low followed by high for each day starting with today
        print(str(int(daily.get_day(day)['temperatureMin'])))
        print(str(int(daily.get_day(day)['temperatureMax'])))
        print(',')

#icon info- clear-day, clear-night, rain, snow, sleet, wind, fog,
#                        cloudy, partly-cloudy-day, or partly-cloudy-night
