import argparse
import json

if __name__ == "__main__":
    # Parse command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", dest="",
                        help=r"C:\Users\ibner\MyLearning\Combustion\config.json")
    args = parser.parse_args()

    # Ensure a config was passed to the script.
    if not args.config:
        print("No configuration file provided.")
        exit()
    else:
        with open(args.config, "r") as inp:
            config = json.load(inp)
