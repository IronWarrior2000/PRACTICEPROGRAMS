alphabet = []
vowels = ['a','e','i','o','u']


for i in range(97,123):
    if chr(i) not in vowels:
        alphabet.append(chr(i))


def main():

    word = change_word('SpookySkeletons')
    print(alphabet)
    print(vowels)
    print(word)



def change_word(case):
    split_case = list(case)


    print(split_case)


    ## using the Modulo operator, it helps the vowels and character loop back around as 
    ## the last index being U(index is 5) will set it back to 0 as 5 % 5 = 0

    new_word = ''

    for i in split_case:
        if i.isupper():  # Check if the character is uppercase
            if i.lower() in vowels:  # Check if it's an uppercase vowel (converted to lowercase for checking)
                index = vowels.index(i.lower())  # Find its position in the vowels list
                new_word += vowels[(index + 1) % len(vowels)].upper()  # Get next vowel and convert to uppercase
            else:  # It's an uppercase consonant
                index = alphabet.index(i.lower())  # Find its position in the alphabet list
                new_word += alphabet[(index + 1) % len(alphabet)].upper()  # Get next consonant and convert to uppercase

        elif i.islower():  # Check if the character is lowercase
            if i in vowels:  # Check if it's a lowercase vowel
                index = vowels.index(i)  # Find its position in the vowels list
                new_word += vowels[(index + 1) % len(vowels)]  # Get next vowel in lowercase
            else:  # It's a lowercase consonant
                index = alphabet.index(i)  # Find its position in the alphabet list
                new_word += alphabet[(index + 1) % len(alphabet)]  # Get next consonant in lowercase

        else:  # If it's not a letter (e.g., punctuation, numbers), leave it unchanged
            new_word += i

    return new_word

main()


