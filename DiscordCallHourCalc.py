import time
import math
import os
import sys


callTime = "started a call that lasted"
calls = []
hours = []
total_minutes = 0
number_of_calls = 0
total_hours = 0



with open("exportedData.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)



for item in lines:
    if callTime in item:
        calls.append(item)
        number_of_calls += 1


for line in calls:
    if any(char.isdigit() for char in line):


        time_parts = [int(s) for s in line.split() if s.isdigit()]
        

        hours = time_parts[0]
        minutes = time_parts[1] if len(time_parts) > 1 else 0
        seconds = time_parts[2] if len(time_parts) > 2 else 0
        

        total_minutes += hours * 60 + minutes + seconds / 60

        total_hours = total_minutes / 60

        minutes = 60 * (total_hours - math.floor(total_hours))

        seconds = 60 * (minutes - math.floor(minutes))

        
AvgHours = total_hours / number_of_calls
AvgMinutes = (60 * (AvgHours - math.floor(AvgHours)))
AvgSeconds = (60 * (AvgMinutes - math.floor(AvgMinutes)))


print(f"{int(total_hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds is the total time spent calling.")
print(f"{number_of_calls} was the total amount of calls.")
print(f"{int(AvgHours)} hours, {int(AvgMinutes)} minutes {int(AvgSeconds)} seconds is the average length of a call.")


input("Press Enter to exit...")





















