import os
import sys


terms = ['hackathon', 'Dec', 'Chicago', 'Java']

with open(os.getenv("HOME")+"/input/HW2.txt") as input_file:
    lines = input_file.readlines()
    with open('output_without_hadoop.txt', 'w') as file:
        for i in terms:
            output = "{} {}".format(i,sum(i.lower() in j.lower() for j in lines))
            print(output)
            file.write(output)
            file.write("\n")