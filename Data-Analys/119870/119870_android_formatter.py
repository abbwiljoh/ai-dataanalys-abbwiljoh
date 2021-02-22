import time
# time, x, y, z <-- x, z, y, time_from_prev

X = []
Y = []
Z = []
T = 0
times = []
total_time = 0
write_string = ''

file = input('File path > ')
time1 = time.perf_counter()

with open(file) as f:
    rows = f.read().split('\n')
    
    for row in rows:
        data = row.split(',')
        try:
            x = float(data[0])
            y = float(data[2])
            z = float(data[1])
            T = int(data[3])
            total_time += T
            X.append(x)
            Y.append(y)
            Z.append(z)
            times.append(total_time)

        except ValueError:
            pass


formatted =  input('Input formatted file name > ')
formatted = formatted.split('.')
formatted = formatted[0] + '.csv'

with open(formatted, 'w') as f:
    for index, t in enumerate(times):
        write_string += f'{t},{X[index]},{Y[index]},{Z[index]}\n'
    f.write(write_string)
time2 = time.perf_counter()

print(f'Done in {round(time2-time1, 3)} s')