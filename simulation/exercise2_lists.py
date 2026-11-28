voltages = [3.9, 3.6, 4.2, 2.8, 3.8]
voltages.append(3.7)
print(voltages)
voltages.sort()
print(voltages)
voltages.reverse()
print(voltages)

def average(volts):
    total = 0
    for v in volts:
        total += v
        average = total / len(volts)
    return average

print(average(voltages))

                
