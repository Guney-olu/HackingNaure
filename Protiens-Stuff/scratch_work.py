import re
reverse_genetic_code = {
    'I': ['ATA', 'ATC', 'ATT'],
    'M': ['ATG'],
    'T': ['ACA', 'ACC', 'ACG', 'ACT'],
    'N': ['AAC', 'AAT'],
    'K': ['AAA', 'AAG'],
    'S': ['AGC', 'AGT'],
    'R': ['AGA', 'AGG'],
    'L': ['CTA', 'CTC', 'CTG', 'CTT'],
    'P': ['CCA', 'CCC', 'CCG', 'CCT'],
    'H': ['CAC', 'CAT'],
    'Q': ['CAA', 'CAG'],
}

file_path = 'Protiens/SARS-CoV-2.txt'
with open(file_path, 'r') as file:
    protein_sequence = file.read().replace('\n', '')

dna_sequence = ''
for amino_acid in protein_sequence:
    codons = reverse_genetic_code.get(amino_acid, ['XXX'])  # 'XXX' for unknown or invalid amino acid
    dna_sequence += codons[0]


file_path = 'Protiens/C3-origin.txt'
with open(file_path, 'r') as file:
    dna_sequence = file.read()

cleaned_dna_sequence = ''.join(re.findall(r'[a-zA-Z]+', dna_sequence)).upper()


#codon-to-amino acid translation
codon_table = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
}

# Translating the DNA sequence to protein sequence
protein_sequence = ''
for i in range(0, len(cleaned_dna_sequence), 3):
    codon = cleaned_dna_sequence[i:i+3]
    amino_acid = codon_table.get(codon, 'X')  # 'X' for unknown or invalid codon
    protein_sequence += amino_acid

print(protein_sequence)

