list_of_seq_unprocessed = []
list_of_seq_processed = []

# Code to read file
with open("Input_2_3.fasta") as file:
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

size = len(list_of_seq_processed[0])
list_of_lists = []
for i in range(0, 4):
    inner_list = [0] * size
    list_of_lists.append(inner_list)
for i in range(0, size):
    A = 0
    C = 0
    G = 0
    T = 0

    for list_of_char in list_of_seq_processed:
        if list_of_char[i] == 'A':
            A += 1
        elif list_of_char[i] == 'C':
            C += 1
        elif list_of_char[i] == 'G':
            G += 1
        else:
            T += 1
    for j in range(0, 4):
        if j == 0:
            inn_list = list_of_lists[j]
            inn_list[i] = A
        elif j == 1:
            inn_list = list_of_lists[j]
            inn_list[i] = C
        elif j == 2:
            inn_list = list_of_lists[j]
            inn_list[i] = G
        else:
            inn_list = list_of_lists[j]
            inn_list[i] = T

# Code to generate consensus sequence and frequency matrix
consensus = []
for i in range(0, size):
    max = -1
    max_idx = -1
    for j in range(0, 4):
        if list_of_lists[j][i] > max:
            max = list_of_lists[j][i]
            max_idx = j
    if max_idx == 0:
        consensus.append('A')
    elif max_idx == 1:
        consensus.append('C')
    elif max_idx == 2:
        consensus.append('G')
    else:
        consensus.append('T')

print("Consensus:" + ''.join(consensus))

print("Frequency Matrix:")
print('[',end='')
for i in range(0, len(list_of_lists)):
    if i == len(list_of_lists)-1:
        print(list_of_lists[i], end=']')
    else:
        print(list_of_lists[i], end=',')
        print()