test1='This is a test of the emergency text system'

test_file=open('Files_Test_Text.txt','w')
test_file.write(test1)
test_file.close()

test_file=open('Files_Test_Text.txt','r')
test2=test_file.read()
test_file.close()

print('Test1:'+test1)
print('Test2:'+test2)
if test1==test2:
    print('Both strings are same')
else:
    print('Both strings are different')
############################################

#book_csv=open('Module_Books_CSV.csv','w')
#book_csv.write(test1)
#book_csv.close()

#book_csv=open('Module_Books_CSV.csv','r')
#print('Books csv: '+book_csv.read())
#book_csv.close()
