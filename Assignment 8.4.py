#dene = open("C:/Users/a/Desktop/Coursera/dene.txt","r")
"""lst=list()

try:
    with open("C:/Users/a/Desktop/Coursera/dene.txt","r") as file:
        for i in file:
            print(file.read().split())
except Exception as e:
    print(e)
"""

#fname = input("Enter file name: ")
lst = list()
try:
    with open("C:/Users/a/Desktop/Coursera/dene.txt","r") as fh:
        for line in fh:
            parts = line.split()
        for part in parts:
            if not part in lst:
                lst.append(part)
                lst.sort()
        print(lst)
except Exception as e:
    print(e)
 
"""fname = input("Enter file name: ")
lst = list()
fh = open(fname)
for line in fh:
    parts = line.split()
    for part in parts:
        if not part in lst:
            lst.append(part)
lst.sort()
print(lst)"""
        
#t = dene.read()
#print(t)
#dene.close()