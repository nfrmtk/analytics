import csv
def csv_read():
    path = input()
    arr = input().split(' ')
    x = int(arr[0])
    y = int(arr[1])
    file = open(path)
    data = csv.reader(file, delimiter=',')
    # data[x][y]
    for row in data:
        if data.line_num == x :
            print(row[y])


    


csv_read()
# s = open('data.csv')

# print(csv.load(s)[2][2])
