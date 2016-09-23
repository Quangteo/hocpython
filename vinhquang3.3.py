# Exercise 3.3
#
# Viết chương trình loại bỏ phần mở rộng của một tên file bất kỳ.
# Ví dụ:
# input = '....slsslslsls...sls'
# output = '....slsslslsls..'
#
# input = 'maria.ozawa.mp9'
# output = 'maria.ozawa'

#Method

input = '....slsslslsls...sls'
index = 0
for i in range(-1, -len(input), -1):
    if input[i] == '.':
        index = i
print(input[:index])
