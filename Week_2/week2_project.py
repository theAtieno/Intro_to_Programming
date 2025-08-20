import random

Game = (
    "abruptly","absurd","abyss","boxcar","boxful","buckaroo","cockiness","croquet","crypt","curacao","dizzying","duplex","dwarves","espionage","euouae","exodus",
    "foxglove","frazzled","frizzled","giaour","gizmo","glowworm","haiku","haphazard","hyphen","injury","ivory","ivy","jaundice","jawbreaker","jaywalk","keyhole","khaki",
    "kilobyte","lucky","luxury","lymp","megahertz","microwave","mnemonic","nowadays","numbskull","nymph","ovary","oxidize","oxygen","pixel","pizazz","pneumonia","quixotic",
    "quiz","quizzes","rhubarb","rhythm","rickshaw","sphinx","spritz","squawk","topaz","transcript","transgress","unknown","unworthy","unzip","voodoo","vortex","voyeurism",
    "wheezy","whiskey","whizzing","xylophone","yoked","youthful","yummy","zephyr","zigzag","zigzagging","zilch","zipper"
)   

# Now, apply the input function to allow the user to make letter guesses. 
# Use try... except and if statements to make sure that only valid inputs work with your script 
# i.e. a user can only choose one letter at a time, and a user cannot choose letters that have been chosen before.
# # If the letter is in the word then it is printed in place of the corresponding dash. 
# If the letter is not in the word, that is counted as a failed attempt, 
# Limit the number of failed attempts for the user to 6 such that on the 6th fail, the game ends and the script 
# prints the actual word and "You Lost". 
# Make sure to tell the user they won if they guess all the correct letters in under 6 failed attempts.

secret_word = random.choice(Game)
secret_word_len = ["_"]*len(secret_word)
print(secret_word_len)

wrong_guesses = 0
max_attempts = 6 

guessed_letters = []

while "_" in secret_word_len and wrong_guesses < max_attempts:

    try:
        guessed_letter = input("Enter a letter: ").lower().strip()

        if len(guessed_letter) != 1:
            raise ValueError("Enter ONE letter (a-z):")
        
        if  guessed_letter in guessed_letters:
            raise ValueError("You already guessed this:")

        guessed_letters.append(guessed_letter)

        if guessed_letter in secret_word:
            print("Correct guess")
            for i,letter in enumerate(secret_word) :
                if letter == guessed_letter :
                 secret_word_len [i] = guessed_letter
        else:
            wrong_guesses +=1
            print(f"Failed Attempt. You have: {max_attempts - wrong_guesses} tries left") 

        print("Word:" , " ".join(secret_word_len))   

    except ValueError as e:
        print(e)
if "_" not in secret_word_len:
    print(f"Congratulations! You guessed the correct word. The word is: {secret_word}")

else:
    print(f"You Lost. The secret word is {secret_word}")
