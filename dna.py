import random
from collections import Counter

codon = {'Phenylalanine':['TTT','TTC'],
        'Leucine':['TTA','TTG','CTT','CTC','CTA','CTG'],
        'Isoleucine':['AUU','AUC','AUA'],
        'Methionine':['AUG'],
        'Valine':['GUU','GUC','GUA','GUG'],
        'Serine':['UCU','UCC','UCA','UCG','AGU','AGC'],
        'Proline':['CCU','CCA','CCG','CCC'],
        'Threonine':['ACU','ACC','ACA','ACG'],
        'Alanine':['GCU','GCC','GCA','GCG'],
        'Tyrosine':['UAU','UAC'],
        'Ochre':['UAA'],
        'Amber':['UAG'],
        'Histidine':['CAU','CAC'],
        'Glutamine':['CAA','CAG'],
        'Asparagine':['AGU','AGC'],
        'Lysine':['AAA','AAG'],
        'Aspartic acid':['GAU','GAC'],
        'Glutamic acid':['GAA','GAG'],
        'Cysteine':['UGU','UGC'],
        'Opal':['UGA'],
        'Tryptophan':['UGG'],
        'Aginine':['CGU','CGC','CGA','CGG','AGA','AGG'],
        'Glycine':['GGU','GGC','GGA','GGG']}

protein = {i:0 for i in codon}

dna = ''.join([random.choice(['T','C','G','A'])for i in range(6000)])

index = 0
while index < len(dna):
    strand = dna[index:index+3]
    for key in codon:
        if strand.upper() in codon[key]:
            protein[key] += 1
    index += 3


dna_strands = [ dna[strand:strand+3] for strand in range(0,len(dna),3)]
print(dna_strands)
strand_freq = {strand:dna_strands.count(strand) for strand in dna_strands} 
print(strand_freq)
oneline = {code:(strand_freq[count] if count in codon.values() else strand_freq[count]) for count,code in zip(strand_freq,codon)}

print(oneline)
 
# print({code:(Counter(dna_strands)[count] if count in codon.values() else Counter(dna_strands)  for count,code in zip(Counter(dna_strands)),codon)})
# print({code:(Counter([dna[strand:strand+3] for strand in range(0,len(dna),3)])[count] if count in codon.values() else Counter([dna[strand:strand+3] for strand in range(0,len(dna),3)])[count])  for count,code in zip(Counter([dna[strand:strand+3] for strand in range(0,len(dna),3)]),codon)})
  
# print(protein)

 