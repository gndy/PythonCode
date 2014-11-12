from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio import SeqIO
import sys,os
'''
translate the dna sequences to amino acid sequences, need a consensus to calculate the index of dna segments
'''

def listcmp(l,ll):
    length = len(l)
    count = 0
    for i in range(length):
        if str(l[i]).upper()==str(ll[i]).upper():
            count = count+1
    if count >= 15 :
        return True
    else:
        return False

def myindex(seed,lists):
    for i in range(len(lists)):
        if listcmp(seed,lists[i]) == True:
            return i
    return -1

def startindex(sequence,lists):
    '''
    this function is for s gene slice and indexing
    '''
    for i in range(len(sequence)-20):
        if i<50:
            sliding = sequence[i:i+20]
            index = myindex(sliding,lists)
            if index != -1:
                mytuple = (i,index)
                return mytuple

	else:
            return (-1,-1)
    
files =os.listdir(sys.argv[1])
consensus = SeqIO.parse('/home/wenlei/s_dna_consensus.fna','fasta')
con_seq = str(list(consensus)[0].seq)
con_seqs = [con_seq[i:i+20] for i in range(len(con_seq)-20)]


for item in files:
    sequences = SeqIO.parse(sys.argv[1]+item,'fasta')
    output = []
    mismatch = 0
    count = 0
    star_count = 0
    print ''
    print item
    for myseq in sequences:
        count = count+1
        seed = myseq.seq
        seed = str(seed).upper()
	result_tuple = startindex(seed,con_seqs)
        start = result_tuple[0]
        pos = result_tuple[1]
	print count
        if pos != -1:
            adjust = 3-pos%3
            if adjust != 3:
                trans = myseq.seq[start+adjust:].translate()
            else:
                trans = myseq.seq[start:].translate()
            if (678-pos)/3<len(trans):
                trans = trans[0:(678-pos)/3]
            if '*' in str(trans):
                star_count = star_count+1
            else:
                myseq.seq = trans
		print trans
                output.append(myseq)
        else:
            mismatch = mismatch+1
    print 'star number'+str(star_count)
    print 'mismatch'+str(mismatch)
    print 'all'+str(count)
    SeqIO.write(output,sys.argv[2]+item,'fasta')
