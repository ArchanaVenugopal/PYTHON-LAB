import csv
fields=['Programming language', 'Designed by', 'Appeared', 'Extension']
rows=[['Python', 'Guido van Rossum', '1991', '.py']
     ['Java', 'James Gosling', '1995', '.java']
     ['C++', 'Bjarne Stroustrup', '1983', '.cpp']]
filename="data.csv"

with open('data.csv','r')as csvfile :
  data = csv.reader(csvfile)
  for row in data:
        print(row)