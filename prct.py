import argparse

parser = argparse.ArgumentParser(
    description="Provides a personal greeting."
)

parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="The name of person to greet."
)

args = parser.add_argument()

msg = f"hello {args.name}!"
print(msg)