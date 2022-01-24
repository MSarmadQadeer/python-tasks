List = [5, 3, 7, 6, 1, 9, 2]
print(List)
for i in range(len(List)):
    minposition = i
    for j in range(i, len(List)):
        if List[j] < List[minposition]:
            minposition = j
    List[i], List[minposition] = List[minposition], List[i]
print("Selection Accending Sort: ", List)
