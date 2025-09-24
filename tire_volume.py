# Lora Chisholm
# CSE 111
# Assignment: 
""" The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:


# ─────────────────────────────────────────────────────────────────────────────
# Tire volume formula (assignment reference)
#                 π · w^2 · a · (w · a + 2,540 · d)
#     v   =      ───────────────────────────────────
#                       10,000,000,000
#
# WHERE: 
#   v = approximate volume of air in the tire (liters)
#   w = tire width (millimeters, user input)
#   a = aspect ratio (percent, user input)
#   d = wheel diameter (inches, user input)
# DOES/MEANS:
#   This is the exact formula we’ll implement in code below.
# ─────────────────────────────────────────────────────────────────────────────

or $$ v=\frac{\pi\, w^2\, a\,(w a + 2{,}540\, d)}{10{,}000{,}000{,}000} $$


v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches."""


import math
from pathlib import Path

# ***************************TIRE*******************************
# capture the width of tire
w= float(input("Enter the width of the tire in mm (ex. 205): "))

# capture the aspect ratio
a = float(input("Enter the aspect ratio of the tire (ex 60): "))

#Shows the exact assignment prompt; float() converts the text to a numeric value
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculation line
v = (math.pi * (w ** 2) * a * (w * a +2540 * d)) / 10_000_000_000

# uses an f string to insert v and format it to 2 decimals; leading "\n" adds the blank line shown in the sample
print(f"\nThe approximate volume is {v:.2f} liters")



#**************************DATETIME****************************

# DateTime - Makes datetime.now() available to fetch today's date from the os clock
from datetime import datetime

# Calls datetime.now() to get a datetime object we can format as YYYY-MM-DD when writing the file
current_dt = datetime.now()

# Provides a file handle named 'volumes_file', writable file
with open("volumes.txt", "at") as volumes_file:
    print(f'{current_dt:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}', file=volumes_file)
    
print(f"(Saved to) {Path('volumes.txt').resolve()}")




