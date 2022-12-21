def swap_case(s):
    sentence = []
    for i in s:
        if i.isupper():
            sentence.append(i.lower())
            se = "".join(sentence)
        else:
            sentence.append(i.upper())
            se = "".join(sentence)
        
    return se

if __name__ == '__main__':
