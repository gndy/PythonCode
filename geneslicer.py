from Bio import SeqIO
import sys

for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
    sliceFile = file(sys.argv[2])
    seqs = []
    for i in sliceFile.readlines():
        list = i.split()
        if list:
            begin= int(list[0])-1
            end = int(list[1])
            my_seq = seq_record[begin:end]
            my_seq.description = list[0]+"-"+list[1]
            seqs.append(my_seq)
    SeqIO.write(seqs, sys.argv[3], "fasta")
        
