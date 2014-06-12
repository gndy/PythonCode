
# coding: utf-8

# In[ ]:

from Bio import SeqIO
import sys

count = [0,0,0,0,0,0,0,0,0,0]
for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
    length = len(seq_record)
    if length>0 and length<=100:
        count[0] = count[0]+1
    elif length>100 and length<=200:
        count[1] = count[1]+1
    elif length>200 and length<=300:
        count[2] = count[2]+1
    elif length>300 and length<=400:
        count[3] = count[3]+1
    elif length>400 and length<=500:
        count[4] = count[4]+1
    elif length>500 and length<=600:
        count[5] = count[5]+1
    elif length>600 and length<=700:
        count[6] = count[6]+1
    elif length>700 and length<=800:
        count[7] = count[7]+1
    elif length>800 and length<=900:
        count[8] = count[8]+1
    elif length>900 and length<=1000:
        count[9] = count[9]+1
for i in count:
    print i

