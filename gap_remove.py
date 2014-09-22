from Bio import SeqIO
import sys,os


filenames = os.listdir(sys.argv[1])
for file in filenames:
    seq_records = SeqIO.parse(sys.argv[1]+file,'fasta')
    print file
    for seq in seq_records:
        if 'reference' in seq.name:
            reference = seq
            positions = []
            isDNA = False
            for i in range(len(reference)):
                if reference.seq[i] != '-':
                    if isDNA == False:
                        positions.append(i)
                        isDNA = True
                elif isDNA == True:
                    positions.append(i)
                    isDNA = False
            positions.append(len(reference))
    print positions
    print '================='
    seq_records = SeqIO.parse(sys.argv[1]+file,'fasta')
    output = []
    for myseq in seq_records:
        seq_tmp = myseq[positions[0]:positions[1]]
        for i in range(2,len(positions),2):
            if i<len(positions)-1:
                seq_tmp = seq_tmp+myseq[positions[i]:positions[i+1]]
        output.append(seq_tmp)
    SeqIO.write(output,sys.argv[2]+file,"fasta")
        
