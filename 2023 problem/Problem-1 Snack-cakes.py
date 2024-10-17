#Problem 1
def userInput():
    answer = []
    y = input(f"Enter value here\n")
    for each in y.split():
        answer.append(each)
    return answer

def problem1():
    text = {1: "You will enjoy our delicious [] snack cakes!", 2: "Goritos: taste the XYZZY", 3: "No one does na-flavored chips as well as Yummy TreatCo", 4:"Gimme a @ !"}
    choice = int(input("How many Templates you want?"))
    if choice == 4:
        template1(text[1])
        template2(text[2])
        template3(text[3])
        template4(text[4])
        
        #return dictionary
def template1(text):
    dictionary = []
    answer = userInput()
    for words in text.split():
        dictionary.append(words)
    i = dictionary.index("[]")
    for each in answer:
        print(each)
        dictionary[i] = each
        text = " ".join(dictionary) 
        display(text)

def template2(text):
    dictionary = []
    answer = userInput()
    for words in text.split():
        dictionary.append(words)
    i = dictionary.index("XYZZY")
    for each in answer:
        print(each)
        dictionary[i] = each
        text = " ".join(dictionary) 
        display(text)

def template3(text):
    dictionary = []
    answer = userInput()
    for words in text.split():
        dictionary.append(words)
    i = dictionary.index("na-flavored")
    for each in answer:
        each += "-flavored"
        dictionary[i] = each
        text = " ".join(dictionary) 
        display(text)

def template4(text):
    dictionary = []
    answer = userInput()
    for words in text.split():
        dictionary.append(words)
    i = dictionary.index("@")
    for each in answer:
        dictionary[i] = each
        text = " ".join(dictionary) 
        display(text)

def display(text):
    print(text, text)
    
def main():
    while True:
        try:
            problem1()
            repeat = input("Would you like to try this again?(Y|N)").upper() #WILL AUTOMATICALLY MAKE EVERY REPLY TO THIS CAPITALIZE
            if repeat != 'Y':   
                break
       # except ValueError:
            print("ValueError")
        except ZeroDivisionError:
            print("ZeroDivisionError") 


main()