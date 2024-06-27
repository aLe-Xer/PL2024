
modalidades = []
total = 0
aptos = 0
inaptos = 0
escaloes = [0]* 4

with open('emd.csv', 'r') as data:
    next(data)

    for entry in data:
        total += 1

        values = entry.strip().split(',')

        age = int(values[5])
        if 20 <= age <= 24:
            escaloes[0] += 1
        elif 25 <= age <= 29:
            escaloes[1] += 1
        elif 30 <= age <= 34:
            escaloes[2] += 1
        elif 35 <= age <= 39:
            escaloes[3] += 1
        else: print("datas por validar" + str(age))

        if values[8] not in modalidades:
            modalidades.append(values[8])

        if values[12] == "true":
            aptos +=1
        else: inaptos +=1


p_aptos = (aptos/total) *100
p_inaptos = (inaptos/total) *100

modalidades.sort()

with open('result.txt', 'w') as result:

    result.write('Modalidades: \n')
    for mod in modalidades:
        result.write(mod + '\n')
    result.write('\n')

    result.write('Percentagem de atletas aptos = ' + str(p_aptos) + '\n')
    result.write('Percentagem de atletas inaptos = ' + str(p_inaptos) + '\n\n')

    result.write('Numero de pessoas por escalao:\n')
    result.write('[20-24] = ' + str(escaloes[0]) + '\n')
    result.write('[25-29] = ' + str(escaloes[1]) + '\n')
    result.write('[30-34] = ' + str(escaloes[2]) + '\n')

