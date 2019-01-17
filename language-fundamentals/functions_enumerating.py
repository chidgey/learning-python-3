#!/usr/bin/env python3

def skyline_hacker_speak(message):
    result = []
    for character in enumerate(message):
        if character[0] % 2 == 0:
            result.append(character[1].lower())
        else:
            result.append(character[1].upper())
    return ''.join(result)

print(skyline_hacker_speak('hacker elite speak for the skyline exercise'))