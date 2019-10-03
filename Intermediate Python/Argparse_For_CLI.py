import argparse
import sys

def main():
    #Making a argparse object
    parser = argparse.ArgumentParser()
    #Taking inputs of variables through the CLI
    parser.add_argument('--x', type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation?(add, sub, mul, div or mod)')
    #Combining all the input variables into a single variable namely args
    args = parser.parse_args()
    #Printing the result of calling calc with args as a parameter
    sys.stdout.write(str(calc(args)))
    
    
def calc(args):
    if args.operation == 'add' :
        return args.x+args.y
    elif args.operation == 'sub':
        return args.x-args.y
    elif args.operation == 'mul':
        return args.x*args.y
    elif args.operation == 'div':
        return args.x/args.y
    elif args.operation == 'mod':
        return args.x%args.y

if __name__ == '__main__':
    main()


"""
INPUT

Goto Cmd Prompt and locate the file by changing directory...open the file using
command 'python file_name'...Run the program using the below command
python Argparse_For_CLI.py --x=2 --y=5 --operation=mul

OUTPUT
10.0

"""
