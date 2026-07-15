# decoding secret coded sentence

# input:
# encoded sentence with the letter p and the same vowel when a vowel comes up

# output:
# original sentence decoded

sentence = 'ipi lipikepe yopoupu'

# initiating the result var and character index
result = ''
char_idx = 0


# looping through each of the character in the sentence
while char_idx< len(sentence):
    
    # adding each char to result
    result += sentence[char_idx]
    
    # if vowel, skipping the encoded chars to the actual chars
    if sentence[char_idx] in 'aeiou':
        char_idx+=3
    
    # if consonant,dont skip but just move to next char
    else:
        char_idx+=1

print(result)