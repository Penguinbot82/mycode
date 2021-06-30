#!/usr/bin/env python3

message = 'Your WIFI newtork needs a boost.'

# wrap connection in a float() to accept decimals as numbers
connection = float(input("Enter current speed in Mbps?"))

# if input value was higher or equal to 25
if connection >= 300:
    message = message + 'use 2.4GHz band on channel 9.'
elif connection >= 200:
    message = message + 'use 2.4GHz band on channel 3.'
elif connection >= 100:
    message = message + 'use 5.0GHz band on channel 50.'
else:
    message = message + 'finding another access network.'
print(message)

