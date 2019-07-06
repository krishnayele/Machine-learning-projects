import csv
f= open('csvFileDemo.csv','w',newline='') 
'''
theeditor = csv.writer(f)

theeditor.writerow(['col1','col2'])

for i in range(1,15):
    theeditor.writerow(['m','y','s'])
'''
# another apraoch

_fieldnames = ['column1','column2','column3']
theeditor = csv.DictWriter(f, fieldnames=_fieldnames)

theeditor.writeheader()
theeditor.writerow({'column1':'Krish','column3':'smart','column2':'is'})# order does not matter
