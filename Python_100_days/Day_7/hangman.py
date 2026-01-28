import random

word_list = ["aardvark", "baboon", "camel"]

choosen_word = random.choice(word_list)
print(choosen_word)

place = ""
correct_letters = []
life = 6
for _ in choosen_word:
    place += "_"
print(place)
game_over = False
while not game_over:
        guess = input("Guess a letter: ").lower()

        display = ""

        for letter in choosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
        print(display) 
        if guess not in choosen_word:
            life -= 1
            print(f"You have {life} lives left")
        if "_" not in display:
            game_over = True
            print("You win")
        elif life ==0:
            game_over = True
            print("You lose")