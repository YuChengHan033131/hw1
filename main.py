import csv
dict={'C0A880':-1, 'C0F9A0':-1, 'C0G640':-1, 'C0R190':-1, 'C0X260':-1}
with open("107033131.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        if row['station_id'] in dict:
            if float(dict[row['station_id']])>float(row['TEMP']):
                continue
            dict[row['station_id']]=row['TEMP']
print("[",end=''),
count=0
for key in sorted(dict):
    if count==0:
        print("['",end='',sep='')
        count+=1
    else:
        print(", ['",end='',sep='')
    if float(dict[key])<0:
        print(key,"', 'None']",end='',sep='')
    else:
        print(key,"', ",float(dict[key]),"]",end='',sep='')
print("]")
