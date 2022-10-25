#!/usr/bin/env python

"""
Pandoc filter to only keep headers
"""

from pandocfilters import toJSONFilters, Header, Para

# Whether the travel point is in a header tag or not
position = -1
max_els_below = 0

def remove_img(key, value, format, meta):
    if key == 'Image':
        return []

def headers_only(key, value, format, meta):
    global position
    global max_els_below

    if key == 'Header':
        position = 0
        max_els_below = len(value[2])
        return None

    elif position >= max_els_below or position == -1:
        position = -1
        max_els_below = 0
        return []

    else:
        position += 1
        return None    
    
if __name__ == "__main__":
    toJSONFilters([remove_img, headers_only])