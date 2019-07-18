""" Command-line configurables
"""

from argparse import ArgumentParser
import json

def set_checking_period(sec):
    """ Gets new Checking Period in seconds(int)
    Update Checking Period in config file.
    """
    with open('config.json', 'r') as json_data_file:
        data = json.load(json_data_file)
        
    data['checking_period']['sec'] = sec
    with open('config.json', 'w') as json_data_file:
        json.dump(data, json_data_file, indent=2)
        print("Checking period updated to:", sec, "seconds")

def main():
    """ cmd options menu """
    parser = ArgumentParser()
    parser.add_argument("-scp", type=int, dest="seconds",
                        help="set checking period last in seconds")
    args = parser.parse_args()
    if args.seconds is not None:
        set_checking_period(args.seconds)
    else:
        parser.print_help()
        
if __name__ == "__main__":
    main()