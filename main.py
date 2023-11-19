'''
Our goal is the match scrambled words to a list of unscrambled words. We're doing this by creating a dictionary with all words sorted alphabetically as the key.

After that we take the input from the inputfile.txt, match them with the dictionary and output them to console. Comma seperated.
'''

words_dictionary = {}
input_words = []

'''
Load the wordlist and put the words in a dictionary. The keys are the words but alphabetically sorted, the values are the words
'''
def loadWords():
    with open("wordlist.txt") as wordlist:
        for word in wordlist:
            words_dictionary[''.join(sorted(word.strip()))] = word.strip()

'''
Load the scrambled words from file. No sanity checking or validations. Sort the input words and put them in the list.
'''
def loadInput():
    with open("inputfile.txt") as inputs:
        for word in inputs:
            input_words.append(''.join(sorted(word.strip())))

def main():
    loadWords()
    loadInput()
    
    output_string = ''
    output_words = []

    for word in input_words:
        output_words.append(words_dictionary[word])
    output_string = ','.join(output_words)
    print(output_string)

main()