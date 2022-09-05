mobile=['samsung','redmi','oneplus']

file=open('f1.txt','w')
for items in mobile:
    file.writelines([items])

file.close()