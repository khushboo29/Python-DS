def reverseSentence(input):
    str = input.split(" ")
    words = [st[::-1] for st in str]
    output = ' '.join(words)
    return output
    
if __name__ == '__main__':
    input = "hello this is working"
    print reverseSentence(input)

#one linear for the same 
'''
' '.join(word[::-1] for word in Sentence.split(" "))
'''
