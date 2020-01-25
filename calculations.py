import matplotlib.pyplot as plt
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#base prices
price = [6.95, 10, 19, 28, 36, 70, 137]

#base amounts
amount = [2, 6, 12, 18, 24, 50, 100]

#3 free cookie deal
for i in amount:
    amount[amount.index(i)]=i+3

#sales tax
for i in price:
    price[price.index(i)]=i*1.0625
    
#shipping    
for i in price:
    price[price.index(i)]=i+2.99

avg_price = []
#calculating average price
for i in amount:
    x = amount.index(i)
    avg_price.append(price[x]/i)

#setting up graph
plt.scatter(amount,avg_price)

for x,y in zip(amount,avg_price):
    label = str(x)
    
    plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,5), ha='center')

plt.ylabel('average price per cookie ($)')
plt.xlabel('# of cookies (preferably snickerdoodles)')
plt.title('Insomnia Cookie price efficency for each bundle')
plt.suptitle('Including 6.5% sales tax, shipping, and the 3 free cookie deal')
plt.show()