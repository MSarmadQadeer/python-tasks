string = list(input("Enter Any data: ").lower())
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
         "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
new = []
for i in alpha:
    new.append(string.count(i))

print(new)
print(alpha[new.index(max(new))])
