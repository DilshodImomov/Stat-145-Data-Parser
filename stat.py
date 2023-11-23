file = open("owid-covid-data.csv", "r")
lines = file.readlines()
file.close()

countries = dict()

for line in lines:
    line = line.strip().split(",")
    country = line[0]
    if country not in ["USA", "ITA", "RUS", "CAN"]:
        continue
    date = line[3].split("-")
    year = date[0]
    mon = int(date[1]) - 1
    if year != "2021":
        continue
    
    months = [0 for i in range(12)]
    if country in countries:
        months = countries[country]
    death = line[8].split('.')
    if len(death) >= 1:
        months[mon] += int(death[0])

    countries[country] = months

for country in countries.keys():
    print(country + ": ")
    for i in countries[country]:
        print(i, end = " ")
    print()    

output = open("output2.csv", "w")
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
cntries = ["USA", "CAN", "ITA", "RUS"]

output.write("Month,USA,CAN,ITA,RUS\n")

for i in range(12):
    s = months[i]
    for j in range(4):
        s += "," + str(countries[cntries[j]][i])
    s += '\n'
    output.write(s)

s = "Total"
for i in range(4):
    s += "," + str(sum(countries[cntries[i]]))
s += '\n'

output.write(s)
output.close()