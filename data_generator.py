import string
import random
import csv

client_fields = ['clientId','clientName','clientType','rate','location','industry','holding','scale','maturity']
train_fields = ['clientId','clientName','clientType','rate','location','industry','holding','scale','maturity',
      #  't_amt','month',
        'loan','deposits','pension','credit','mortage','report','asset','investment','plan','consulting']

client_type_options = string.ascii_uppercase[:10]
client_rate_options = ['AAAA','AAA','AA','A','BBBB','BBB','BB','B','C']
location_options = ['US','CN','TT','SD','HK','RU','EU','IR','AP']
industry_options = ['IAT','SEV','MKT','ENG','LPG','TTT']
scale_options = ['S','XS','M','L','XL','XXL']
maturity_options = ['M01','M02','M03','M04','M05','M06','M07','M08','M09','M10']

client_data = []
train_data = []

for i in range(100):
    row = {
        client_fields[0]:'C' + str(i+1).zfill(3),
        client_fields[1]:'C' + str(i+1).zfill(3) + " Name",
        client_fields[2]:random.choice(client_type_options),
        client_fields[3]:random.choice(client_rate_options),
        client_fields[4]: random.choice(location_options),
        client_fields[5]: random.choice(industry_options),
        client_fields[6]: random.randrange(100000, 20000000),
        client_fields[7]: random.choice(scale_options),
        client_fields[8]: random.choice(maturity_options)
    }
    client_data.append(row)

for i in range(1000):
    row = {
        train_fields[0]:'C' + str(i+1).zfill(3),
        train_fields[1]:'C' + str(i+1).zfill(3) + " Name",
        train_fields[2]:random.choice(client_type_options),
        train_fields[3]:random.choice(client_rate_options),
        train_fields[4]: random.choice(location_options),
        train_fields[5]: random.choice(industry_options),
        train_fields[6]: random.randrange(100000, 20000000),
        train_fields[7]: random.choice(scale_options),
        train_fields[8]: random.choice(maturity_options),
        train_fields[9]: random.randint(0, 1),
        train_fields[10]: random.randint(0, 1),
        train_fields[11]: random.randint(0, 1),
        train_fields[12]: random.randint(0, 1),
        train_fields[13]: random.randint(0, 1),
        train_fields[14]: random.randint(0, 1),
        train_fields[15]: random.randint(0, 1),
        train_fields[16]: random.randint(0, 1),
        train_fields[17]: random.randint(0, 1),
        train_fields[18]: random.randint(0, 1)
    }
    train_data.append(row)

with open('client.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=client_fields)
    writer.writeheader()
    for row in client_data:
        writer.writerow(row)

with open('train_data.csv','w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=train_fields)
    writer.writeheader()
    for row in train_data:
        writer.writerow(row)
