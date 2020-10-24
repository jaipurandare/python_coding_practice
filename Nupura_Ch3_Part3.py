
print('Enter file header and trailer in comma separated format\n')
header=input('Enter Header (6 fields): ')
trailer=input('Enter Trailer (3 fields): ')
detail=input('Enter count of Detail records: ')

#Header validations
hdr=header.split(',')
validFrom=['6','D','X']
validTo=['D','X']
if hdr[0]!='ZHV':
    print('Incorrect header record name')
if hdr[1].isalnum()==True:
    print('Incorrect file sequence number in header')
if hdr[2] not in validFrom:
    print('Incorrect From code in header')
if hdr[3].isalnum()==True:
    print('Incorrect From value in header')
if hdr[4] not in validTo:
    print('Incorrect To code in header')
if hdr[5].isalnum()==True:
    print('Incorrect To value in header')

#Trailer validations
tlr=trailer.split(',')
if tlr[0]!='ZPT':
    print('Incorrect trailer record name')
if tlr[1].isalnum()==True or tlr[1]!=hdr[1]:
    print('Incorrect file sequence number in trailer')
if tlr[2]!=detail or detail.isalnum()==True:
    print('Incorrect detail records number in trailer')

if detail.isalnum()==True:
    print('Incorrect Detail number')

