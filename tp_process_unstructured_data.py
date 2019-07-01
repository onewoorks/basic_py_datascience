from collections import Counter

filename = "text_data.txt"

# with open(filename) as fn:
#     ln = fn.readline()

#     lncount = 1
#     while ln:
#         print("Line {}: {}".format(lncount, ln.strip()))
#         ln = fn.readline()
#         lncount += 1


print("\n")
with open(filename) as f:
    p = Counter(f.read().split())
    print(p)