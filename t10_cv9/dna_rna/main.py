# TODO Task 1
import random
from Bio import SeqIO

# record = Seq10.read("inputs/sequence.gb", "genbank")
# print(record)
# TODO Task 2

# dna = "5'-TACCGGAT"
# table = dna.maketrans("ATGC", "TACG")
# print(dna.translate(table))

# TODO Task 3
record = SeqIO.read("inputs/sequence.fasta", "fasta")
print(record.seq)


def mutate(dna):
    dna_list = list(dna)
    index = random.randint(0, len(dna_list)-1)
    dna_list[index] = random.choice("ATGC")
    return "".join(dna_list)


dna = record.seq
for i in range(1000):
    dna = mutate(dna)

print(dna)
# TODO Task 4

# C+G/DLZKA_DNA
count_seq = (record.count("C") + record.count("G")) / len(record.seq)
print(count_seq)
