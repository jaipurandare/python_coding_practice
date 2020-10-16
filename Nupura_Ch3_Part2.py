#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Compare both the lists
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
newweek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','HDay1','Sunday','Mercury','Venus','Mars']
mismatch = []
print(weekdays and newweek)
matchcnt=0
#maxcnt = max(len(weekdays),len(newweek))
print("Max Count {}".format(maxcnt))

if len(weekdays)>len(newweek):
    print("Weekdays list ({}) is greater than new week list ({})".format(len(weekdays),len(newweek)))
elif len(weekdays)<len(newweek):
    print("New week list ({}) is greater than weekdays list ({})".format(len(newweek),len(weekdays)))
else:
    print("Weekdays and new week list has same number of entries {}".format(len(weekdays)))
    
#1st way:Create new mismatch list to display mismatched entries
    cnt=0
while cnt < len(newweek):
    if str(newweek[cnt]) not in weekdays:
        mismatch.append(newweek[cnt])
    cnt+=1
print(mismatch)
    
#2nd way: remove the matched elements from other list 'newweek' 
cnt=0
while cnt < len(weekdays): #(len(weekdays),len(newweek)):
    if str(weekdays[cnt]) in newweek:
            print(weekdays[cnt])
            element=weekdays[cnt]
            newweek.remove(element)
    else:
            print("Not present")
    cnt+=1
print(newweek)


#Same assignment using For loop

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Random"]
newweek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','HDay1','Sunday','Mercury','Venus','Mars']

match=[]
mismatch=[]

for day in weekdays:
    if day in newweek:
        match.append(day)
        newweek.remove(day)
    else:
        mismatch.append(day)
print(match)

for day in newweek:
        mismatch.insert(0,day)
        
print(mismatch)