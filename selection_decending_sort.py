List = [5, 3, 7, 6, 1, 9, 2]
print(List)
for i in range(len(List)):
    maxposition = i
    for j in range(i, len(List)):
        if List[j] > List[maxposition]:
            maxposition = j
    List[i], List[maxposition] = List[maxposition], List[i]
print("Selection Decending Sort: ", List)
