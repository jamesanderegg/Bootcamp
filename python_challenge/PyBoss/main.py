import pandas as pd
import glob
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
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
def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")
def getData(data_file):
        data_file = pd.read_csv(data_file)

        return data_file

still_working = True


while still_working == True:  
    

    file_list = getFileList()
    list_number = getListNumber(len(file_list))
    file_path =(file_list[list_number -1])
    df = getData(file_path)

    df['First Name'],df['Last Name'] = df['Name'].str.split().str
    df['1'],df['2'],df['SSN'] = df['SSN'].str.split('-').str
    df =df.drop(columns =['Name', '1', '2'])
    df['SSN'] = '***-**-' + df['SSN'].astype(str)
    df['DOB'] = pd.to_datetime(df.DOB)
    df['DOB'] = df['DOB'].dt.strftime('%m/%d/%Y')
    
    df['State'] = df['State'].map(us_state_abbrev)
    cleaned_data= df[['Emp ID', 'First Name','Last Name','DOB','SSN','State']]
    
    print(cleaned_data.head(10))

    still_working = yes_or_no("Would you like to load another file?")
