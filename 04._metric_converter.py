import math

number = float(input())
input_measurement = input()
output_measurement = input()
if input_measurement == "mm" and output_measurement == "m":
    output_measurement = number * 0.001
    print(f"{output_measurement:.3f}")
elif input_measurement == "mm" and output_measurement == "cm":
    output_measurement = number * 0.1
    print(f"{output_measurement:.3f}")
elif input_measurement == "cm" and output_measurement == "mm":
    output_measurement = number * 10
    print(f"{output_measurement:.3f}")
elif input_measurement == "cm" and output_measurement == "m":
    output_measurement = number * 0.01
    print(f"{output_measurement:.3f}")
elif input_measurement == "m" and output_measurement == "cm":
    output_measurement = number * 100
    print(f"{output_measurement:.3f}")
elif input_measurement == "m" and output_measurement == "mm":
    output_measurement = number * 1000
    print(f"{output_measurement:.3f}")
