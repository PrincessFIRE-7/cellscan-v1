def grade_cell(voltage, resistance):
    if voltage >= 3.9 and resistance <= 80:
        return "A"
    elif voltage >= 3.6 and resistance <= 150:
        return "B"
    else:
        return "C"

voltages = [3.9, 3.8, 2.8, 4.2]
resistances = [60, 80, 100, 170]

for v, r in zip(voltages, resistances):
    print(v, r, grade_cell(v, r))
