from Bio import SeqIO
import sys,os

seqs = []
lens = []
count_all = 0
count_n = 0

seq_files = os.listdir(sys.argv[1])
for seq_file in seq_files:
    for seq_record in SeqIO.parse(sys.argv[1]+seq_file, "fasta"):
        count_all = count_all+1
        if 'n' in seq_record or 'N' in seq_record:
            count_n = count_n+1
        else:
            seqs.append(seq_record)
            lens.append(len(seq_record))
    print seq_file
    print 'total  '+str(count_all)
    print 'with n  '+str(count_n)
    #SeqIO.write(seqs, sys.argv[2], "fasta")
    #lens.sort()

    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    for i in lens:
        if i<290:
            c1 = c1+1
        elif i>290 and i<310:
            c2 = c2+1
        elif i>310 and i<330:
            c3 = c3+1
        elif i>330 and i<350:
            c4 = c4+1
        else:
            c5 = c5+1
    print '<290  '+str(c1)
    print '290-310  '+str(c2)
    print '310-330  '+str(c3)
    print '330-350  '+str(c4)
    print '>350  '+str(c5)
    print ''
