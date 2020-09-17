
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] #list

cnt = 0
while cnt < 7:
    print("Day {} of the week is {}".format(cnt+1,weekdays[cnt]))
    cnt +=1

#Slicing patterns
print(weekdays[0:3])
print(weekdays[4:8])
print(weekdays[:3])
print(weekdays[4:])
print(weekdays[2:4])

#reverse list
print("\nReverse list1: {}".format(weekdays[::-1]))
print("Reverse list2: {}".format(weekdays[:2:-1]))

print("\nLength of the list: {}".format(len(weekdays))) #length of the list

weekdays.append("HDay1") #Append holiday to the list
print("Append holiday to the list: {}".format(weekdays))

weekdays.insert(3,"HDay2") #Insert holiday after Wednesday
print("Insert holiday after Wed: ".format(weekdays))

weekdays.remove("HDay1") #Remove holiday at the end of the list
print("Remove holiday from end of the list: {}".format(weekdays))

weekdays.sort() #Sort the list
print("\nSort the list: {}".format(weekdays))

weekdays.reverse() #Reverse the list
print("Reverse the list: {}".format(weekdays))

print("Index of Sunday: {}".format(weekdays.index("Sunday"))) #Index of Sunday

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] #list
newdays = ["Mercury","Venus","Mars"] #create list of new days
print("\nNew days list: "+str(newdays))

weekdays.extend(newdays) #Extend the old list with the days from new list
print("Old list extended: {}".format(weekdays))

newweek = weekdays.copy() #create copy of the list
print("Create copy of the old list: {}".format(newweek))

newweek.insert(6,"HDay1") #add one more day to the copied list
print("One more day added: {}".format(newweek))

#Compare both the lists
cnt=0
matchCnt=0

if len(weekdays)>len(newweek):
    print("\nWeekdays list ({}) is greater than new week list ({})".format(len(weekdays),len(newweek)))
elif len(weekdays)<len(newweek):
    print("\nNew week list ({}) is greater than weekdays list ({})".format(len(newweek),len(weekdays)))
else:
    print("\nWeekdays and new week list has same number of entries {}".format(len(weekdays)))
    
for x in weekdays or newweek:
    if weekdays[cnt]==newweek[cnt]:
        matchCnt+=1
        cnt+=1
    else:
        cnt+=1

if cnt<len(weekdays):
    cnt=len(weekdays)
elif cnt<len(newweek):
    cnt=len(newweek)
mismatchCnt = cnt-matchCnt

print("Number of matches: {}".format(matchCnt))
print("Number of mismatch: {}".format(mismatchCnt))

#pop element from the list
newweek.pop(6) 
print("\nList after element poped: "+str(newweek))

#clear the list
newweek.clear()
print("Clear list: "+str(newweek))

