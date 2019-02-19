# MT16121
# Ankit Sharma

my_list = ['-', 'A', 'C', 'G', 'T']

# Method to get sequences from the file
def get_processed_list_of_seq(file_name):
    list_of_seq_unprocessed = []
    list_of_seq_processed = []
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            my_list_of_char = list(line)
            if my_list_of_char[0] != '>':
                list_of_seq_unprocessed.append(line)
    for idx in range(0, len(list_of_seq_unprocessed)):
        my_list = list(list_of_seq_unprocessed[idx])
        if idx != len(list_of_seq_unprocessed) - 1:
            my_list.pop()
        list_of_seq_processed.append(my_list)
    return list_of_seq_processed


# Method to return all possible permutations of size k
def permute(k, idx):
    if k == 0:
        print("No k-mer is possible!")
        exit()
    elif k == 1 and idx == -1:
        return my_list
    elif k == 1 and idx == 0:
        return '-'
    elif k == 1 and idx == 1:
        return 'A'
    elif k == 1 and idx == 2:
        return 'C'
    elif k == 1 and idx == 3:
        return 'G'
    elif k == 1 and idx == 4:
        return 'T'
    elif k == 2:
        my_output_list = []
        for i in range(0, 5):
            for j in range(0, 5):
                my_output_list.append(my_list[i] + permute(k - 1, j))
        return my_output_list
    else:
        my_output_list = []
        for i in range(0, 5):
            returned_list = permute(k - 1, -1)
            for returned_list_elt in returned_list:
                my_output_list.append(my_list[i] + ''.join(returned_list_elt))
        return my_output_list

# Method to get the count of number of occurnces of the pattern in the string
def get_count(input_string, input_pattern):
    input_string_list = list(input_string)
    input_pattern_list = list(input_pattern)

    string_index_iterator = 0
    temp_iterator = 0
    temp_offset = 0
    print_check = 0
    offset_list = []

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
    return len(offset_list)

# Method to count kmers
def count_kmers(my_str, k):
    my_dict = dict()
    permuted_list = permute(k, -1)
    for permuted_entry in permuted_list:
        count = get_count(my_str, permuted_entry)
        my_dict[permuted_entry] = count
    return my_dict

K = int(input("Enter the value of K "))
file_name = "Input_2_3.fasta"
processed_list_of_seq = get_processed_list_of_seq(file_name)
for elt in processed_list_of_seq:
    returned_dict = count_kmers(elt, K)
    print("For sequence " + ''.join(elt))
    for key, value in returned_dict.items():
        print(key + " " + str(value))