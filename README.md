# CellScan V1

A battery cell tester built on the Raspberry Pi Pico W. It will measure voltage, current, temperature and internal resistance, then grade a cell as A, B or C.

**Status:** just started (Nov 2026). Simulating in Wokwi first, then building real hardware.

## Blink LED (simulation)

- `simulation/redblink.py`: MicroPython blink, LED on GP15 through a 220 ohm resistor. [Run it in Wokwi](https://wokwi.com/projects/481918925812021249)
- `simulation/blink.py`: earlier version that runs on a normal PC.
- `simulation/machine.py`: a stand-in for the Pico's `machine` module so the PC version runs. Do not upload it to a Pico.

## Other files

- `simulation/grade_cell.py`: grades a cell A, B or C.
- `simulation/count_grades.py`: counts how many A, B and C grades there are.
