# readFile = open("Rule.txt", "r+")
# print(readFile.read())
# print("isi : ", readFile)
with open("Verb.txt") as f: 
    temp = []
    contents = f.read()
    temp.append(contents)
print("isi dari temp adalah : ", temp)
