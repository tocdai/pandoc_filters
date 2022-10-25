#!/usr/bin/env python

"""
Pandoc filter to remove all images in the doc
"""

from pandocfilters import toJSONFilters


def remove_img(key, value, format, meta):
    if key == "Image":
        return []


if __name__ == "__main__":
    toJSONFilters(remove_img)
