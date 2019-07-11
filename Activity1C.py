import datetime
def pangatlo():
    global date3
    isValid=False
    while not isValid:
        try:
            date3 = datetime.datetime.strptime(raw_input('Input Date&Time (format:MM-DD-YYYY HH:MM): '),"%m-%d-%Y %H:%M")
            isValid=True
            break
        except:
            print "Input Proper Date Format"
pangatlo()
if date3.strftime("%H:%M") >= "17:00":
  new = date3 + datetime.timedelta(hours=8 ) - datetime.timedelta(seconds=86400)
  current = new + datetime.timedelta(days=1)
  print "New Time added 8 Hours"
  print(current.strftime("%m-%d-%Y %H:%M"))
else:
  new = date3 + datetime.timedelta(hours=8)
  print "New Time added 8 Hours"
  print(new.strftime("%m-%d-%Y %H:%M"))
print("\n")
