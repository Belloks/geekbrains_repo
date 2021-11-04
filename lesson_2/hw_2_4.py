input_str = 'мама мыла раму, а папа престидижитировал'
list_str = input_str.split()
print(list_str)
for ind, el in enumerate(list_str, 1):
    el = (el, el[0:10])[len(el) > 10]
    print(ind, el)