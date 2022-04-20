import json
from genericpath import exists
from random import randrange

def manipulateDataFile(handleJson):
    with open('data.json', 'r+') as f:
        data = handleJson(json.load(f))
        f.seek(0)        
        json.dump(data, f, indent=4)
        f.truncate()     

while True:
    
    if exists('data.json'):
        def startGame(data):
            print(f"Welcome! You've played {data['gamesPlayed']}, won {data['timesWon']} times and lost {data['timesLost']} times.")
            data['gamesPlayed'] += 1 
            return data
        manipulateDataFile(startGame)

    else :
        aDict = {"gamesPlayed":1, "timesWon":0 , "timesLost": 0}
        jsonString = json.dumps(aDict,indent=4)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        
    numsRange = range(1,101)
    tries = 10
    randomValue = randrange(1,101)
    previusValues = []

    while tries:
        print(f"You have now {tries} tries")
        try:
            enteredValue = int(input(f"Please guess value between ({numsRange.start}-{numsRange.stop - 1}): "))
        except:
            print("Enter a valid int")
            continue
        
        if enteredValue not in numsRange:
            print("Value is out of range")
            continue
        
        if enteredValue in previusValues:
            print(f"You entered {enteredValue} before, try another.")
            continue
        
        if enteredValue == randomValue:
            print("You Won!")
            previusValues = []
            def winGame(data):
                data['timesWon'] += 1 
                return data
            manipulateDataFile(winGame)
            randomValue = randrange(1,101)
            print("Now guess the new number.")
            continue
        
        elif enteredValue > randomValue:
            print("Lower your number.")
            
        else:
            print("Raise your number.")
            
        previusValues.append(enteredValue)
        tries -= 1
    
    def loseGame(data):
        data['timesLost'] += 1
        return data
    
    manipulateDataFile(loseGame)
    choice = input("You lost! type 'y' to play again: ")
    if choice != "y":
        break
    
        
        

        
