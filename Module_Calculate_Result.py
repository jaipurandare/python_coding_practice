import sys
import Module_Calculate

calculateDict = {'add':Module_Calculate.add,
                 'subtract':Module_Calculate.subtract,
                 'multiply':Module_Calculate.multiply,
                 'divide':Module_Calculate.divide}
calculateFunction=calculateDict[sys.argv[1]]
answer=calculateFunction(int(sys.argv[2]),int(sys.argv[3]))
print('Answer:{}'.format(answer))

#if sys.argv[1]=='add':
#	answer=Module_Calculate.add(int(sys.argv[2]),int(sys.argv[3]))
#	print('Addition:{}'.format(answer))
#elif sys.argv[1]=='subtract':
#	answer=Module_Calculate.subtract(int(sys.argv[2]),int(sys.argv[3]))
#	print('Subtraction:{}'.format(answer))
#elif sys.argv[1]=='multiply':
#	answer=Module_Calculate.multiply(int(sys.argv[2]),int(sys.argv[3]))
#	print('Multiplication:{}'.format(answer))
#elif sys.argv[1]=='divide':
#	answer=Module_Calculate.divide(int(sys.argv[2]),int(sys.argv[3]))
#	print('Division:{}'.format(answer))
