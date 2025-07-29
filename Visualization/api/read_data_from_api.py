import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

#Requests current exchange rates for INR (Indian Rupee)
#Converts the JSON response into a Python dictionary
url="https://open.er-api.com/v6/latest/INR"
response=requests.get(url)
data= response.json()


#Checks if the response was successful. If not, stops execution with an error
if data['result']!='success':
    raise  Exception('API call failed')


#Extract Metadata from Response
timestamp=data['time_last_update_unix']
base_currency=data['base_code']
rates=data['rates']


#Selects 5 major currencies
#Converts from foreign currency → INR using reciprocal of the exchange rate
#For example: If 1 INR = 0.012 USD, then 1 USD ≈ 83.33 INR
major_currencies=['USD','EUR','GBP','JPY','AUD']
inr_per_currency={}

for currency in major_currencies:
    if(currency in rates and rates[currency]!=0):
        inr_per_currency[currency]=round(1/rates[currency],2)
        

#Converts UNIX timestamp to a standard date–time format in UTC
updated_at=datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


#Converts the exchange rates dictionary into a structured table
#Adds metadata 4 columns
df=pd.DataFrame(list(inr_per_currency.items()),columns=['Currency','Inr_Equivalent'])
df['Base_Currency']=base_currency
df['Updated_At']=updated_at


#Shows the exchange rates in INR for each selected currency
print(df)


#Visualize with Bar Chart
plt.figure(figsize=(10,2))
plt.bar(df['Currency'],df['Inr_Equivalent'],color='pink')
plt.title('Indian Value of Major Currencies')
plt.xlabel("Currency")
plt.ylabel("Value in INR")
plt.grid(axis='y',linestyle='--',alpha=0.8)  #grid lines visibility
plt.tight_layout()
plt.show()