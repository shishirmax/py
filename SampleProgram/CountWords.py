OUT = 0
IN = 1
def countWords(string):
    state = OUT
    wc = 0

    for i in range(len(string)):
        if(string[i] == ' ' or string[i] == '\n' or string[i] == '\t'):
            state = OUT

        elif state == OUT:
            state == IN
            wc += 1
    return wc

string = "Hello Python"
print("No. of words: "+str(countWords(string)))    