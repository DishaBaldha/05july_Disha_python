a = input('Enter the string :')
b = a[-3:]
if(a[-3:] == 'ing'):
    b = a +'ly'
elif(len(b) <3):
    print(b)
else:
    b =a+'ing'
print(b)


