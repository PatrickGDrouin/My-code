#!/usr/bin/env python3
"""Attempt to read a file in the current directory"""

import os

def main():
    """Main logic"""
    os.chdir("/home/student/mycode/temp")
    with open("protoss.txt", "r") as foo:
            print(foo.read())

main()
