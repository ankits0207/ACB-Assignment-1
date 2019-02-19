# MT16121
# Ankit Sharma

# Code to return list of lists for the required pascal triangle
def pascals_triangle_recursion(my_level):
    if my_level == 1:
        return [[1]]
    elif my_level == 2:
        return [[1], [1, 1]]
    else:
        my_list = [None]*my_level
        returned_list = pascals_triangle_recursion(my_level-1)
        upper_list = returned_list[my_level-2]
        my_list[0] = 1
        my_list[my_level - 1] = 1
        for i in range(1, my_level - 1):
            my_list[i] = upper_list[i-1] + upper_list[i]
        returned_list.append(my_list)
        return returned_list


level = int(input("Enter number of levels of the pascal triangle with first level being level 1 "))
list_of_lists = pascals_triangle_recursion(level)
for my_list_1 in list_of_lists:
    for elements in my_list_1:
        print(elements, end=' ')
    print()