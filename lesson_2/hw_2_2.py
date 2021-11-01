output_list = []
input_list = ['a', '1', 'b', '2', 'c', '3', 'd']

input_list_len = len(input_list)
for i in range(0, input_list_len, 2):
    if i < input_list_len - 1:
        next_index = i + 1
        output_list.insert(i, input_list[next_index])
        output_list.insert(next_index, input_list[i])
    else:
        output_list.append(input_list[-1])
print(output_list)