VALID_FROM=['6','D','X']
VALID_TO=['D','X']
HEADER_RECORD_START='HDR'
TRAILER_RECORD_START='TLR'
detailcount=1

def file_validation(file):
    errorlist=[]
    errorlist.append(file_validation_header(file[0]))
    errorlist.append(file_validation_detail(file[1]))
    errorlist.append(file_validation_trailer(file[2],file[0][1]))
    return errorlist

def file_validation_header(header):
    error_header=[]
    if header[0]!= HEADER_RECORD_START:
        error_header.append('Incorrect header record name')
    if not header[1].isnumeric():
        error_header.append('Incorrect file sequence number in header')
    if header[2] not in VALID_FROM:
        error_header.append('Incorrect From code in header')
    if not header[3].isalpha():
        error_header.append('Incorrect From value in header')
    if header[4] not in VALID_TO:
        error_header.append('Incorrect To code in header')
    if not header[5].isalpha():
        error_header.append('Incorrect To value in header')
    return error_header

def file_validation_detail(detail):
    error_detail=[]
    if not detail[0].isnumeric():
        error_detail.append('Incorrect detail record number sequence')
    if not detail[1].isalpha():
        error_detail.append('Incorrect detail name')
    if not detail[2].isnumeric():
        error_detail.append('Incorrect detail mobile number')
    return error_detail

def file_validation_trailer(trailer,header_seq_no):
    error_trailer=[]
    if trailer[0]!=TRAILER_RECORD_START:
        error_trailer.append('Incorrect trailer record name')
    if not trailer[1].isnumeric() or trailer[1]!=header_seq_no:
        error_trailer.append('Incorrect file sequence number in trailer')
    if not trailer[2].isnumeric() or int(trailer[2])!=detailcount:
        error_trailer.append('Incorrect detail records number in trailer')
    return error_trailer
