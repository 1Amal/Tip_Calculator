# Created by Amal Kariyawasam from Melbourne, Australia on 30/04/2022 :-)
# I love coding and doing this to learn and improve my coding skills !
# Description of program: Simple tip calculator

#Start of code
print("Good day, welcome to Amal's simple tip calculator !")
billAmount=float(input("Please enter the bill amount $")) # Code to capture bill amount
numberOfPeople=int(input("Please enter number of people to share the bill with:")) # Code to capture number of people
tipPercentage=(float(input("Please enter the tip percentage:")))/100 # Code to capture tip percentage
totalTip=billAmount * tipPercentage # Code to calculate the total tip
finalBill=round(billAmount+totalTip, 2) # Code to calculate the final bill
indvidualBill=round(finalBill/numberOfPeople,2) # Code to calculate the individual bill

print(f"Based on bill amount of ${billAmount}, between {numberOfPeople} number of people, tip percentage of {tipPercentage*100}%, it is estimated that a final bill of ${finalBill}, hence each person will have to pay ${indvidualBill}")
input("Press enter to exit this program")
#End of code