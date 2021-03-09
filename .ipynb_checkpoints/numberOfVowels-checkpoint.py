def numberOfVowels(data):
    '''
        numberOfVowels: count the number of values that appear in a string; vowels: a, e, i, o u 
        inputs: data  as string
        return: count as int
        expected output: 
        3
        5
        5
    '''
    vowels ='aeiou'
    count = 0
    try:
        for letter in data:
            if letter in vowels:
                count += 1
    finally:
        return count


print(numberOfVowels("orange"))
print(numberOfVowels("lighthouse labs"))
print(numberOfVowels("aeiou"))
