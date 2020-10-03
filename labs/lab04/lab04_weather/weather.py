import datetime
import csv

def weather(date, location):
    if date.strip() == '' or location.strip() == '':
        return (None, None)
    
    try:
        date = datetime.datetime.strptime(date, "%d-%m-%Y").strftime("%Y-%m-%d")
    except ValueError:
        pass

    with open('weatherAUS.csv', 'r') as file_object:
        reader = csv.DictReader(file_object)
        lines = [line for line in reader]

    dates = set([line['Date'] for line in lines])
    locations = set([line['Location'] for line in lines])

    if date not in dates or location not in locations:
        return (None, None)

    MinTemps = []
    MaxTemps = []

    for line in lines:
        if line['Location'] == location and line['MaxTemp'] != 'NA' and line['MinTemp'] != 'NA':
            MinTemps.append(float(line['MinTemp']))
            MaxTemps.append(float(line['MaxTemp']))

    avgMinTemp = round(sum(MinTemps)/len(MinTemps), 1)
    avgMaxTemp = round(sum(MaxTemps)/len(MinTemps), 1)

    for line in lines:
        if line['Date'] == date and line['Location'] == location:
            return (round(avgMinTemp - float(line['MinTemp']), 1), round(avgMaxTemp - float(line['MaxTemp']), 1))
    
    return (None, None)

