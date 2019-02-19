# MT16121
# Ankit Sharma

# Python code to transcribe the given DNA sequence (Replace T by U)
DNA = input("Enter the DNA sequence ")
list_of_char = list(DNA)
for i in range(0, len(list_of_char)):
    if list_of_char[i] == 'T':
        list_of_char[i] = 'U'
print("Corresponding RNA sequence is ", end='')
for char in list_of_char:
    print(char, end='')

