counts = dict()
names = ["csev", "cven", "csev", 33, "zqin", "cwen"]

# for name in names:
#     if name not in counts:
#         counts[name]=1
#     else:
#         counts[name] +=1

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
