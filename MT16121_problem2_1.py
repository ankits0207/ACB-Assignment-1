# MT16121
# Ankit Sharma

K = int(input("Enter the value of K "))
my_list = ['-', 'A', 'C', 'G', 'T']


# Python code to return the list of all possible permutations
# The time complexity of this code is O(k*5^k). Simple recursive and iterative approaches also have the same complexity.
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

for obj in permute(K, -1):
    print(obj)
