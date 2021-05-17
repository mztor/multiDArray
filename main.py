import random

def loadData():
    f = open("3DArrayData.csv","w")
    f.write("Town,Month,Product,Sales Value\n")
    for i in range(1000):
        town = str(random.randint(0,5))
        month = str(random.randint(0,11))
        product = str(random.randint(0,3))
        sales = str(round(random.uniform(20.50,99.99),2))
        f.write(town + "," + month  + "," + product  + "," + sales + "\n")

    f.close()

def printFromArray():
#this is a stub that does not work yet
#convert the pseudocode from page 71 of the syllabus to print out
#the total sales for each town AND the grand total sales
    print(sales)

runLoadData = False #my flag that decides whether to run load data or not
if runLoadData:
    loadData()
else:
    f = open("3DArrayData.csv", "r")
    #set up the 3 dimensions of the array
    sales = []
    for town in range(6):
        sales.append([]) #make an array for each town
        for month in range(12):
            sales[town].append([]) #make an array for each month for the current town
            for product in range(4):
                sales[town][month].append([]) #make an array for each product for the current month in the current town

    #this section reads from the file into the array
    f.readline() #read the heading
    for line in f:
        data = line.split(",")
        town = int(data[0])
        month = int(data[1])
        product = int(data[2])
        print(town, month, product)
        sales[town][month][product] = float(data[3])

    f.close()
    printFromArray()

