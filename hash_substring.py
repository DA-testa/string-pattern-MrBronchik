# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    t_input=input().strip().upper()
    if t_input=="I":
        pattern=input().strip()
        text=input().strip()
    elif t_input=="F":
        filename='tests/06'
        with open(filename) as file:
            pattern=file.readline().strip()
            text=file.readline().strip()
            
    else:
        exit()
    return t_input, pattern,text          
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences( t_input,pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    text_l=len(text)
    pattern_l=len(pattern)
    occurances=[]
    if t_input=="I":
        for i in range(text_l-pattern_l+1):
            if text[i: i+pattern_l]==pattern:
                occurances.append(i)
    elif t_input=="F":
        pattern1=sum(ord(pattern[i])*pow(10,pattern_l-i-1) for i in range(pattern_l))
        text1=sum(ord(text[i])*pow(10,pattern_l-i-1) for i in range(pattern_l))
        for i in range(text_l-pattern_l+1):
            if text1==pattern1 and text[i:i +pattern_l]==pattern:
                occurances.append(i)
            if i<text_l-pattern_l:
                text1=(text1-ord(text[i])*pow(10,pattern_l-1))*10+ord(text[i+pattern_l]) 
                                        
    # and return an iterable variable
    return occurances
    

# this part launches the functions
if name == 'main':
    print_occurrences(get_occurrences(*read_input()))
