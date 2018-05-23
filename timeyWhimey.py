
import time
import datetime

#struct = time.localtime()
#dt = datetime.fromtimestamp(mktime(struct))
#print dt

"""
ts = time.time()
dft = datetime.datetime.fromtimestamp(ts)
print dft

today = datetime.datetime.today()
print today
print today - datetime.timedelta(days=1)

strpToday = time.strptime("2017-02-10 11:31:37", "%Y-%m-%d %H:%M:%S")
print strpToday
print time.mktime(strpToday)
"""

dtJulian = datetime.datetime.strptime("2017-1", "%Y-%j")
print dtJulian

utcTime = time.mktime(dtJulian.timetuple())
print utcTime
#strpJulian = time.strptime("2017-1", "%Y-%j")
#print strpJulian
"""
print time.mktime(strpJulian)

for i in range(1, 367):
    d = "2015-" + str(i)
    print time.mktime(time.strptime(d, "%Y-%j"))
"""


