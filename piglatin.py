#**Pig Latin** - Pig Latin is a game of alterations played on the English language game. 
# To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed 
# (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.

#TO-DO: put special characters at the end, to help with questionmarks

eng_sentence = []
pig_list = []

def main(string):
    eng_sentence = string.split()
    #print(eng_sentence)
    for i in range(len(eng_sentence)):
        first_letter = eng_sentence[i][0]
            
        if first_letter.lower() not in ("a", "e", "i", "o", "u"):
            #print(f"{first_letter} is not a vowel")
            string = eng_sentence[i][1:]
            #print(string)
            new_string = pig_latinize(string,first_letter)
            pig_list.append(new_string)
        else:
            #print(f"{first_letter} is a vowel!")
            pig_list.append(pig_latinize(eng_sentence[i], ""))
    pig_sentence = " ".join(pig_list)
    print(pig_sentence)
        #print(eng_sentence[i])
        #print(first_letter)

#string is without its first letter
def pig_latinize(string, first_letter):
    # check for ! or ?
    last_letter = string[-1]
    if last_letter in ("!", "?", ",", "."):
        string = string[:-1]
    else:
        last_letter = ""    
    pig_latin = f"{string}-{first_letter}ay{last_letter}"
    return(pig_latin)    
main(input("what sentence would you like pig latinized? \n"))