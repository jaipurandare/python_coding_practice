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

#Part6:
#Email validation:
Email= 'nupura@gmail.com'
x=Email.partition('@')
y=x[2].partition('.')

if len(Email)<=20 and Email.count('@')==1 and Email.count('.')==1 and Email.isspace()==False and x[1]=='@' and y[1]=='.' and x[0]!='' and y[0]!='' and y[2]!='':
	print('Email validation: Valid email address: '+Email)
else:	
	print('Email validation: Invalid email address: '+Email)

print ('Upper letters: '+FirstName.upper())
print ('Lower letters: '+FirstName.lower())

text='Good Morning! How are you?'
print ('Find command: Location of "are" in the sentence: "'+ text+'" is -->'+ str(text.find('are')))

text1='     apple    '
print ('Strip command: Do you like '+text1.strip()+' or banana?')
