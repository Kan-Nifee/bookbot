def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    #splits text file into whole words based on wite space for counting later.
    words = file_contents.split()
    #holds counted words, used to return or print total # of words in text doc.
    
    count = 0
    #iterates over previously split words and adds them to count for tallying
    for each_word in words:
        count += 1
    print (count)
    
    #NEW OPERATION for tallying idividual characters (letters) so letters can be counted
    chars = list(file_contents.lower())  #Holds individual lettter from Text fil for looping throught and tallyiong
    
    #char_count has each letter set to 0 as we iterrate over each char we will updated the count per letter then return the list)
    
    char_count = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 
    'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 
    's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0  
    }

    for char in chars:
        if char in char_count:
            char_count[char] += 1
            
    print (char_count)

main()