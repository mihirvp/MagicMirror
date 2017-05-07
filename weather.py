from forecastiopy import *

#troy lat and long
lat = 42.6064
lon = -83.1498

apikey = '48417b85900035a878ea5d28fafd5a79'

fio = ForecastIO.ForecastIO(apikey,
                            units=ForecastIO.ForecastIO.UNITS_US,
                            lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                            latitude = lat, longitude=lon)

#print('Latitude', fio.latitude, 'Longitude', fio.longitude)
#print('Timezone', fio.timezone, 'Offset', fio.offset)
#print(fio.get_url())


currently = FIOCurrently.FIOCurrently(fio)

#icon for weather todaoy
print(currently.icon)

daily = FIODaily.FIODaily(fio)


for day in range(0, 7):
        #low followed by high for each day starting with today
        print(str(daily.get_day(day)['temperatureMin']))
        print(',')
        print(str(daily.get_day(day)['temperatureMax']))
        print(',');

#php parse
# pieces = explode(" ", $output)
# pieces[1] = icon info- clear-day, clear-night, rain, snow, sleet, wind, fog,
#                        cloudy, partly-cloudy-day, or partly-cloudy-night
# pieces[2] = today low
# pieces[3] = today high
# pieces[4] = tomorow low
# .... up to and including pieces[14]
# .... low is odd numbers high is even

