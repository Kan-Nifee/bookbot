#Main Purposed of this program will be to allow me to loop throw text files and evaluate them,
#When its done I should be able to prompt for;
#                                             1.) How many times a word is used
#                                             2.) How many words total
#                                             3.) Ratio of promt words used to compared to other words
#                                             4.) Pass output of Program into text file for later reference



import errno

def main ():
#this block handles incorrect file types because humans will make errors and we dont want- 
#-the user to have to open the file again just because I CANT TYPE lol    
    file_not_found = False
    while not file_not_found:
        try:
#variable below prompts and stores a user input so we can try and catch inorrect files and of course
#-evaluate correct ones
            path_to_file = (input("please provide book bot with the path to file: \n"))
            print ("")
            print (f"Thank you for your selection{path_to_file}")
            print ("")

            with open(path_to_file) as f:
                file_contents = f.read()
                file_not_found = True
        except FileNotFoundError as e:
            if e.errno == errno.ENOENT:
                print ("INPUT ERROR; FILE OR PATH TO FILE IS NOT CORRECT")
    
#splits text file into whole words based on wite space for counting later.
    words = file_contents.split()
    
#holds counted words, used to return or print total # of words in text doc. 
    count = 0
    
#iterates over previously split words and adds them to count for tallying
    for each_word in words:
        count += 1
    
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
    
      
    print ("")
    
    print (f"--- Begin report of {path_to_file} ---")        
    print (f"{count} words were found in the document")
    
    for letter, value in char_count.items():
        print (f"The {letter} charactger was found {value} times")
        print ("--- End report ---")
main()