
class HumanPlayer():

    def readInputIn(self):
        rawInput = input("Whats your new guessed combination? ")
        processedInput = [int(x) for x in rawInput.split()]
        #print(rawInput +" "+ str(processedInput))
        return processedInput