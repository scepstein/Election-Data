#Create venv to operate in (code run in terminal)
cd 'New York City, NY 2024 - Unofficial Results'
python3 -m venv venv
source venv/bin/activate
pip install bs4
pip install pandas
pip install ipython
pip install requests

#Run iPython
ipython
#code below run in ipython environ

#Import Necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL containing the table with AD links
url = "https://enr.boenyc.gov/CD26825AD0.html"  

# Fetch the webpage
response = requests.get(url)
response.raise_for_status()

# Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table (update selector if necessary for your table)
table = soup.find_all('table')
table = table[2]

# Extract rows and columns
rows = table.find_all('tr')
data = []

for row in rows:
    cols = row.find_all(['td', 'th'])
    row_data = []
    for col in cols:
        # Check if there is an <a> tag and extract the href, otherwise get text
        link = col.find('a')
        if link:
            row_data.append(link['href'])  # Add the hyperlink
        else:
            row_data.append(col.get_text(strip=True))  # Add the cell text
    data.append(row_data)

# Create DataFrame
df = pd.DataFrame(data[1:], columns=data[0])  # First row as header

#Change Column Names
columns = list(df.columns)  # Get current column names as a list
columns[0] = 'URL'  
columns[1] = 'Reported'
columns[2] = 'HarrisWalz DEM'
columns[4] = 'TrumpVance GOP'
columns[6] = 'TrumpVance CON'
columns[8] = 'HarrisWalz WFP'  
columns[10] = 'WRITE IN'  
df.columns = columns

#Crop out extra rows and columns
df =df.iloc[1:len(df),:]
df=df.iloc[:, [0,1,2,4,6,8,10]]

#Complete URLs
df["URL"] = ["https://enr.boenyc.gov/"+ x for x in df["URL"]]
df =df.iloc[0:len(df)-1,:]

#Format
df["HarrisWalz DEM"] = df["HarrisWalz DEM"].astype(float)
df["HarrisWalz WFP"] = df["HarrisWalz WFP"].astype(float)
df["TrumpVance CON"] = df["TrumpVance CON"].astype(float)
df["TrumpVance GOP"] = df["TrumpVance GOP"].astype(float)
df.dtypes

df["HarrisWalz"] = df["HarrisWalz DEM"] + df["HarrisWalz WFP"]
df["TrumpVance"] = df["TrumpVance CON"] + df["TrumpVance GOP"]


#New Goal: Open every AD page and scrape the table

ED_data = []
for x in df["URL"]:

    ## Set the URL and fetch HTML
    url = x
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('table')
    table = table[2]

    #Extract Rows and Tables
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all(['td', 'th'])
        row_data = []
        for col in cols:
            row_data.append(col.get_text(strip=True))  # Add the cell text
        data.append(row_data)

    #Reformat Table
    df2 = pd.DataFrame(data[1:], columns=data[0]) #Convert to df
    columns = list(df2.columns)  # Get current column names as a list
    columns[0] = 'ED'  
    columns[1] = 'Reported'
    columns[3] = 'HarrisWalz DEM'
    columns[5] = 'TrumpVance GOP'
    columns[7] = 'TrumpVance CON'
    columns[9] = 'HarrisWalz WFP'  
    columns[11] = 'WRITE IN'  
    df2.columns = columns
    df2 =df2.iloc[1:len(df2),:]
    df2=df2.iloc[:, [0,1,3,5,7,9,11]]
    df2["HarrisWalz DEM"] = df2["HarrisWalz DEM"].astype(float)
    df2["HarrisWalz WFP"] = df2["HarrisWalz WFP"].astype(float)
    df2["TrumpVance CON"] = df2["TrumpVance CON"].astype(float)
    df2["TrumpVance GOP"] = df2["TrumpVance GOP"].astype(float)
    df2["HarrisWalz"] = df2["HarrisWalz DEM"] + df2["HarrisWalz WFP"]
    df2["TrumpVance"] = df2["TrumpVance CON"] + df2["TrumpVance GOP"]
    df2["ED"]= [y.replace(" ", "").replace("ED", "") if "ED" in y else y for y in df2["ED"]]
    df2["AD"]= x.split("https://enr.boenyc.gov/CD26825AD")[1].split("0.html")[0]

    #Combine with other EDs
    if len(ED_data) == 0:
        ED_data = df2
    else:
        ED_data = pd.concat([ED_data, df2])


#Save pandas to csv
ED_data.to_csv("precincts24.csv", index=False)
    


