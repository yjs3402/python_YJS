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
