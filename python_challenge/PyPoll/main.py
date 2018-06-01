
import pandas as pd
import glob

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
            while file_number > len(file_list):
               file_number = input(int("Select a number between the list: 0-", len(file_list)))
            break
        except ValueError:
            print("OOPS. That number is not on the list! Try again: ")
    return file_number

def getData(data_file):
    data_file = pd.read_csv(data_file)

    return data_file



file_list = getFileList()
list_number = getListNumber(len(file_list))
file_path =(file_list[list_number -1])

df = getData(file_path)

candidate_names = list(df["Candidate"].unique())
vote_counts = list(df["Candidate"].value_counts())
percents = list(df["Candidate"].value_counts(1))
winning_votes = 0
winner = ''
total_votes =df["Candidate"].count()

print("Election Results\n")
print("*****************************************")
print("Total Votes: ", total_votes)
print("*****************************************")
for i in range(len(vote_counts)):
    print(candidate_names[i], '{:.1%}'.format(percents[i]) ,vote_counts[i])
    if vote_counts[i] > winning_votes:
        winning_votes = vote_counts[i]
        winner = candidate_names[i]
print("*****************************************")
print("WINNER: ", winner)
print("*****************************************")       

myFile = open('Election_Results.txt', 'a')
myFile.write('\n**************************\n')
for i in range(len(vote_counts)):
    myFile.write(candidate_names[i] + str(' {:.1%}'.format(percents[i])) + '- Total Votes ' + str(vote_counts[i]) +'\n')
myFile.write("\nTotal Votes: " + str(total_votes))
myFile.write("\nWinning Votes: " + str(winning_votes))
myFile.write("\nWinner: " + str(winner))



myFile.close()

