import re


def find_sum(arr):
    s = 0
    for num in arr:
        s += int(num)
    return s


file = open('files/actual.txt', 'r')

all_numbers = list()
for line in file:
    numbers = re.findall('[0-9]+', line)
    all_numbers += numbers

print('Total numbers found:', len(all_numbers))
print('Sum:', find_sum(all_numbers))
