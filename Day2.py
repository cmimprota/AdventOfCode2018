from collections import defaultdict

# PART 1
with open("Day2input.txt") as f:
    input = f.readlines()
    input = list(map(str, input))
    f.close()
counter = {2: 0, 3: 0}
for i in input:
    alphabet = defaultdict(int)
    for character in i:
        alphabet[character] += 1
    couple = False
    triplet = False    
    for character, count in alphabet.items():
        if count == 2 and couple==False:
            couple = True
            counter[2] += 1
        if count == 3 and triplet==False:
            triplet = True
            counter[3] += 1
        

print("{} items with 2 common letters, {} items with 3 common letters".format(counter[2], counter[3]))
print("Checksum: {}".format(counter[2] * counter[3]))

# PART 2
for i in range(len(input)):
    firstBox = input[i]
    for j in range(i, len(input)):
        secondBox = input[j]
        counter = 0
        index = 0
        if(len(firstBox)==len(secondBox)):
            for k in range(len(firstBox)):
                if(firstBox[k]!=secondBox[k]):
                    counter+=1
                    if counter==1:
                        index = k
            if counter==1:
                common = firstBox[:index] + firstBox[index+1:]
                print(firstBox)
                print("{} and {} differ exactly one character at index {}".format(firstBox[:-1], secondBox[:-1], index))
                print("The letters in common between the two boxes are and {}".format(common)) 