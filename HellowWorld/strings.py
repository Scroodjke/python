s = input("input sentence:")
length = int(input("enter word length:"))
index_word = [i for i,x in enumerate(s.split()) if len(x) == length]
max_distance = 0
if index_word :
    for i in range(len(index_word)-1):
        distance = index_word[i+1] - index_word[i]
        if max_distance < distance:
            max_distance = distance
    print(max_distance-1)
else:
    print('no words ',length, " letters long")

    