#! /usr/bin/python3

# 1. Take the number of points one team is ahead.
points = int(input("Enter the lead in points: "))

# 2. Subtract three.
lead_calculation = float(points - 3)

# 3. Add a half-point if the team that is ahead has the ball,
#    and subtract a half-point if the other team has the ball.
has_ball = input("Does the lead team have the ball (Yes or No): ")

if has_ball == "Yes":
    lead_calculation = lead_calculation + 0.5
else:
    lead_calculation = lead_calculation - 0.5

# (Numbers less than zero become zero)
if lead_calculation < 0:
    lead_calculation = 0

# 4. Square that.
lead_calculation = lead_calculation ** 2

# 5. If the result is greater than the number of seconds left in the
#    game, the lead is safe.
seconds_remaining = int(input("Enter the number of seconds remaining: "))

if lead_calculation > seconds_remaining:
    print("Lead is safe.")
else:
    print("Lead is not safe.")
