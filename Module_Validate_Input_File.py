#Method 1:
#import Module_Input_File_Validations as ifv
#file=[['HDR','1','6','ABC','A','EAS'], ['A','Name','123123'], ['TTT','1','1']]
#result=ifv.file_validation(file)
#print(result)

#Method 2
import Module_Input_File_Validations as ifv
with open('Input_Text_File.txt') as itf:
    file_content=itf.read()

file_list=file_content.splitlines()
header=file_list[0].split(',')
details=file_list[1].split(',')
trailer=file_list[2].split(',')
file=[header,details,trailer]

result=ifv.file_validation(file)
print(result)