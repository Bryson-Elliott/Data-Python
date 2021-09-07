open_file = open('CupcakeInvoices.csv')

for row in open_file:
    print(row)

#open_file.close()

open_file.seek(0)

#Cupcake Flavas!
for line in open_file:
    line = line.rstrip('\n').split(',')
    cupcakes = line[2]
    print(cupcakes)

#open_file.close()

open_file.seek(0)

#Invoice total
for line in open_file:
    line = line.rstrip('\n').split(',')
    quantity = int(line[3])
    price = float(line[4])
    total = quantity * price
    print(total)

#open_file.close()

open_file.seek(0)
total = 0
for line in open_file:
    line = line.rstrip('\n').split(',')
    quantity = int(line[3])
    price = float(line[4])
    total += quantity * price
    
print(total)

open_file.close()