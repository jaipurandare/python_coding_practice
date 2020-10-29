#First method

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

#Second method

print('Enter file header and trailer in comma separated format\n')
header=input('Enter Header (6 fields): ')
trailer=input('Enter Trailer (3 fields): ')
detail=input('Enter count of Detail records: ')
err=[[],[],[]]
HEADER_RECORD_START='HDR'
TRAILER_RECORD_START='TLR'

#Header validations
hdr=header.split(',')
validFrom=['6','D','X']
validTo=['D','X']

if hdr[0]!= HEADER_RECORD_START:
    err[0].append('Incorrect header record name')
if not hdr[1].isnumeric():
    err[0].append('Incorrect file sequence number in header')
if hdr[2] not in validFrom:
    err[0].append('Incorrect From code in header')
if not hdr[3].isalpha():
    err[0].append('Incorrect From value in header')
if hdr[4] not in validTo:
    err[0].append('Incorrect To code in header')
if not hdr[5].isalpha():
    err[0].append('Incorrect To value in header')

#Trailer validations
tlr=trailer.split(',')
if tlr[0]!=TRAILER_RECORD_START:
    err[1].append('Incorrect trailer record name')
if not tlr[1].isnumeric() or tlr[1]!=hdr[1]:
    err[1].append('Incorrect file sequence number in trailer')
if tlr[2]!=detail or not detail.isnumeric():
    err[1].append('Incorrect detail records number in trailer')

if not detail.isnumeric():
    err[2].append('Incorrect Detail number')
    
print(err)

#Trail - List inside list
hdrerr='header error'
tlrerr='trailer error'
dtlerr='detail error'
totalerr =[hdrerr,tlrerr,dtlerr]
totalerr