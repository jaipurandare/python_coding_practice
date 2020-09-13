students=input("Enter number of students: ")
i=1
while i<=int(students):
	marks=input("\nEnter marks: ")
	if marks.isnumeric()==True and int(marks)>0 and int(marks)<=100:
		if int(marks)<100 and int(marks)>=80:
     			print('A grade')
		elif int(marks)<80 and int(marks)>=60:
     			print('B grade')
		elif int(marks)<60 and int(marks)>=40:
     			print('C grade')
		else:
     			print('Fail')
	else:
     		print('Invalid input')
	i+=1

