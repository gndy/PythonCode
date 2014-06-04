from Bio import SeqIO
import sys

seqs = []
for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
    txtRecords = file(sys.argv[2]).readlines()
    if seq_record.name in txtRecords:
	seq.append(seq_record)
SeqIO.write(seqs, sys.argv[3], "fasta")
