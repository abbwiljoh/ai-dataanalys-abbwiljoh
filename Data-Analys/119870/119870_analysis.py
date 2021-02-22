import matplotlib.pyplot as plt
# Z-vertical, X/Y-horizontal
ma_window_mid = 1

t = []
x = []
y = []
z = []
z_avg = []


def mov_avg(values, window):
    '''Returns list of filtered values to be used in plotting, number of values is preserved.
    \nWindow = number of values on each side of central value. If window=1, there will be 1+1+1 values in the window, if window= 2 there will be 2+1+2 values in window.'''
    avg_list = []
    for index, data_point in enumerate(values):
        moving_average = []
        # VI VILL HITTA FÖNSTRET GENOM ATT BÖRJA FRÅN VÄNSTER OCH GÅ MOT HÖGER (GRAFISKT SETT)
        i = index - window
        while index - window <= i <= index + window:
            try:
                moving_average.append(values[i])
            except IndexError:
                pass
            i += 1
        try:
            # HITTA MEDELVÄRDET AV ALLA VÄRDEN I FÖNSTRET
            avg = sum(moving_average) / len(moving_average)
        except ZeroDivisionError as e:
            # OM NÅGOT GÅR FEL FINNS ETT STANDARD-FÖNSTER
            avg = sum(moving_average) / (2 * window + 1)
            print(f'{e} in index {index}: "{moving_average}"')
        avg_list.append(avg)
    return avg_list


def cycle_max(values, time):
    '''Returns list of dictionaries containing cycle data: Start time, duration, cycle number, and cycle type.
    \n values is a list of values, time is a list of times corresponding to the values.'''

    cycle = 1
    cycles = []
    i = 0
    start_time = 0
    for index, v in enumerate(values):

        # EFTERSOM VI VILL JÄMFÖRA MED VÄRDEN FÖRE OCH EFTER MÅSTE VI SE TILL ATT DE VÄRDENA FINNS
        if index in [0, 1, len(values) - 1, len(values) - 2]:
            pass

        else:
            # SJÄLVA "DEFINITIONEN" AV EN MAXIMIPUNKT ENLIGT PRESENTATIONEN (ENKEL)
            if values[index - 2] < values[index - 1] < v and v > values[
                    index + 1] > values[index + 2]:
                # VI KOLLAR OM DET ÄR I BÖRJAN ELLER SLUTET AV CYKELN MED HJÄLP AV I (I=0 ELLER I=1)
                if i == 0:
                    start_time = time[index]
                    reference_time = index
                    i = 1
                # OM DET ÄR I SLUTET AV EN CYKEL VILL VI HANTERA DE INTRESSANTA DATA-PUNKTERNA
                elif i == 1:
                    # PROGRAMMET SKA FÖRSÖKA MOTBESVISA ATT CYKELN ÄR ETT GÅNGSTEG, OCH TA REDA PÅ OM DET EGENTLIGEN ÄR ETT LÖPSTEG
                    stride = 'walk-stride'
                    i = 0
                    cycle_length = t[index] - start_time
                    # I CYKEL-INTERVALLET SER VI OM ACCELERATIONEN NEDÅT ÄR MINDRE ÄN NOLL, ALLTSÅ ETT LÖPSTEG
                    for value in range(int(reference_time), index, 1):
                        if values[value] < 0:
                            stride = 'run-stride'
                            break
                    # ALLT LÄGGS IHOP I EN DICTIONARY ATT HANTERAS SENARE
                    cycle_dict = {
                        'start_time': start_time,
                        'cycle_length': round(cycle_length, 5),
                        'cycle_number': cycle,
                        'cycle_type': stride
                    }
                    cycles.append(cycle_dict)
                    cycle += 1
    return cycles


with open('119870/rawdata119870.csv') as raw_data:  # rawdata119870.csv
    # VI DELAR UPP DATAN I RADER (rows) OCH SEDAN I ENSTAKA DATA-PUNKTER
    rows = raw_data.read().split('\n')

    for index, row in enumerate(rows):
        data = row.split(',')
        try:
            if index == 0:
                # TIDEN INNAN INSPELING ÄR IRRELEVANT, SÅ VI SUBTRAHERAR DEN FRÅN ALLA TIDS-VÄRDEN
                err_time = int(data[0])
            T = int(data[0])
            # PROGRAMMET ANTAR ATT VI ARBETAR I MILLISEKUNDER SOM OMVANDLAS TILL SEKUNDER FÖR ATT TYDLIGARE AVLÄSAS I DIAGRAMMET
            T = (T - err_time) / 1000
            X = float(data[1])
            Z = float(data[2])
            Y = float(data[3])
        except ValueError as e:
            pass
        # TIDS- OCH ACCELERATIONSVÄRDE-LISTOR FÖR ATT ANVÄNDAS I ANALYSEN OCH GRAFRITNINGEN
        t.append(T)
        z.append(Z)
        x.append(X)
        y.append(Y)

# ÖPPNAR EN SEPARAT FIL DÄR ALLA VÄRDEN SPARAS
with open('119870_stridedata.csv', 'w') as f:
    # FÖRSTA RADEN I FILEN
    lines = 'start_time,cycle_length,cycle_number,cycle_type\n'

    for cycle in cycle_max(mov_avg(z, 2), t):
        # LÄGGER TILL ALLA VÄRDEN I ORDNING ENLIGT UPPGIFTEN TILL FILEN
        lines += f'{cycle["start_time"]},{cycle["cycle_length"]},{cycle["cycle_number"]},{cycle["cycle_type"]}\n'
    f.write(lines)

# GRAFEN RITAS UT MED LÄMPLIGA VÄRDEN
plt.plot(t, z, label='Raw Data')
plt.plot(t, mov_avg(mov_avg(z, 1), 1), label="Z: Double-Smoothed (window: 3)")
plt.plot(t, mov_avg(mov_avg(x, 1), 1), label="X: Double-Smoothed (window: 3)")
plt.plot(t, mov_avg(mov_avg(y, 1), 1), label="Y: Double-Smoothed (window: 3)")
# plt.plot(t,mov_avg(z,4), label = "Smoothed (window: 9)")
# plt.plot(t,mov_avg(z, 13), label= "Smoothed (window: 27)")
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s**2)')
plt.title('Accelerometerdata')
plt.legend()
plt.show()

# HÄR HAR JAG BARA LAGT IN FRAMÅT- OCH SIDOVÄRDENA FÖR SKOJS SKULL. MAN KAN BEDÖMA BALANS OSV. OM MAN VET VAD MAN LETAR EFTER. DET VET INTE JAG, MEN GRAFERNA SER UT SOM COOL ABSTRAKT KONST!
plt.plot(mov_avg(mov_avg(x, 1), 1),
         mov_avg(mov_avg(z, 1), 1),
         label="x-z: Double-Smoothed (window: 3)")
plt.plot(mov_avg(mov_avg(y, 1), 1),
         mov_avg(mov_avg(z, 1), 1),
         label="x-z: Double-Smoothed (window: 3)")
plt.show()