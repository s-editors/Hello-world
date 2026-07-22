import os
import sys
import pandas as pd


# Removed unused variableclass userData:
    def __init__(self,name):
        self.Name=name

    def display(self):
        print("User:",self.Name)


def main():
    user = userData("Suyash")
    user.display()

    value = calculate_sum(10,20)

    print(value)

    if value > 20:
        print("Greater")


main()
