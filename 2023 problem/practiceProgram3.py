#500




def fetchInput():
    data = input(f"Enter in the value here\n")
    return data

def numOfGames():
    print(f"How many games did you play?")
    n = fetchInput()
    return int(n)

def scoreboardResults(n):
    scoreboard = {}
    ticks = 1
    while ticks <= n:
        score, name = input(f"Enter in the value here\n").split()
        if score == "JACKPOT":
            score = "0"
            score = int(score)         
            score += 500
        elif score == "BANKRUPT":
            score = 0
        if name in scoreboard:
            scoreboard[name] += score
        else:
            scoreboard[name] = score
        ticks += 1

    #print(max(scoreboard, key=scoreboard.get))




def game():
    n = numOfGames()
    scoreboard = scoreboardResults(n)


def main():
    while True:
        game()
        try:
            repeat = input("Would you like to continue?").upper()
            if repeat != "Y":
                break
        except ValueError:
            print("ValueError")
        except ZeroDivisionError:
            print("ZeroDivisionError")
        except IOError:
            print("IOError")
            
main()