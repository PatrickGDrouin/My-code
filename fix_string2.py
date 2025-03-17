#!/usr/bin/env python3

# Define the string
quote = "Live Long And Prosper"

# Chain methods to lower the string, split it, and join with "-"
result = quote.lower().split(" ")
result = "-".join(result)
print(result)
