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
from random import seed
from random import random

#Initiliatize the variables

#Assign a starting capital for each company

class Enterprise:
    starting_Capital = 100
    market_Share = 50
    operating_Expenses = 10
    strategies = []
    choices = []
    bankrupt = False

def main():
    #Initialize enterprises with desired parameters
    rounds = 12
    enterpriseA = Enterprise()
    enterpriseB = Enterprise()
    enterpriseA.choices = ["None"]
    enterpriseB.choices = ["None"]

    #Seed for the pseudo-random generator to be used in initializing the strategy
    seed(100)

    #Initialize variables for looping and storing data
    current_Round = 0
    enterpriseACap = []
    enterpriseBCap = []

    #Begin the game
    while current_Round < rounds:

        #Initialize the payoff matrix
        #The payoff matrix changes if there has been a change in market share
        #The values are multiplied by the market share 
        bothHighPrices = [10 * enterpriseA.market_Share/100, 10 * enterpriseB.market_Share/100]
        enterpriseALowPrice = [20 * enterpriseA.market_Share/100, 0 * enterpriseB.market_Share/100]
        enterpriseBLowPrice = [0 * enterpriseA.market_Share/100, 20 * enterpriseB.market_Share/100]
        bothLowPrice = [5 * enterpriseA.market_Share/100, 5 * enterpriseB.market_Share/100]

        #Check if either firm has enough capital to continue
        if enterpriseA.starting_Capital<= enterpriseA.operating_Expenses and enterpriseA.bankrupt == False:
            enterpriseA.bankrupt = True
            rounds = current_Round
            print("Firm A can't cover its operating expenses for the next round. Firm B wins.\n")
            break

        if enterpriseB.starting_Capital <= enterpriseA.operating_Expenses and enterpriseB.bankrupt == False:
            enterpriseB.bankrupt = True
            rounds = current_Round
            print("Firm B can't cover its operating expenses for the next round. Firm A wins.\n")
            break

        if enterpriseA.bankrupt == True and enterpriseB.bankrupt == True:
            rounds = current_Round
            print("Both firms are bankrupt. The game has ended.")
            break

        #These lists keep track of all the starting capitals for plotting
        enterpriseACap += [enterpriseA.starting_Capital]
        enterpriseBCap += [enterpriseB.starting_Capital]
        
        #Objective of the game is for each firm to maximize payoff
        lowPricePayOffA = enterpriseALowPrice[0] + bothLowPrice[0]
        lowPricePayOffB = enterpriseBLowPrice[1] + bothLowPrice[1]
        highPricePayOffA = bothHighPrices[0] + enterpriseBLowPrice[0]
        highPricePayOffB = bothHighPrices[1] + enterpriseALowPrice[1]

        if lowPricePayOffA > highPricePayOffA and current_Round > 0:
            enterpriseA.choices += ["lowPrice"]
        else:
            enterpriseA.choices += ["highPrice"]
        if lowPricePayOffB > highPricePayOffB and current_Round > 0:
            enterpriseB.choices += ["lowPrice"]
        else:
            enterpriseB.choices += ["highPrice"]

        #For the starting round, we assume that neither company knows the true market price
        #They are given equal probabilities to choose a low price or a high price
        if current_Round == 0:
            rand = [random(), random()]
            print(rand)
            enterpriseA.choices[0] = "lowPrice" if rand[0] < 0.50 else "highPrice"
            enterpriseB.choices[0] = "lowPrice" if rand[1] < 0.50 else "highPrice"

        print("Round: " + str(current_Round))
        print("Firm A starts with " + str(enterpriseA.starting_Capital) + ' in capital')
        print("Firm B starts with " + str(enterpriseB.starting_Capital) + ' in capital')

        #Sutract the firm's operating expenses from the starting capital
        enterpriseA.starting_Capital -= enterpriseA.operating_Expenses
        enterpriseB.starting_Capital -= enterpriseB.operating_Expenses
        print("Firm A spends " + str(enterpriseA.operating_Expenses) + ' in operating expenses.')
        print("Firm B spends " + str(enterpriseB.operating_Expenses) + ' in operating expenses.')

        print("Firm A chose to set a " + enterpriseA.choices[current_Round])
        print("Firm B chose to set a " + enterpriseB.choices[current_Round])


        #Evaluate all the cases based on firm choices
        #Reward or punish the choice in market share if opposite choices are made
        #Equal choices = market share stays the same
        if enterpriseA.choices[current_Round] == "lowPrice" and enterpriseB.choices[current_Round] == "lowPrice":
            enterpriseA.starting_Capital += bothLowPrice[0]
            enterpriseB.starting_Capital += bothLowPrice[1]
        if enterpriseA.choices[current_Round] == "lowPrice" and enterpriseB.choices[current_Round] == "highPrice":
            enterpriseA.starting_Capital += enterpriseALowPrice[0]
            enterpriseB.starting_Capital += enterpriseALowPrice[1]

            #Reward Firm A
            enterpriseA.market_Share += 10

            #Punish Firm B
            enterpriseB.market_Share -= 10
        if enterpriseA.choices[current_Round] == "highPrice" and enterpriseB.choices[current_Round] == "lowPrice":
            enterpriseA.starting_Capital += enterpriseBLowPrice[0]
            enterpriseB.starting_Capital += enterpriseBLowPrice[1]

            #Punish Firm A
            enterpriseA.market_Share -= 10
            
            #Reward Firm B
            enterpriseB.market_Share += 10

        if enterpriseA.choices[current_Round] == "highPrice" and enterpriseB.choices[current_Round] == "highPrice":
            enterpriseA.starting_Capital += bothHighPrices[0]
            enterpriseB.starting_Capital += bothHighPrices[1]
            

        print("Firm A now has " + str(enterpriseA.starting_Capital) + " in capital")
        print("Firm B now has " + str(enterpriseB.starting_Capital) + " in capital")

        

        print("Firm A now has " + str(enterpriseA.market_Share) + "% in market share")
        print("Firm B now has " + str(enterpriseB.market_Share) + "% in market share")
        print("-------------------------\n")


        current_Round += 1
    
    plot(rounds, enterpriseACap, enterpriseBCap)


def choose_Strategy():
    return None
    
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
    plt.title('Capital of Two Firms in a Price War') 
    
    # show a legend on the plot 
    plt.legend() 

    # function to show the plot 
    plt.show() 
    
  
if __name__ == '__main__':
    main()

