f = open("dosya.txt", "r+")
lines = f.readlines()
f.seek(0)
f.truncate()
f.writelines(lines[:-2])
f.close()