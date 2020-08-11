print("Hello world")

a = 10
b = 20
c = a+b
d = 10.5
print(c)
type(d)
print("Value of d" + str(d))
f = int(d)
print("f = " + str(f))
g = "12"
print(int(g)+a)
other = '''She said
hii
how are you '''
other_single_line = 'She said \n \'hii\' \t how are you?'
print(other)
print(other_single_line)
print("hi"*3)
#[h,i]
print(other[0])
print(other[-3])
# slice [start: end: step]
print("3:5 "+other[3:5])
print("3::3 "+other[3::3])
print("7: "+other[7:])
print(":5 "+other[:5])
print(": "+other[:])