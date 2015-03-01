import csv
with open('coord.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    f = open('test.kml', 'w')
    f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    f.write("<kml xmlns='http://earth.google.com/kml/2.1'>\n")
    f.write("<Document>\n")
    f.write("   <name></name>\n")
    f.close()
    for row in reader:
        f = open('test.kml', 'a')
        f.write("<Placemark><name>" + row['name'] + "</name><Point><coordinates>" + row['long'] + "," + row['lat'] + "</coordinates></Point></Placemark>" + "\n")
    f.write("</Document>\n")
    f.write("</kml>\n")
    f.close()
