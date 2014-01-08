'''
Created on 2014-1-7

@author: gndy
'''
from Bio import SeqIO
import sys
import os

def hamdist(str1, str2):
    '''return the hamming distance'''
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
            if ch1 != ch2:
                    diffs += 1
    return diffs

def strfromreads(barcode,read):
    length = len(barcode)
    readstr = read.seq[0:length]
    return readstr


barcodes = file(sys.argv[2]).readlines()
idents = [ident.split('\t')[0] for ident in barcodes]
bars = [ident.split('\t')[1].strip() for ident in barcodes]

for i in range(len(bars)):
    seqs = []
    original_reads = SeqIO.parse(sys.argv[1],'fastq')
    for read in original_reads:
        if int(hamdist(bars[i],strfromreads(bars[i],read)))<int(sys.argv[3]):
            seqs.append(read[len(bars[i]):])
    count = SeqIO.write(seqs, idents[i]+'.fastq', 'fastq')
    print idents[i]+str(count)
    



