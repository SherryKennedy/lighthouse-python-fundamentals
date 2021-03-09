def urlEncode(text):
    '''
        urlEncode: simple encoder to replace space values with %20, simple strings, must use a loop and not replace function 
        input: text as string
        output: s as string 
        Sample output: 
        Lighthouse%20Labs
        Lighthouse%20Labs
        blue%20is%20greener%20than%20purple%20for%20sure
        NOTE: strings are mutable in python
    '''
    token = " "
    s=''
    for char in text.lstrip().rstrip():
        if ord(char) == ord(token):
            s+=  '20%'
        else:
            s +=  char
    return s

print(urlEncode("Lighthouse Labs"))
print(urlEncode(" Lighthouse Labs  "))
print(urlEncode("blue is greener than purple for sure"))
