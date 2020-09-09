'''
27/04/2020

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

'''


with open('problem22.txt') as file:
    for line in file:
        name_list = [name.strip('"') for name in line.split(',')]

name_list.sort()

name_sum = 0
total_sum = 0

for index in range(len(name_list)):
    for character in name_list[index]:
        # ord() returns the ascii value of the character
        # A = 65, B = 66, ... , Z = 90
        name_sum += ord(character) - 64
    total_sum += name_sum * (index+1)
    name_sum = 0 # DON'T FORGET TO RESET NAME_SUM YOU DONKEY (spent ~30 mins 'bugfixing')

print(total_sum)