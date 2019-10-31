import csv

with open('testfile.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')    # Lee csv_file, que esta separado por comas
    line_count = 0
    f = open("sqlFile.txt", "a")        # Escribe en fichero en modo Appending (agrega texto al final)
    for row in csv_reader:          # Lee filas de csv y escribe en fichero sql
        if line_count == 0:
            f.write(f'INSERT INTO myTable({", ".join(row)}) VALUES \n')
            line_count += 1
        else:
            f.write(f'(\'{row[0]}\', \'{row[1]}\', \'{row[2]}\', \'{row[3]}\') \n')
            line_count += 1
    print(f'Processed {line_count} lines.')

# No usamos el metodo join al escribir las filas porque las queremos en distintas lineas, con \n