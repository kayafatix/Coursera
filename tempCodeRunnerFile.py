#dene = open("C:/Users/a/Desktop/Coursera/dene.txt","r")
lst=list()

try:
    with open("C:/Users/a/Desktop/Coursera/dene.txt","r") as file:
        for i in file:
            print(file.read().split())
except Exception as e:
    print(e)
