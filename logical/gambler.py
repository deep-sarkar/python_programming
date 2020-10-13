import random

class Gambler:

    def gamble(self, stack, goal, no_of_bet):
        win = 0
        loss = 0
        total_try= win + loss

        while no_of_bet != 0:
            
            if stack == goal:
                print("you won the game. Total try :", total_try)
                break
            toss = random.randrange(2)
            if stack == 0:
                print("You loss the bet...")
                break

            if toss == 1:
                stack += 1
                win += 1
            else:
                stack -= 1
                loss += 1
            
            no_of_bet -= 1
        
        if no_of_bet == 0 and stack > goal:
            print("You loss the bet... your stack is :", stack, "total try :", total_try)

        if no_of_bet == 0 and stack < goal:
            print("You didnt reached your goal, your stack is :", stack, "total try :", total_try)

if __name__ == '__main__':
    gambler_game = Gambler()
    gambler_game.gamble(10, 13, 10)
    


        
