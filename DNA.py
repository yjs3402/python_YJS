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
    if DNA[i:i+3] in codon:
        codon[DNA[i*3:i*3+3]]+=1
    else:
        codon[DNA[i*3:i*3+3]]=1
print(codon)
