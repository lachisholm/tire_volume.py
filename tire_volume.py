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

# my notes
# What: Import Python standard math module to access constants and functions
# Insert before any calculations that use pi or math helpers
# where: at the very top
# Does/Means: makes math.pi and other math ulitities available
import math

from pathlib import Path


again = "yes"

while again =="yes":

# ***************************TIRE*******************************
    # capture the width of tire
    w = float(input("Enter the width of the tire in mm (ex. 205): "))

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
        
    # WHAT: Read the user's answer ("yes" or "no") into a temporary variable for validation.
    # WHEN: End of the loop iteration, after writing the record to volumes.txt.
    # WHERE: Inside the while-loop, immediately after the with-block that appended to the file.
    # DOES/MEANS: Normalize the input for comparison.
    resp = input("Do you want to enter another set? (yes/no): ").strip().lower()

    # WHAT: Validate the response; only accept "yes" or "no".
    # WHEN: Immediately after capturing 'resp'.
    # WHERE: Still inside the while-loop.
    # DOES/MEANS: Re-prompt until the user types a valid answer.
    while resp not in ("yes", "no"):
        resp = input("Please type yes or no: ").strip().lower()

    # WHAT: Update the loop-control flag with the validated response.
    # WHEN: After validation succeeds.
    # WHERE: Inside the while-loop.
    # DOES/MEANS: 'yes' repeats; 'no' ends the loop naturally (no break).
    again = resp
        
    print(f"(Saved to) {Path('volumes.txt').resolve()}")

    # Ask the user if they want to test another set (condition controlled loop)
    # End of each iteration, after writing to file






