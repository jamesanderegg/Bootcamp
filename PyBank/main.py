
import csv
import glob

number_months = 0
total_revenue = 0
greatest_decrease = 0
greatest_increase = 0
greatestDate = 0
decreaseDate = 0
total_average = 0
temp = 0

def getData(dataPath):
    with open(dataPath, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data = list(reader)

        return data
def convertInts(i, data):
    data[i][1] = int(data[i][1])

def addRevenue(i, data, total_revenue):
    total_revenue = data[i][1] + total_revenue
    return total_revenue

def greatestIncrease(temp, greatest_increase, i, date):
    if temp > greatest_increase:
        greatest_increase = temp
        date = i   
    return greatest_increase, date
def greatestDecrease(temp, greatest_decrease, i ,date):
    if temp < greatest_decrease:
        greatest_decrease = temp 
        date = i   
    return greatest_decrease, date
def getFileList():
    fileList = []

    for name in glob.glob('raw/*'):
        fileList.append(name)
    for i in range(len(fileList)):
        print(i+1,':' ,fileList[i])
    return fileList

def getListNumber(length):
    while True:     
        try:
            file_number = int(input("\nPlease select the file from the list. ENTER NUMBER:  "))
            print('\n')
            while file_number > len(fileList):
               file_number = input(int("Select a number between the list: 0-", len(fileList)))
            break
        except ValueError:
            print("OOPS. That number is not on the list! Try again: ")
    return file_number
def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")  


still_working = True


while still_working == True:  
    print("\nLet's start at the beginning.\n")
   
    fileList = getFileList()
    list_number = getListNumber(len(fileList))
    _path =(fileList[list_number -1])
    data = getData(_path)
    for i in range(len(data)):
        convertInts(i,data)
    for i in range(len(data)):
        total_revenue = addRevenue(i, data, total_revenue)
        
        if i == 0:
           
            total_average = data[i][1]
            
            total_average = temp
            
        else:   
            
            
            temp = data[i][1] - temp
            total_average = temp + total_average
            greatest_increase, greatestDate = greatestIncrease(temp, greatest_increase, i, greatestDate)
            greatest_decrease, decreaseDate = greatestDecrease(temp, greatest_decrease, i , decreaseDate)
           
            temp = data[i][1]
           
            
    print("\n***************************************")
    print('Finacial Analysis    \nFILE: ' + _path)
    print('\n***************************************')
    print("Total Months: ", len(data))
    print ("Total Revenue: $", total_revenue)
    print ("Average Revenue Change: $", total_average/len(data))
    print ("Greatest Increase: $" , data[greatestDate][0], greatest_increase)
    print ("Greatest Decrease: $", data[decreaseDate][0], greatest_decrease) 
    print("\n***************************************")
    
    
    myFile = open('final_budget_1.txt', 'a')
    myFile.write('\n***************************************\n')
    myFile.write ('\nFinacial Analysis    \nFILE: ' + _path)
    myFile.write('Finacial Analysis')
    myFile.write('\n***************************************\n')
    myFile.write("\nTotal Months: " + str(len(data)))
    myFile.write ("\nTotal Revenue: $" + str(total_revenue))
    myFile.write ("\nAverage Revenue Change: $" + str(total_average/len(data)))
    myFile.write ("\nGreatest Increase: " + str(data[greatestDate][0]) +' $' +str(greatest_increase))
    myFile.write ("\nGreatest Decrease: "+ str(data[decreaseDate][0]) +' $'+str(greatest_decrease))
    myFile.write('\n\n***************************************\n\n')
    myFile.close()
    
    still_working = yes_or_no("Would you like to load another file?")


