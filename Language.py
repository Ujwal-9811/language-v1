import sys

variables = {}

def execute_line(code):
    parts = code.strip().split()

    if not parts:
        return

    command = parts[0]

    if command == "set":
        name = parts[1]
        expression = " ".join(parts[3:])
        value = eval(expression, {}, variables)
        variables[name] = value

    elif command == "say":
        expression = " ".join(parts[1:])
        result = eval(expression, {}, variables)
        print(result)

    else:
        print("Language Error: Unknown command")


def run_file(filename):
    with open(filename) as file:
        for line in file:
            try:
                execute_line(line)
            except Exception as e:
                print("Language Error:", e)


def repl():
    while True:
        try:
            code = input("Language> ")
            execute_line(code)
        except Exception as e:
            print("Language Error:", e)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        repl()