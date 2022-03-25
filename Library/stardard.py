# https://www.programiz.com/python-programming/methods/string/isnumeric
data_string = '1'

# 문자
print('is alphabet? :', data_string.isalpha())
# 숫자
print('is number? :', data_string.isalnum())
# 슷자
print('is numeric? :', data_string.isnumeric())
# 10진수
print('is decimal? :', data_string.isdecimal())
# 소문자
print('is lower? :', data_string.islower())
# 대문자
print('is upper? :', data_string.isupper())


data_list = ['abcd', 'efgh']
reverse_data_list = [data_list[::-1] for data_list in data_list]
reverse_data_list.reverse()
print('reverse datat list :', reverse_data_list)
