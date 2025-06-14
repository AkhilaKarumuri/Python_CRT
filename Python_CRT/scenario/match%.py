def generate_report(dna,db):
    count_G=0
    count_c=0
    if dna in db:
        ID=db[dna]
    for i in dna:
        
