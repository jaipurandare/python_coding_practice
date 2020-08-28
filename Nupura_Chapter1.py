#Part1
mins=60
secs=60
seconds_per_hour=mins * secs
print ("Seconds per hour: "+ str(seconds_per_hour))

#Part2
seconds_per_day=seconds_per_hour * 24
print ("Seconds per day: "+ str(seconds_per_day))

#Part3
Float_Div1=seconds_per_day/seconds_per_hour
Float_Div2=seconds_per_day//seconds_per_hour
print("Floating point division: " + str(Float_Div1))
print("Integer division: " + str(Float_Div2))

print ("There are {1} seconds per hour and {0} seconds per day ".format(seconds_per_day,seconds_per_hour))

#Part4:
Person='nupura prakash mukadam'
Email= 'nupura@gmail.com'
Address='''Tulshibaugwale Colony
Sahakarnagar no 2
Pune-Maharashtra Pincode 411009'''

print('\n'+'Name in array: '+ str(Person.split(' ')))
print ('Full name: ' + Person.title())
print('Name Initials: '+Person[0].title()+'.'+Person[7].title()+'.'+Person[15].title())
print('\n'+'Address comma separated: ' + Address.replace('\n',','))
Addr_Array=Address.splitlines()
print('\n'+'Address Line 1: '+Addr_Array[0]+'\n'+'Address Line 2: '+Addr_Array[1]+'\n'+'City-State-Pin code: '+Addr_Array[2])
print('Number of characters: '+ str(len(Address)))

#Part5:
FirstName='Nupura'
LastName='Mukadam'
print('\nFull name(from diff strings): {} {}'.format(FirstName,LastName))

AddLine1='Amardhan Society'
AddLine2='Sahkarng no 2'
City='Pune'
State='Maharshtra'
Pincode='411009'
print('Address(from diff strings):\n{}\n{}\n{} {} {}\n'.format(AddLine1,AddLine2,City,State,Pincode))

#Email validation:
if len(Email)<=20 and Email.count('@')==1 and Email.count('.')==1 and Email.isspace()==False:
	print('Email validation: Valid email address: '+Email)
else:	
	print('Email validation: Invalid email address: '+Email)
