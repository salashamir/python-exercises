words = ["One", "Onus", "ThesAUrus", 'ANACONDA', "elated", "onward", "ouroboros"]

def print_upper_words(words, must_start_with):
    """ Given list of words, returns all the words uppercased
    """  
    # lowercase all letters in must_start_with set
    letters_in_set = [];
    for letter in must_start_with:
        letters_in_set.append(letter.lower())
    for word in words:
        if word[0].lower() in letters_in_set:
            print(word.upper())


print_upper_words(words, {"o"})
