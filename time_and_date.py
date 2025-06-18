def time_taker():
   import datetime

   date=datetime.date(2025, 1, 3)
   today=datetime.date.today()

   time=datetime.time(12,30,34)
   now=datetime.datetime.now()

   now=now.strftime("%H:%M:%S--%d/%m/%Y")

   return(now)

print(time_taker())

