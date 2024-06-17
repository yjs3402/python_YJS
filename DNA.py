DNA = "ctacaatgtcagtatacccattgcattagccgg"
ATGC = {
    "a": 0 ,
    "t": 0 ,
    "g": 0 ,
    "c": 0
}

for i in DNA:
    ATGC[f"{i}"]+=1
print(ATGC)

codon = {

}
for i in range(len(DNA)//3):
    start=i*3
    end=start+3

    piece=DNA[start:end]
    if piece in codon:
        codon[piece]+=1
    else:
        codon[piece]=1
print(codon)
