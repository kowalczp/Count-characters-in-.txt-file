import os
import zipfile

with zipfile.ZipFile('zadanie_1_words.zip') as z:
    for filename in z.namelist():
        if not os.path.isdir(filename):
            
            with z.open(filename) as f:
                for line in f:
                    a= str(line.upper())
                    print(dict([(x, a.count(x)) for x in a]))
