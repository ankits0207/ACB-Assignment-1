# MT16121
# Ankit Sharma
# References - Knuth, Donald; Morris, James H.; Pratt, Vaughan (1977). "Fast pattern matching in strings" .
# SIAM Journal on Computing. 6 (2): 323–350. doi : 10.1137/0206024


# Method to generate prefix table
def get_prefix_table(list_of_char):
    list_to_be_returned = [None]*len(list_of_char)
    i = 0
    j = 1
    flag = 0

    list_to_be_returned[0] = 0

    while list_to_be_returned[len(list_of_char)-1] is None:
        if flag == 0:
            if list_of_char[j] == list_of_char[i]:
                list_to_be_returned[j] = list_to_be_returned[i] + 1
                i += 1
                j += 1
                flag = 1
            else:
                list_to_be_returned[j] = 0
                j += 1
        else:
            if list_of_char[j] == list_of_char[i]:
                list_to_be_returned[j] = i + 1
                i += 1
                j += 1
            else:
                while list_of_char[j] != list_of_char[i] and i != 0:
                    i = list_to_be_returned[i-1]

                if i == 0 and list_of_char[j] == list_of_char[i]:
                    list_to_be_returned[j] = i + 1
                elif i == 0 and list_of_char[j] == list_of_char[i]:
                    list_to_be_returned[j] = 0
                else:
                    list_to_be_returned[j] = i + 1
                flag = 0
    return list_to_be_returned

input_string = input("Enter the string ")
input_pattern = input("Enter the pattern ")

input_string_list = list(input_string)
input_pattern_list = list(input_pattern)

prefix_table = get_prefix_table(input_pattern)
string_iterator = 0
pattern_iterator = 0

offset_list = []

# Code to perform string matching using KMP
while string_iterator < len(input_string_list):
    if input_string_list[string_iterator] == input_pattern_list[pattern_iterator]:
        string_iterator += 1
        pattern_iterator += 1
    if pattern_iterator == len(input_pattern_list):
        offset = string_iterator - pattern_iterator
        pattern_iterator = prefix_table[pattern_iterator-1]
        offset_list.append(offset)
    elif string_iterator < len(input_string_list) and input_string_list[string_iterator] != input_pattern_list[pattern_iterator]:
        if pattern_iterator != 0:
            pattern_iterator = prefix_table[pattern_iterator-1]
        else:
            string_iterator += 1

for elt in offset_list:
    print('Offset ' + str(elt))