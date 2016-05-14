def summary(l):
    output_list = []
    for i in list(set(l)):
        output_list.append((i,l.count(i)))
    output_list.sort()
    return output_list
        
        
avian_dir = '/home/wenlei/Influenza_study/avian/raw_protein_sequence/'
human_dir = '/home/wenlei/Influenza_study/human/raw_protein_sequence/'

protein_name = 'HA_protein'

from Bio import SeqIO

output_list = []
records_avian = SeqIO.parse(avian_dir+protein_name,'fasta')
records_avian = list(records_avian)
for record in records_avian:
    if len(record)>= 560:
        output_list.append(record)
lengths_avian = [len(record) for record in records_avian]

print summary(lengths_avian)
SeqIO.write(output_list,'/home/wenlei/Influenza_study/ha_avian_refined.fasta','fasta')

output_list = []
records_human = SeqIO.parse(human_dir+protein_name,'fasta')
records_human = list(records_human)
for record in records_human:
    if len(record)>= 560:
        output_list.append(record)
        
        
lengths_human = [len(record) for record in records_human]
print summary(lengths_human)

#print summary([len(i) for i in list(SeqIO.parse('/home/wenlei/ns1_combined.fasta','fasta'))])

SeqIO.write(output_list,'/home/wenlei/Influenza_study/ha_human_refined.fasta','fasta')
