user_input = int(input())
words_map ={}
for _ in range(user_input):
    word = input()
    if word in words_map:
        words_map[word] += 1
    else:
        words_map[word] = 1
        
print(len(words_map))
for val in words_map.values():
    print(val, end = " ")    
