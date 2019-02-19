# MT16121
# Ankit Sharma

input_string = input("Enter the string ")
input_pattern = input("Enter the pattern ")

input_string_list = list(input_string)
input_pattern_list = list(input_pattern)

string_index_iterator = 0
temp_iterator = 0
temp_offset = 0
print_check = 0
offset_list = []

# Code to perform naive string matching
if len(input_pattern_list) > len(input_string_list):
    print("Pattern length is greater than the string length !")
else:
    while string_index_iterator != len(input_string_list):
        flag = 0
        temp_iterator = string_index_iterator
        for pattern_index_iterator in range(0, len(input_pattern_list)):
            if pattern_index_iterator == 0:
                temp_offset = temp_iterator

            if input_string_list[temp_iterator] != input_pattern_list[pattern_index_iterator]:
                flag = 1

            if flag == 1:
                break
            elif flag == 0 and pattern_index_iterator == len(input_pattern_list) - 1:
                offset_list.append(temp_offset)

            temp_iterator += 1
            if temp_iterator == len(input_string_list):
                flag = 2
                break
        if flag == 2:
            break
        string_index_iterator += 1

    for val in offset_list:
        print_check = 1
        print("Offset " + str(val))
    if print_check == 0:
        print("No match found !")