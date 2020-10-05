#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Compare both the lists
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
newweek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','HDay1','Sunday','Mercury','Venus','Mars']
print(weekdays and newweek)
cnt=0
matchcnt=0
maxcnt = max(len(weekdays),len(newweek))
print("Max Count {}".format(maxcnt))
i=1

if len(weekdays)>len(newweek):
    print("Weekdays list ({}) is greater than new week list ({})".format(len(weekdays),len(newweek)))
elif len(weekdays)<len(newweek):
    print("New week list ({}) is greater than weekdays list ({})".format(len(newweek),len(weekdays)))
else:
    print("Weekdays and new week list has same number of entries {}".format(len(weekdays)))

while cnt < maxcnt: #(len(weekdays),len(newweek)):
    if str(weekdays[cnt]) in newweek:
            print(weekdays[cnt])
            print(i)
            i+=1
    else:
            print("Not present")
            i+=1
    cnt+=1
    
#       if daycnt==x:
 #           matchCnt+=1
  #          i+=1
   #         print(matchCnt) 
    #        continue
       #if weekdays[cnt]==Null:
     #   break

mismatchCnt = cnt-matchCnt

print("Number of matches: {}".format(matchCnt))
print("Number of mismatch: {}".format(mismatchCnt))


# In[ ]:




