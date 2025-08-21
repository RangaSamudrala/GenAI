import subprocess

command = "python calculator.py 5 3 '*'"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

with open("output.txt", "w") as file:
    file.write(result.stdout)

