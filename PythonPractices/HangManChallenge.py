import random
import time

words_to_guess = ["Apple", "Banana", "Orange", "House", "Head", "Body", "Book", "Smile", "Red", "Blue", "Sun", "Coffee", "Skirt", "Shirt", "Shoe", "Bottle", "Beauty", "car", "Yellow", "Black", "Green"]
word_selected = words_to_guess[random.randint(0, 9)]
character_count = len(word_selected)
words_correct = [" "] * character_count
tries = 5
score = 0
answer = False
answer_2 = False
game_over = False

print("Welcome to hangman in python.\nGame is case sensitive.")
time.sleep(2)

def check(tr, ans, ans2, game):
    if tr > 0 and not game:
        
        character_selected = input("Type a character that you think might be in the word: ")
        print(" ")
        time.sleep(2)
        word_spliced = []
        
        for i in word_selected:
            word_spliced.append(i)
        word_spliced_length = len(word_spliced)
        
        for i in range (0, word_spliced_length):
            if character_selected == word_spliced[i]:
                if words_correct[i] != character_selected:
                    words_correct[i] = character_selected
                    ans = True
                else:
                    ans2 = True
                
        print(words_correct)
            
        if words_correct == word_spliced:
            game = True

        if ans:
            print("Your character was right!")
            ans = False
            check(tr, ans, ans2, game)
        elif ans2:
            print("You already typed that character.")
            ans2 = False
            tr = tr - 1
            print(f"Lifes remaining: {tr}")
            check(tr, ans, ans2, game)
        elif not ans:
            print("your character was not in the word.")
            tr = tr - 1 
            print(f"Lifes remaining: {tr}")
            check(tr, ans, ans2, game)
    else:
        print("Game is over.\n")
        print(f"word was: {word_selected}")

check(tries, answer, answer_2,game_over)