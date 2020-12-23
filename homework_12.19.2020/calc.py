import os
os.chdir("/home/hov/ACA/homework/homework_12.19.2020/log")
import datetime
import re

def calc():
    date_time = str(datetime.datetime.now()) # converting date to string to import in .txt file

    x = list(map(str, input("Expression: ").split()))
    error = 0
    info = 0

    # input should have 3 values
    if len(x) != 3:
        error = 0
        info = 0
        with open('log.txt', 'a') as output: # appending error
            output.write(f"{date_time} :: ERROR :: Input 3 values :: {x} ::\n")

        with open('log.txt', 'r') as output: # counting errors and info for output
            for i in output:
                if "ERROR" in i:
                    error += 1
                    info += 1

        print("ERROR: Invalid expression")
        print(f"Report: INFO-{info}, ERROR-{error}")
        exit()

    # Should be provided numbers
    if re.match(r'^-?\d+(?:\.\d+)?$', x[1]) is None or re.match(r'^-?\d+(?:\.\d+)?$', x[2]) is None:
        with open('log.txt', 'a') as output:
            output.write(f"{date_time} :: ERROR :: Provide numbers! :: {x} ::\n") # appending error

        with open('log.txt', 'r') as output: # counting errors and info for output
            for i in output:
                if "ERROR" in i:
                    error += 1
                    info += 1

        print("ERROR: Invalid expression")
        print(f"Report: INFO-{info}, ERROR-{error}")
        exit()

    sign = x[0]
    num1 = float(x[1])
    num2 = float(x[2])
    info = 0
    error = 0
    if sign == "+" or sign == "add": # condition for +
        result = num1 + num2
        with open('log.txt', 'a') as output:
            output.write(f"{date_time} :: INFO :: {x} :: {result} ::\n")

        with open('log.txt', 'r') as output: # counting errors and info for output
            for i in output:
                if "ERROR" in i:
                    error += 1
                    info += 1
                elif "INFO" in i:
                    info += 1
        print("Result: ", result)
        print(f"Report: INFO-{info}, ERROR-{error}")

    elif sign == "-" or sign == "sub": # condition for -
        result = num1 - num2
        with open('log.txt', 'a') as output: # counting errors and info for output
            output.write(f"{date_time} :: INFO :: {x} :: {result} ::\n")

        with open('log.txt', 'r') as output:
            for i in output:
                if "ERROR" in i:
                    error += 1
                    info += 1
                elif "INFO" in i:
                    info += 1
        print("Result: ", result)
        print(f"Report: INFO-{info}, ERROR-{error}")
    elif sign == "*" or sign == "mul": # condition for *
        result = num1 * num2
        with open('log.txt', 'a') as output: # counting errors and info for output
            output.write(f"{date_time} :: INFO :: {x} :: {result} ::\n")

        with open('log.txt', 'r') as output:
            for i in output:
                if "ERROR" in i:
                    error += 1
                    info += 1
                elif "INFO" in i:
                    info += 1
        print("Result: ", result)
        print(f"Report: INFO-{info}, ERROR-{error}")
    elif sign == "/" or sign == "div": # condition for /
        result = num1 / num2
        with open('log.txt', 'a') as output: # counting errors and info for output
            output.write(f"{date_time} :: INFO :: {x} :: {result} ::\n")

        with open('log.txt', 'r') as output:
            for i in output:
                if "ERROR" in i:
                    error += 1
                    info += 1
                elif "INFO" in i:
                    info += 1
        print("Result: ", result)
        print(f"Report: INFO-{info}, ERROR-{error}")
    else:
        with open('log.txt', 'a') as output:
            output.write(f"{date_time} :: ERROR :: Provide signs! :: {x} ::\n")

        with open('log.txt', 'r') as output: # counting errors and info for output
            for i in output:
                if "ERROR" in i:
                    error += 1
                    info += 1
        print("ERROR: Invalid expression")
        print(f"Report: INFO-{info}, ERROR-{error}")
        exit()

calc()