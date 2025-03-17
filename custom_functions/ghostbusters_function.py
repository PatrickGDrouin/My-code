#!/user/bin/env python3
"""Ghostbusters lab | step 1"""

"""def  report_ghost_sighting(ghost_name, location):
    prints a message about a ghost sightin
    print(f"{ghost_name} has been sighted at {location}! Who you gonna call?")

report_ghost_sighting("slimer", "hotel sedgeick")
report_ghost_sighting("stay puft", "new york city")"""

def cal_catch_rate(ghost_name):
    """return a catch rate based on the ghost's name"""
    return len(ghost_name) * 10

rate = cal_catch_rate("slimer")

print(f"the catch rate for this ghost is: {rate}")

