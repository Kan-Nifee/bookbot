#Main Purposed of this program will be to allow me to loop through text files and evaluate them,
#When its done I should be able to prompt for;
#                                             1.) How many times a word is used
#                                             2.) How many words total
#                                             3.) Ratio of promt words used to compared to other words
#                                             4.) Pass output of Program into text file for later reference
import errno
def main ():

#this block handles incorrect file types because humans will make errors and we dont want the user to have to open the file again
    file_not_found = False
    while not file_not_found:
        try:


#variable below prompts and stores a user input so we can try and catch inorrect files and of course evaluate correct ones
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
    

#iterates over previously split words and adds them to count for tallying
    just_words = file_contents.split()
    count = 0
    for each_word in just_words:
        count += 1
    

    #Next Process
    
#word finder, searches doc and record numer of instances of words
    input_word = "frankenstein" #this is a test
    
    context = []        
    how_many = 0
    for word in just_words:
        lower_word = word.lower()
        if lower_word == input_word:
            context.append(word)
            how_many += 1
            
#You're off to a good start by keeping track of the number of instances (how_many) and intending to build context around each occurrence. Let’s refine your approach a bit:
#
#You'll want to ensure you're slicing the list correctly; word in your loop currently doesn't give you the position of the word.
#
#Consider using the index of each occurrence to help with slicing.
#
#You don't need to append the word itself to context, but rather the words surrounding it.
#
#Here's a hint on how to approach these steps:
#
#As you loop over just_words, you can utilize enumerate to get both the index and the word.
#
#When you find the input_word, calculate the start and end indices for your context slice. Consider using max and min functions to stay within the list's bounds.
#
#What do you think would be necessary to implement these suggestions?            
               
    
           
                    
        
    #outputs the results in a pretty formatted way becaus we like pretty formatted reading.
    print ("")
    print (f"--- Begin report of {path_to_file} ---")        
    print ("")
    print (f"Approximately {count} words were found in the document")
    print ("")
    print (f"the word {input_word} was found {how_many}")
    print ("--- End report ---")

main()