s = input("enter the string :")

my_list = s.split()

max_len = 0
for i in my_list:
    if len(i) > max_len:
        max_len = len(i)

print(max_len)