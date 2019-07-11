import datetime
def una():
    global first
    isValid=False
    while not isValid:
        date1 = raw_input('Input Date1 (format:MM-DD-YYYY):')
        try:
            first = datetime.datetime.strptime(date1, "%m-%d-%Y")
            isValid=True
            break
        except:
            print "Input Proper Date Format"
def pangalawa():
    global second
    isValid=False
    while not isValid:
        date2 = raw_input('Input Date2 (format:MM-DD-YYYY):')
        try:
            second = datetime.datetime.strptime(date2, "%m-%d-%Y")
            isValid=True
            break
        except:
            print "Input Proper Date Format"
una()
pangalawa()

if first > second:
   diffdays = abs((first - second).days)
   diffyears = diffdays / 365
   diffmonths = diffdays * 0.0328767
   print int(diffmonths),"Month(s) , ",diffdays,"Days(s) , ",int(diffyears),"Year(s)"
else:
   diffdays = abs((second - first).days)
   diffyears = diffdays / 365
   diffmonths = diffdays * 0.0328767
   print int(diffmonths),"Month(s) , ",diffdays,"Days(s) , ",int(diffyears),"Year(s)"
