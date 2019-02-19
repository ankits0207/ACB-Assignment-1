# MT16121
# Ankit Sharma
# The speed of the biopython parser is very fast as compared to my own parser on large data sets. Biopython parsers are
# easier to use and they are well organized in classes.


from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import time

text_file = open("Output_fasta.txt", "w")
for record in SeqIO.parse("Input_2_3.fasta", "fasta"):
    text_file.write(str(record.seq) + '\n')
text_file.close()
print('Time to read fasta file and write txt file ' + str(time.clock()))

i = 1
my_list = []
for record in SeqIO.parse("mtb.gb", "genbank"):
    for feature in record.features:
        if feature.type == "CDS":
            start = feature.location.start
            stop = feature.location.end
            coding_region = record.seq[start:stop]
            if "gene" in feature.qualifiers:
                gene = feature.qualifiers["gene"][0]
            else:
                gene = None
            locus_tag = feature.qualifiers["locus_tag"][0]
            loc = str(start+1)+".."+str(stop)

            if gene is None:
                desc = "[locus_tag=" + locus_tag + "]" + " " + "[location=" + loc + "]"
            else:
                desc = "[gene=" + gene + "]" + " " + "[locus_tag=" + locus_tag + "]" + " " + "[location=" + loc + "]"

            rec = SeqRecord(coding_region, id="lcl|"+record.id+"_gene_"+str(i), description = desc)
            my_list.append(rec)
            i += 1
SeqIO.write(my_list, "problem1_gene.fasta", "fasta")
print("Fasta file (problem1_gene.fasta) written successfully.")