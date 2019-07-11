def check():
  global listuna
  isValid=False
  while not isValid:
    try:
      listuna = int(input("Input Length of List: "))
      isValid=True
      break
    except:
      print "Input Integer Only"
def checking(lst) :
    for i in range(len(lst)) :
        if lst[i].isdigit() != True :
            return False
    return True
check()
list1 = []
for i in range (0, listuna):
  lista = raw_input("Input value for list1: ")
  list1.append(lista)
print "List 1: ",list1

for i in range(len(list1)) :
  if checking(list1[i]) :
   withstr = False
  else:
   withstr = True
   break

if withstr == False:
  Largest = max(list1)
  Smallest = min(list1)
  SumL = sum(map(int, list1))
  print "The Sum of the List is: ", SumL
  print "The Largest value in the list is: ", Largest
  print "The Smallest value in the list is: ", Smallest
else:
  Largest = max(list1)
  Smallest = min(list1)
  print "The Sum of the List is: Cannot be sum because of string"
  print "The Largest value in the list is: ", Largest
  print "The Smallest value in the list is: ", Smallest
print("\n")
check()
list2 = []
for i in range (0, listuna):
  listb = raw_input("Input value for list: ")
  list2.append(listb)
print "List 1: ",list1
print "List 2: ",list2

for g, c in map(None, list1, list2):
    print "List 1:",g," ","List 2:",c
print ("\n")

print ("Convert list into list of dictionaries")
a = 0
dictio1={}
dictio2={}
for i in range(len(list1)):
    a=i+1
    dictio1[a]=list1[i]
for i in range(len(list2)):
    a=i+1
    dictio2[a]=list2[i]
print "List 1 into Dictionaries: ", dictio1
print "List 2 into Dictionaries: ", dictio2

for g, c in map(None, dictio1, dictio2):
   print "Dictionaries 1 Value: ",g," ", "Dictionaries 2 Value: ",c
print("\n")
