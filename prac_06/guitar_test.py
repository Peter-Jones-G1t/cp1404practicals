"""
Testing for guitar.py
"""

from prac_06.guitar import Guitar

gibson_l_5_ces = Guitar("Gibson L-5 CES", 1922)
another_guitar = Guitar("Another Guitar", 2013)

print(f"Gibson L-5 CES get_age() - Expected 103. Got {gibson_l_5_ces.get_age()}")
print(f"Another Guitar get_age() - Expected 12. Got {another_guitar.get_age()}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson_l_5_ces.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
