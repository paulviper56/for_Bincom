import csv
from bs4 import BeautifulSoup
green_score=0
yellow_score=0
blue_score=0
brown_score=0
orange_score=0
cream_score=0
white_score=0
pink_score=0
red_score=0

my_list = []
with open('python_class_question (1).html', 'r') as file:
    my_doc = BeautifulSoup(file, 'html.parser')
    
doc_tds1 = my_doc.find_all('td')[1]
doc_tds2 = my_doc.find_all('td')[3]
doc_tds3 = my_doc.find_all('td')[5]
doc_tds4 = my_doc.find_all('td')[7]
doc_tds5 = my_doc.find_all('td')[9]


day1 = csv.reader(doc_tds1)
day2 = csv.reader(doc_tds1)
day3 = csv.reader(doc_tds1)
day4 = csv.reader(doc_tds1)
day5 = csv.reader(doc_tds1)

my_list = []
new_list = []
for row in day1:
    my_list.append(row)
    
for row in day2:
    my_list.append(row)
    
for row in day3:
    my_list.append(row)
    
for row in day4:
    my_list.append(row)
    
for row in day5:
    my_list.append(row)
    
    
for colors in my_list[0]:
    new_list.append(colors)
for colors in my_list[1]:
    new_list.append(colors)
for colors in my_list[2]:
    new_list.append(colors)
    
for colors in my_list[3]:
    new_list.append(colors)
for colors in my_list[4]:
    new_list.append(colors)
print(new_list)
    
for color in new_list:
    print(color)
    if color == 'GREEN' or color == ' GREEN':
        green_score +=1
    elif color == 'YELLOW' or color == ' YELLOW':
        yellow_score +=1
    elif color == 'BLUE' or color == ' BLUE':
        blue_score +=1
    elif color == 'BROWN' or color == ' BROWN':
        brown_score +=1
    elif color == 'ORANGE' or color == ' ORANGE':
        orange_score +=1
    elif color == 'CREAM' or color == ' CREAM':
        cream_score +=1
    
    elif color == 'WHITE' or color == ' WHITE' :
        white_score +=1
    elif color == 'PINK' or color == ' PINK':
        pink_score +=1
    else:
        red_score +=1
scores = [green_score,yellow_score,blue_score,brown_score,orange_score,cream_score,white_score,pink_score,red_score]
mostly_worn_color = max(scores)
print(mostly_worn_color)
print(green_score)
print(blue_score)
print(yellow_score)
  
# blue_score is the max, which implies that color BLUE is the mostly worn color throughout the week
sorted_color_list = sorted(new_list)
print(sorted_color_list)
length_of_sorted_color_list = len(sorted_color_list)
print(length_of_sorted_color_list)
#since the length of the sorted list is 95, which is an odd number, the median is N+1/2 = 95+1/2 = 48
start = True
count_color = 0
while start:
    for color in sorted_color_list:
        count_color +=1
        if count_color ==48:
            print(f"the median is {color}")
            start=False
# To get the mean we have to divide the total length of the sorted list by the number of days which is 5
mean = length_of_sorted_color_list/5

start = True
count_color =0
while start:
    for color in sorted_color_list:
        count_color +=1
        if count_color == mean:
            print(f"the mean color is {color}")
            start=False
    

    

