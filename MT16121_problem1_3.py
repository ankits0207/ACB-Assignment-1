# MT16121
# Ankit Sharma

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC


# Method to transcribe the input DNA sequence
def transcription(DNA):
    list_of_char = list(DNA)
    for i in range(0, len(list_of_char)):
        if list_of_char[i] == 'T':
            list_of_char[i] = 'U'
    return list_of_char

# Method to get the dictionary corresponding to the codon table
def get_codon_dict(file_name):
    my_dict = dict()
    with open(file_name) as file:
        lines = file.readlines()
    for line in lines:
        my_content = line.split("\t")
        my_dict[my_content[0]] = my_content[1]
    return my_dict

mydict = get_codon_dict("codon_table.tsv")
list_of_prot = []

# Python code to transcribe and translate the given sequence in proteins
for record in SeqIO.parse("problem1_gene.fasta", "fasta"):
    my_protein = []
    RNA = transcription(record.seq)
    flag = 0
    i = 0
    while i < len(RNA)-2:
        if i == 0:
            my_protein.append('M')
        elif RNA[i] == 'U' and RNA[i + 1] == 'A' and (RNA[i + 2] == 'A' or RNA[i + 2] == 'G'):
            pass
        elif RNA[i] == 'U' and RNA[i + 1] == 'G' and RNA[i + 2] == 'A':
            pass
        else:
            triplet = RNA[i] + RNA[i + 1] + RNA[i + 2]
            my_protein.append(mydict[triplet])
        i += 3
    r = SeqRecord(Seq(''.join(my_protein), IUPAC.protein), id=record.id)
    list_of_prot.append(r)

SeqIO.write(list_of_prot, "problem1_protein.fasta", "fasta")
print("Fasta file (problem1_protein.fasta) written successfully.")






