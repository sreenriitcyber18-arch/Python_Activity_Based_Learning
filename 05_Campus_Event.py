# Campus Event Financial Planning

import math

venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
catering = float(input("Catering cost: "))
transport = float(input("Transport cost: "))
sponsorship = float(input("Sponsorship amount: "))

total = venue + equipment + catering + transport
remaining = max(0, total - sponsorship)

participants = math.ceil(remaining / 500)

print("Total Expenses:", total)
print("Sponsorship:", sponsorship)
print("Remaining Amount:", remaining)
print("Minimum Participants:", participants)
