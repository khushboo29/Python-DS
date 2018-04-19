def reverseWord(input):
    str = input.split(" ")
    str = str[-1::-1]
    output = ' '.join(str)
    return output
    
if __name__ == '__main__':
    input = "hello this is working"
    print reverseWord(input)
