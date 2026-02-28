def add_punctuation(sentences):
    # Create a set of all uper letters
    set_upper_Case = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    # convert the string in a list
    list_sentences = list(sentences)
    #init pos variable in 0
    pos = 0
    # while not in the end of the list
    while pos < len(list_sentences):
        # if char in this position is uppercase and there is a space before
        if list_sentences[pos] in set_upper_Case and list_sentences[pos-1] == ' ':
            # insert the new character
            list_sentences.insert(pos-1,'.')
            # increment position of added character
            pos += 1
        # change position to next character
        pos += 1
    # insert the . character at the end of the list
    list_sentences.insert(len(list_sentences),'.')
    # return the list as a string
    return "".join(list_sentences)

if __name__ == '__main__':
    #print(add_punctuation("Hello world"))
    print('------')
    print(add_punctuation("Hello world It's nice today"))
    print('------')
    print(add_punctuation("JavaScript is great Sometimes"))
    print('------')
    print(add_punctuation("A b c D e F g h I J k L m n o P Q r S t U v w X Y Z"))
    print('------')
    print(add_punctuation("Wait.. For it"))
    print('------')