def decodeMorse(morseCode):
    # First, split the input by triple spaces to get the words
    words = morseCode.strip().split('   ')
    
    # For each word, split it by single spaces and decode each letter using the MORSE_CODE dictionary
    decoded_words = []
    for word in words:
        decoded_word = ''.join(MORSE_CODE[letter] for letter in word.split(' '))
        decoded_words.append(decoded_word)
    
    # Join all decoded words with a space and return the result
    return ' '.join(decoded_words)