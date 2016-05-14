from Bio import SeqIO

records = SeqIO.parse('/home/wenlei/ns1_combined_aligned.fasta','fasta')
records = list(records)

all_description = [i.description.strip() for i in records]

avian_records = SeqIO.parse('/home/wenlei/ns1_avian_refined.fasta','fasta')
avian_list = []
for record in avian_records:
    description = record.description
    avian_list.append(description.strip())
    
    
human_records = SeqIO.parse('/home/wenlei/ns1_human_refined.fasta','fasta')
human_list = []
for record in human_records:
    description = record.description
    human_list.append(description.strip())



avian_output = []
human_output = []

count = 0
for record in records:
    description = record.description
    accession = description.split('|')[-2].strip()

    if description in avian_list:
        avian_output.append(record)
    elif description in human_list:
        human_output.append(record)
    else:
        print 'failed'
print len(avian_output)
print len(human_output)
SeqIO.write(avian_output,'/home/wenlei/avian_alignment.fasta','fasta')
SeqIO.write(human_output,'/home/wenlei/human_alignment.fasta','fasta')
