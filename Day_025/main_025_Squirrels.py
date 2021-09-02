import pandas

colors = ['Gray', 'Cinnamon', 'Black']
new_table = {'Colors': list(), 'Count': list()}
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color = data['Primary Fur Color']

for color in colors:
    new_table['Colors'].append(color)
    new_table['Count'].append(len(data[fur_color == color]))

new = pandas.DataFrame(new_table)
print(new)
