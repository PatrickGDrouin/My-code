#!/usr/bin/env python3
"""Move and Rename Files with shutil"""

import shutil  # For moving and renaming files
import os  # For directory operations

def main():
    """Main logic"""
    overwrite = "n"
    # Ensure the script starts in the correct directory
    os.chdir("/home/student/mycode/")
    if os.path.exists("battlecruiser/raynor.obj"):
        overwrite = input("would you like to overwrite the file(y/n): ")
    if  not os.path.exists("battlecruiser/raynor.obj") or overwrite == "y":
        # Move Raynor to battlecruiser
        if overwrite == "y":
            os.remove("battlecruiser/raynor.obj")
        shutil.move("raynor.obj", "battlecruiser/")
        
    # Prompt for Kerrigan's new name
    # xname = input("What is the new name for kerrigan.obj? ")

    # Rename Kerrigan
    # shutil.move("battlecruiser/kerrigan.obj", f"battlecruiser/{xname}")

main()
