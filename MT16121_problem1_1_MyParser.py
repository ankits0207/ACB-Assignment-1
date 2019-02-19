# MT16121
# Ankit Sharma
# The speed of the biopython parser is very fast as compared to my own parser on large data sets. Biopython parsers are
# easier to use and they are well organized in classes.


import time


def get_processed_list_of_seq_fasta(file_name):
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


def get_processed_list_of_seq_gbk(file_name):
    with open(file_name) as file:
        my_list = []
        lines = file.readlines()
        flag = 0
        key = ""
        val_builder = ""
        list_of_keywords = ['LOCUS', 'DEFINITION', 'ACCESSION', 'VERSION', 'DBLINK', 'KEYWORDS', 'SOURCE', 'ORGANISM', 'REFERENCE', 'AUTHORS', 'TITLE', 'JOURNAL', 'PUBMED', 'REMARK', 'CONSRTM', 'COMMENT', 'FEATURES', 'source', 'gene', 'CDS', 'tRNA', 'repeat_region', 'mobile_element', 'ORIGIN']
        for line in lines:
            trimmed_line = " ".join(line.split())
            trimmed_line_list = trimmed_line.split(' ', 1)
            if trimmed_line_list[0] in list_of_keywords and flag == 0:
                flag = 1
                key = trimmed_line_list[0]
                val_builder += trimmed_line_list[1]
            elif trimmed_line_list[0] not in list_of_keywords and flag == 1:
                val_builder += " " + trimmed_line
            elif trimmed_line_list[0] in list_of_keywords and flag == 1:
                my_list.append(key + '-' + val_builder)
                key = trimmed_line_list[0]
                val_builder = ""
                if key != 'ORIGIN':
                    val_builder += trimmed_line_list[1]
        my_list.append(key + '-' + val_builder)
        return my_list


# Reading fasta files
f_name = "Input_2_3.fasta"
processed_list_of_seq = get_processed_list_of_seq_fasta(f_name)
text_file = open("Output_fasta.txt", "w")
for elt in processed_list_of_seq:
    text_file.write(''.join(elt) + '\n')
text_file.close()
print('Output_fasta.txt written')
print('Time to read fasta file and write txt file ' + str(time.clock()))

# Reading genbank files
f_name = 'mtb.gb'
returned_list = get_processed_list_of_seq_gbk(f_name)
text_file = open("Output_gbk.txt", "w")
for elt in returned_list:
    text_file.write(elt + '\n')
text_file.close()
print('Output_gbk.txt written')

