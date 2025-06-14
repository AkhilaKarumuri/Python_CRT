db = {
  "seq001": "ATGCGGAATT",
  "seq002": "CGTACGTAGC",
  "seq003": "TTATGCATTA",
  "seq004": "GGAATCCGTA",
  "seq005": "CATGCCGTAGC",
  "seq006": "GGGCGTGCAT",
  "seq007": "AATGCTAGCTA",
  "seq008": "CGCGATGCGC",
  "seq009": "TATATATATA",
  "seq010": "ATGCGGATGCA"
}
query=input("Enter the query to find:")
matches = []
for key, value in db.items():
    if value == query:
        matches.append(key)
else:
  print(f"No match found for {query}")