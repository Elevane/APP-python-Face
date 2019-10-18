import csv

"""
the function getlines return the number of the last line to get the index of the file
"""


def getlines():
    i = 0
    with open('images/log.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1

            print(row)
        print(f'Processed {line_count // 2} lines.')

    return line_count // 2


"""
add function log the image taken by the camera into a csv file.
It iterates a line with information :
- the id of the image
- the formatted date it was taken
- the path to access it
"""


def add(file):
    #   parsing of the name of the file
    name = file[7:24]

    #   get the date contained inside the file's name
    d = name[0:2]
    mo = name[2: 4]
    y = name[4: 8]
    h = name[8: 10]
    m = name[10: 12]
    s = name[12: 14]

    # time the screenshots was taken formatted
    time = d + "/" + mo + "/" + y + "||" + h + "::" + m + "::" + s

    # path of the file
    path = "images/" + file
    #   the row that will be added to the csv contains the id, the formatted date and the path of the screenshots
    row = [getlines(), time, path]

    #   got through the csv and add a row at the end
    with open('images/log.csv', "a") as a:
        writer = csv.writer(a)
        writer.writerow(row)
