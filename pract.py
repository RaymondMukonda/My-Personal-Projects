from datetime import datetime, timedelta
today = datetime.now()
print("today is: "+ str(today))

one_day = timedelta(days=1)
yesterday = today - one_day
print("yesterday was: " + str(yesterday))