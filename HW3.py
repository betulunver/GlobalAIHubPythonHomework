import random

# Homework 3
"""
Code The Hangman Game
You are the free on this assignment.
YOu can set the rules yourself. There is only one thing expected of you.
When entering the game The User's name and for example "Welcome John" should be pressed to the screen.
When the game is over, exit the game. SO let the game end.
"""
# Game Rules
"""
Selected word length is ;
                    smaller than 5 => 3 life, 1 joker
                    smaller than 10 => 4 life, 2 joker
                    smaller than 15 = > 5 life, 3 joker
Jokers : 
        return count of randomly selected character within the selected word. For example "There are 2 "k" in word."
        gives the information whether the entered letter is the first letter of the word.
        Gives the information whether the entered letter is the last letter of the word.
                    
Pseudo code: 
1.Get username
2.print game rules
3.select random word in wordlist
4.define user life and joker
5.show user the encrypted word
6.get letter from user
7.check, is this letter in the word ?
    8.yes => show the letter to user and add userChars list
       9. Are all the letters opened? 
            10. yes => print("Congrats")
            11. no => return 6
    12.no => reduce players life
        13. life == 0
            14. yes => game over
            15. no=> return 6


                    
"""


class Game:

    def __init__(self):
        self.word = ""
        self.wordList = ["python", "computer", "programming", "artificial", "object", "hangman", "github",
                         "gamification", "intelligence"]
        self.encryptionWord = ""
        self.userChars = []
        self.joker = 0
        self.life = 0
        self.run = True

    # randomly select word in wordList
    def selectword(self):
        self.word = random.choice(self.wordList)
        self.encryptionWord = self.encryptionword()
        self.definegamerules()

    def definegamerules(self):
        length = len(self.word)
        if length < 5:
            self.life = 3
            self.joker = 1
            print(f"You have {self.life} life and {self.joker} joker. ")
        elif length < 10:
            self.life = 4
            self.joker = 2
            print(f"You have {self.life} life and {self.joker} joker. ")
        else:
            self.life = 5
            self.joker = 3
            print(f"You have {self.life} life and {self.joker} joker. ")

        print("PS : If you want use joker, Enter upper 'J'")
        print("Good luck :)")

    # show word as => * * * * * * *
    def encryptionword(self):
        obj = []
        for i in self.word:
            obj.append("*")
        print("Your word is : " + " ".join(obj))
        return obj

    # get letter from players
    def game(self):
        while self.run:
            letter = input("Enter a letter:")

            if letter == "J":
                self.selectJoker()
            elif letter == "X":
                print(f"Your exit. The word is {self.word}")
            else:
                self.controlWord(letter)

    def reducelife(self):
        self.life -= 1
        if self.life == 0:
            print("Sorry, game over man :(")
            self.returnselectedword()
        else:
            print(f"Wrong! Your life : {self.life}")

    def returnselectedword(self):
        print(f"Word is : {self.word}")

    def selectJoker(self):
        if self.joker > 0:
            print("--------- Welcome Joker Selector -------- : ")
            print(" 1 => This joker gives count of randomly selected character within the word.",
                  "\n 2=> This joker gives the information whether the your entered letter is the first letter of the word.",
                  "\n 3 => This joker gives the information whether the your entered letter is the last letter of the word.")
            select = "0"

            while select not in ["1", "2", "3"]:
                select = input("Enter your select : ")

            if select == "1":
                self.joker1()
            elif select == "2":
                self.joker2()
            elif select == "3":
                self.joker3()

            self.joker -= 1
            print(f"Your joker count: {self.joker}")

        else:
            print("Sorry, You haven't got a joker.")

    def joker1(self):
        randomletter = random.choice(self.word)
        print(f"{randomletter} => {self.word.count(randomletter)} time in word.")

    def joker2(self):
        # gives the information whether the entered letter is the first letter of the word.
        letter = input(
            "Pleas enter a character and then I give the information whether the entered letter is the first letter of the word : ")
        istrue = self.word.startswith(letter)
        if istrue:
            print("Yes!")
        else:
            print("No :(")

    def joker3(self):
        # gives the information whether the entered letter is the last letter of the word.
        letter = input(
            "Please enter a character and then I give the information whether the entered letter is the last letter of the word : ")
        if self.word.endswith(letter):
            print("Yes!")
        else:
            print("No")
    # todo: add control
    def checkinput(self, char):
        try:
            if type(char) == 'str':
                if len(char) == 1:
                    return True
                else:
                    print("Please enter only one character.!")
                    return False
            else:
                print("Invalid Value ")
                return False
        except:
            print("Invalid Value")

    def showEncryptionWord(self):
        print("Word: " + " ".join(self.encryptionWord))

    def win(self):
        print("****************Congrats ! You win :)) *********************")
        self.showEncryptionWord()
        self.run = False

    def controlWord(self, letter):
        if letter in self.userChars:
            print("You already guessed this letter, try something else.")
        else:
            self.userChars.append(letter)
            if letter in self.word:
                for i in range(len(self.word)):
                    if self.word[i] == letter:
                        self.encryptionWord[i] = letter
                if "*" not in self.encryptionWord:
                    self.win()
                else:
                    self.showEncryptionWord()

            else:
                self.reducelife()
                print("Used letters : ", self.userChars)



print("******* Welcome to the Hangman Game ******** \n *****************************************")
username = input("Please enter your name: ")

print("\n Hello {}".format(username))

game = Game()
game.selectword()
print("If you ready, let begin.")
game.game()


