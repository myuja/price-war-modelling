######################################################
#
#   name: Michael Yuja & Marios Lykiardopoulos
#   
#   assignment: Modelling price wars
#   
#   course: Modelling and Simulation Semester 1a 2018
#
#   email: m.j.yuja.matute@student.rug.nl
#          m.p.lykiardopoulos@student.rug.nl
######################################################

import time
import matplotlib.pyplot as plt

#Initiliatize the variables

#Assign a starting capital for each company

class Enterprise:
    starting_Capital = 100
    market_Share = 0.5
    operating_Profit = []
    operating_Expenses = 10
    bankrupt = False

def main():
    #Initialize enterprises with desired parameters
    enterpriseA = Enterprise()
    enterpriseB = Enterprise()
    enterpriseB.operating_Expenses = 20
    rounds = 12

    #Initialize the payoff matrix
    bothHighPrices = [10, 10]
    enterpriseALowPrice = [20,0]
    enterpriseBLowPrice = [0,20]
    bothLowPrice = [5,5]

    #Initialize variables for looping and storing data
    current_Round = 0
    enterpriseACap = []
    enterpriseBCap = []

    #Begin the game
    while current_Round < rounds:
        #Check if either firm has enough capital to continue
        if enterpriseA.starting_Capital<= 0 and enterpriseA.bankrupt == False:
            enterpriseA.bankrupt = True
            rounds = current_Round
            print("Firm A has gone bankrupt. Firm B wins.\n")
            break

        if enterpriseB.starting_Capital <= 0 and enterpriseB.bankrupt == False:
            enterpriseB.bankrupt = True
            rounds = current_Round
            print("Firm B has gone bankrupt. Firm A wins.\n")
            break

        if enterpriseA.bankrupt == True and enterpriseB.bankrupt == True:
            rounds = current_Round
            print("Both firms are bankrupt. The game has ended.")
            break

        enterpriseACap += [enterpriseA.starting_Capital]
        enterpriseBCap += [enterpriseB.starting_Capital]
        
        #Objective of the game is for each firm to maximize payoff
        lowPricePayOffA = enterpriseALowPrice[0] + bothLowPrice[0]
        lowPricePayOffB = enterpriseBLowPrice[1] + bothLowPrice[1]
        highPricePayOffA = bothHighPrices[0] + enterpriseBLowPrice[0]
        highPricePayOffB = bothHighPrices[1] + enterpriseALowPrice[1]

        if lowPricePayOffA > highPricePayOffA:
            choiceA = "lowPrice"
        else:
            choiceA = "highPrice"

        if lowPricePayOffB > highPricePayOffB:
            choiceB = "lowPrice"
        else:
            choiceB = "highPrice"

        print("Round: " + str(current_Round))
        print("Firm A starts with " + str(enterpriseA.starting_Capital) + ' in capital')
        print("Firm B starts with " + str(enterpriseB.starting_Capital) + ' in capital')

        #Sutract the firm's operating expenses from the starting capital
        enterpriseA.starting_Capital -= enterpriseA.operating_Expenses
        enterpriseB.starting_Capital -= enterpriseB.operating_Expenses
        print("Firm A spends " + str(enterpriseA.operating_Expenses) + ' in operating expenses.')
        print("Firm B spends " + str(enterpriseB.operating_Expenses) + ' in operating expenses.')

        print("Firm A chose to set a " + choiceA)
        print("Firm B chose to set a " + choiceB)


        #Evaluate all the cases based on firm choices
        if choiceA == "lowPrice" and choiceB == "lowPrice":
            enterpriseA.starting_Capital += bothLowPrice[0]
            enterpriseB.starting_Capital += bothLowPrice[1]
        if choiceA == "lowPrice" and choiceB == "highPrice":
            enterpriseA.starting_Capital += enterpriseALowPrice[0]
            enterpriseB.starting_Capital += enterpriseALowPrice[1]
        if choiceA == "highPrice" and choiceB == "lowPrice":
            enterpriseA.starting_Capital += enterpriseBLowPrice[0]
            enterpriseB.starting_Capital += enterpriseBLowPrice[1]
        if choiceA == "highPrice" and choiceB == "highPrice":
            enterpriseA.starting_Capital += bothHighPrices[0]
            enterpriseB.starting_Capital += bothHighPrices[1]
            
        print("Firm A now has " + str(enterpriseA.starting_Capital) + " in capital")
        print("Firm B now has " + str(enterpriseB.starting_Capital) + " in capital")

        print("-------------------------\n")
        
        current_Round += 1
    
    plot(rounds, enterpriseACap, enterpriseBCap)

"""
def getTimeFormatted(seconds):
	m, s = divmod(seconds, 60)
	return "%02d:%02d" % (m, s)

    """
    
def plot(rounds, enterpriseACap, enterpriseBCap):
    # x axis values 
    x = [x for x in range(1, rounds + 1)]
    # corresponding y axis values 
    y1 = enterpriseACap
    y2 = enterpriseBCap

    # plotting the points  
    plt.plot(x, y1, label = "Enterprise A")
    
    # plotting the points  
    plt.plot(x, y2, label = "Enterprise B")  
    
    # naming the x axis 
    plt.xlabel('Round') 
    # naming the y axis 
    plt.ylabel('Capital') 
    
    # giving a title to my graph 
    plt.title('Capital of two firms in a price war') 
    
    # show a legend on the plot 
    plt.legend() 

    # function to show the plot 
    plt.show() 
    
  


if __name__ == '__main__':
    main()

