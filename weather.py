from forecastiopy import *

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


#currently = FIOCurrently.FIOCurrently(fio)
#print('Currently')
#for item in currently.get().keys():
#    print(item + ' : ' + unicode(currently.get()[item]))
# Or access attributes directly
#print(currently.temperature)


#print( )
#print( )


daily = FIODaily.FIODaily(fio)
print('Daily')
print('Summary:', daily.summary)
print('Icon:', daily.icon)

for day in range(0, daily.days()):
        print('Day ' + str(day))
        print('temperatureMin' + ' : ' + str(daily.get_day(day)['temperatureMin']))
        print('temperatureMax' + ' : ' + str(daily.get_day(day)['temperatureMax']))
