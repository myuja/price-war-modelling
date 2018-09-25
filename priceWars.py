################################################
#
#   name: Michael Yuja & Marios Lykiardopoulos
#   
#   assignment: Modelling price wars
#   
#   course: Modelling and Simulation Semester 1a 2018
#
#   email: m.j.yuja.matute@student.rug.nl
#          m.p.lykiardopoulos@student.rug.nl
################################################

import time

#Initiliatize the variables

#Assign a starting capital for each company

class Enterprise:
    starting_Capital = 100
    operating_Profit = []
    operating_Expenses = 15

def main():
    enterpriseA = Enterprise()
    enterpriseB = Enterprise()

    rounds = 12

    bothHighPrices = [10, 10]
    enterpriseALowPrice = [20,0]
    enterpriseBLowPrice = [0,20]
    bothLowPrice = [5,5]
    payoff_Matrix = [bothHighPrices,enterpriseALowPrice,enterpriseBLowPrice,bothLowPrice]
    current_Round = 1

    while current_Round <= rounds:
        #Check if either firm has enough capital to continue
        if enterpriseA.starting_Capital < 0:
            print("Firm A has gone bankrupt")

        if enterpriseB.starting_Capital < 0:
            print("Firm B has gone bankrupt")
            break

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
        enterpriseB.starting_Capital -= enterpriseA.operating_Expenses
        print("Firm A spends " + str(enterpriseA.operating_Expenses) + ' in operating expenses.')
        print("Firm B spends " + str(enterpriseB.operating_Expenses) + ' in operating expenses.')

        
        print("Firm A chose to set a " + choiceA)
        print("Firm B chose to set a " + choiceB)


        #Evaluate all the cases based on firm choices
        if choiceA == "lowPrice" and choiceB == "lowPrice":
            enterpriseA.operating_Profit += [bothLowPrice[0]]
            enterpriseB.operating_Profit += [bothLowPrice[1]]
            enterpriseA.starting_Capital += bothLowPrice[0]
            enterpriseB.starting_Capital += bothLowPrice[1]
        if choiceA == "lowPrice" and choiceB == "highPrice":
            enterpriseA.starting_Capital += enterpriseALowPrice[0]
            enterpriseB.starting_Capital += enterpriseALowPrice[1]
        if choiceA == "highPrice" and choiceB == "lowPrice":
            enterpriseA.starting_Capital += enterpriseBLowPrice[0]
            enterpriseB.starting_Capital += enterpriseBLowPrice[1]
        if choiceA == "highPrice" and choiceB == "highPrice":
            enterpriseA.starting_Capital += bothHighPrice[0]
            enterpriseB.starting_Capital += bothHighPrice[1]
            
        print("Firm A now has " + str(enterpriseA.starting_Capital) + " in capital")
        print("Firm B now has " + str(enterpriseB.starting_Capital) + " in capital")


        print("-------------------------\n")
        
        current_Round += 1

"""
def getTimeFormatted(seconds):
	m, s = divmod(seconds, 60)
	return "%02d:%02d" % (m, s)

    """
if __name__ == '__main__':
    main()

