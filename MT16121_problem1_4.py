# MT16121
# Ankit Sharma

from Bio import SeqIO
from decimal import Decimal

# Python code to find the GC content
for record in SeqIO.parse("problem1_gene.fasta", "fasta"):
    list_of_char = list(record)
    GC = 0
    for i in range(0, len(list_of_char)):
        if list_of_char[i] == 'G' or list_of_char[i] == 'C':
            GC += 1
    GC_content = Decimal(GC)/Decimal(len(list_of_char))*100
    print("GC content for " + record.id + " is " + str(GC_content) + "%")