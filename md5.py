import hashlib

md5_hash_to_crack = '2f67742e1c3990db50d0a48077923916'
wordlist = open('norwegian (2).txt') .readlines() #read file into memory

def generate_combinations(word):
    yield word  # Check the word itself
    for i in range(1000):  # Generate numbers from 0 to 9
        yield str(i) + word  # Number in front
        yield word + str(i)  # Number behind
        
    # Special characters in front
        for special_char in "!@#$%^&*()_+[]{}|;:'\"<>,.?/~`":
            yield special_char + word

        # Special characters behind
        for special_char in "!@#$%^&*()_+[]{}|;:'\"<>,.?/~`":
            yield word + special_char

        # Special characters in both front and behind
        for special_char1 in "!@#$%^&*()_+[]{}|;:'\"<>,.?/~`":
            for special_char2 in "!@#$%^&*()_+[]{}|;:'\"<>,.?/~`":
                yield special_char1 + word + special_char2


for word in wordlist: #loop through each word
    word = word.strip() #stripping away whitespace etc

    result = hashlib.md5(word.encode()) .hexdigest () #compute actual hash

    if result == md5_hash_to_crack: #check if result matches
        print('Found password: ' + word) #match sucess
        
    capitalized_word = word.capitalize()  # Capitalize the first letter
    result = hashlib.md5(capitalized_word.encode()).hexdigest()  # compute hash with capital letter
    if result == md5_hash_to_crack:  # check if result matches
        print('Found password with capital letter: ' + capitalized_word)  # match success
        
    # Check combinations with numbers in front or behind
    for combo in generate_combinations(word):
        result = hashlib.md5(combo.encode()).hexdigest()  # compute hash with numbers
        if result == md5_hash_to_crack:  # check if result matches
            print('Found password with numbers: ' + combo)  # match success

print('Searched through ' + str(len(wordlist)) + ' words') #tell user we finished
