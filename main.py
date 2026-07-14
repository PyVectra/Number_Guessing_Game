import random
# number_guessed = int(input("Enter your Guess:"))
# if number_required > number_guessed:
#     print("Incorrect!, Number is greater than what you have guessed.")
# elif number_required < number_guessed:
#     print("Incorrect!, Number is less than what you have guessed.")
# elif number_required == number_guessed:
#     print("Correct!")

# def play():
#     m = 0
#     number_guessed = int(input("Enter your Guess: "))
#     if number_required > number_guessed:
#         print("Incorrect!, Number is greater than what you have guessed.")
#         m+=1
#         if m<=5:
#             print(m)
#             return play()
#     elif number_required < number_guessed:
#         print("Incorrect!, Number is less than what you have guessed.")
#         m+=1
#         if m<=5:
#             print(m)
#             return play()
        
#     elif number_required == number_guessed:
#         print("Correct!")

# play()

number_required = random.randint(0,50)
class Game:
    def __init__(self,m,score,player):
        self.m = m
        self.score = score
        self.player = player
    # print("PLAYER",player)
    def play(self):
        # print(f"Hint: Number is between:",(number_required-0,number_required+20))
        number_guessed = int(input("Enter your Guess: "))
        if number_required > number_guessed:
            print("Incorrect!, Number is greater than what you have guessed.")
            self.m+=1
            if self.m<5:
                if 1<=abs(number_guessed - number_required)<=2:
                    print("🔥You're extremely close!")
                elif 3<=abs(number_guessed - number_required)<=5:
                    print("😄 Very close!")
                elif 6<=abs(number_guessed - number_required)<=10:
                    print("🙂Close, keep going!")
                elif 11<=abs(number_guessed - number_required)<=20:
                    print("😐You're getting there.")
                elif 21<=abs(number_guessed - number_required)<=35:
                    print("🥶You're quite far away!")
                elif abs(number_guessed - number_required)>=35:
                    print("Not even close!")
                print("Attempts remaining:",5-self.m)
                return self.play()
            else:
                print(f"GAME OVER! The number was {number_required}.")
                self.score = 0
                print(f"Your score is {self.score}")
        elif number_required < number_guessed:
            print("Incorrect!, Number is less than what you have guessed.")
            self.m+=1
            if self.m<5:
                if 1<=abs(number_guessed - number_required)<=2:
                    print("🔥You're extremely close!")
                elif 3<=abs(number_guessed - number_required)<=5:
                    print("😄 Very close!")
                elif 6<=abs(number_guessed - number_required)<=10:
                    print("🙂Close, keep going!")
                elif 11<=abs(number_guessed - number_required)<=20:
                    print("😐You're getting there.")
                elif 21<=abs(number_guessed - number_required)<=35:
                    print("🥶You're quite far away!")
                elif abs(number_guessed - number_required)>=35:
                    print("Not even close!")
                print("Attempts remaining:",5-self.m)
                return self.play()
            else:
                print(f"GAME OVER! The number was {number_required}.")
                self.score = 0
                print(f"Your score is {self.score}")
        elif number_required == number_guessed:
            if self.m == 1:
                self.score = 25
            elif self.m == 2:
                self.score = 20
            elif self.m == 3:
                self.score = 15
            elif self.m == 4:
                self.score = 10
            elif self.m == 5:
                self.score = 5
            print(f"Correct! Your score is {self.score}")
            

    

player_1 = Game(0,0,1)
player_1.play()


