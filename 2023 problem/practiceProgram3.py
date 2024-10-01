#500




def fetchInput():
    data = input(f"Enter in the value here\n")
    return data

def numOfGames():
    print(f"How many games did you play?")
    n = fetchInput()
    return int(n)

def results(n):
    scoreboard = {}
    ticks = 1
    total = 0
    while ticks <= n:
        score, name = input(f"Enter in the value here\n").split()
        scoreboard.update({name:score})
        if name in scoreboard:
            total += int(score)
            scoreboard.update({name:score})
        ticks += 1
    print(scoreboard)

def game():
    n = numOfGames()
    results(n)



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