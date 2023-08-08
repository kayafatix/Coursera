# counts = dict()
# names = ["csev", "cven", "csev", 33, "zqin", "cwen"]

# for name in names:
#     if name not in counts:
#         counts[name]=1
#     else:
#         counts[name] +=1
#
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)
#
# lines = input("Type a sentence: ")
# words = lines.split()
# print("words:", words)
#
# for word in words:
#     counts[word] = counts.get(word, 0)+1
# print("counts:", counts)
#
#
# handle = open("mbox-short.txt")
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword, bigcount)

handle = open("mbox-short.txt")
counts = dict()
count = 0
# for line in handle:
#     words = line.rstrip().split()
#     if "from" in words:
#         print(words[2])
#         #for word in words[1]:
#         counts[words[2]] = counts.get(words[2], 0) + 1
#     else:
#         continue
# handle.close()


fh = open("mbox-short.txt")
for lines in fh:
    words = lines.rstrip().split()
    if "From" in words:
        counts[words[1]] = counts.get(words[1], 0) + 1
    else:
        continue

fh.close()
bigcount = -1
bigword = None
for mail, count in counts.items():
    if count > bigcount:
        bigword = mail
        bigcount = count
print(bigword, bigcount)
# print(counts)
