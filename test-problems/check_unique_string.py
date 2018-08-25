my_str = input('Please enter the input string')
my_dict = {}
flag = 0
for x in my_str:
    print(x)
    if x not in my_dict:
        my_dict[x] = 1
    else:
        print('String has characters that repeat')
        flag = 1
        break

if flag == 0:
    print('String as unique characters')