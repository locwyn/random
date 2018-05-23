#!/usr/bin/env python
import forecastio
import time
import datetime

"""
file structure:
icon,sunriseTime,sunsetTime,moonPhase,precipIntensity,precipType,temperatureMin,temperatureMax,dewPoint,humidity,windSpeed,windBearing,visibility,cloudCover,pressure
"""

def buildRow(pastTime):
    api_key = "1c6c1c1116e7bd35ab79fadecb54dd25"
    lat = 39.844216
    lng = -89.539542
    darkSkyRow = []
    forecast = forecastio.load_forecast(api_key, lat, lng, time=pastTime)
    byDay = forecast.daily()
    for dailyData in byDay.data:
        dsIcon = str(dailyData.icon)
        dsSunriseTime = str(dailyData.sunriseTime)
        dsSunsetTime = str(dailyData.sunsetTime)
        dsMoonPhase = str(dailyData.moonPhase)
        dsPrecipIntensity = str(dailyData.precipIntensity)
        try:
            dsPrecipType = str(dailyData.precipType)
        except:
            dsPrecipType = "none"
        dsTempMin = str(dailyData.temperatureMin)
        dsTimeMax = str(dailyData.temperatureMax)
        dsDewPoint = str(dailyData.dewPoint)
        dsHumidity = str(dailyData.humidity)
        dsWindSpeed = str(dailyData.windSpeed)
        dsWindBearing = str(dailyData.windBearing)
        dsVisibility = str(dailyData.visibility)
        try:
            dsCloudCover = str(dailyData.cloudCover)
        except:
            dsCloudCover = str(0.0)
        dsPressure = str(dailyData.pressure)
    darkSkyRow.extend([dsIcon, dsSunriseTime, dsSunsetTime, dsMoonPhase, dsPrecipIntensity])
    darkSkyRow.extend([dsPrecipType, dsTempMin, dsTimeMax, dsDewPoint, dsHumidity])
    darkSkyRow.extend([dsWindSpeed, dsWindBearing, dsVisibility, dsCloudCover, dsPressure])
    return darkSkyRow

def writeRow(pullDate):
    row = buildRow(pullDate)
    delimiter = ","
    fileName = "darkSkyHistory1980.txt"
    utcTime = time.mktime(pullDate.timetuple())
    with open(fileName, 'a') as outFile:
        outFile.write(str(utcTime) + "," + delimiter.join(row) + "\n")

#dtJulian = datetime.datetime.strptime("2017-1", "%Y-%j")
#currentTime = datetime.datetime.now()
#pastTime = currentTime - datetime.timedelta(days=1)
#testing forecastio wrapper for darksky api
for i in range(1, 367):
#    pastTime = currentTime - datetime.timedelta(days=i)
    pastTime = datetime.datetime.strptime("1980-" + str(i), "%Y-%j")
    writeRow(pastTime)
#    forecast = forecastio.load_forecast(api_key, lat, lng, time=pastTime)
#    byHour = forecast.hourly()
#    print byHour.summary
#    print byHour.icon
#    byDay = forecast.daily()
#    print byDay.summary
#    for dailyData in byDay.data:
#        print "High Temperature = " + str(dailyData.temperatureMax)
#        print "Low Temperature = " + str(dailyData.temperatureMin)
#        print "Cloud Cover = " + str(dailyData.cloudCover)
#        print "Humidity = " + str(dailyData.humidity)
#        print "Moon Phase = " + str(dailyData.moonPhase)
#        print "Precipitation Intensity = " + str(dailyData.precipIntensity)
#        print "Precipitation Max Intensity = " + str(dailyData.precipIntensityMax)
#        print "Pressure = " + str(dailyData.pressure)
#        print "Moon Phase = " + str(dailyData.moonPhase)
#        print "Sunrise Time = " + str(dailyData.sunriseTime)
#        print "Sunset Time = " + str(dailyData.sunsetTime)


"""
#test loop to pull historical data from dark sky api
for i in range(1, 367):
    d = "2015-" + str(i)
    print time.mktime(time.strptime(d, "%Y-%j"))
"""
