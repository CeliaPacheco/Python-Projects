import sys
import argparse
import os
import datetime

def getArgs(argv=None):
    parser = argparse.ArgumentParser(description="Log times worked on a project \
            or whatever you want to log times for")
    parser.add_argument('-st', '--start', action='store_true', default=False)
    parser.add_argument('-so', '--stop', action='store_true', default=False)
    parser.add_argument('-p', '--part', action='store')
    parser.add_argument('-n', '--note', action='store')
    parser.add_argument('file')
    return parser.parse_args(argv)

def writeBeginning(file):
    with open('format.txt') as f:
        for line in f:
            file.write(line)

def StartLog(file):
    d = datetime.datetime.now()
    if os.path.isfile(file):
        try:
            with open(file, 'a') as f:
               s = d.strftime('%m/%d    %H:%M')
               f.write("\n"+ s +"   *")
        except IOError as e:
            print(e)
    else:
        try:
            with open(file, 'w+') as f:
                writeBeginning(f)
                s = d.strftime('%m/%d    %H:%M')
                f.write(s + "   *")
        except IOError as e:
            print(e)

def StopLog(file, part, note):
    try:
        with open(file, 'a+') as f:
            #print(f)
            for line in f:
                print(line)
            """
            f.readlines(5)
            line = f.readline()
            while line:
                print(line)
                line = f.readline()
                """
    except IOError as e:
        print(e)

def main():
    args = getArgs()

    if args.start:
        StartLog(args.file)
    elif args.stop:
        StopLog(args.file, args.part, args.note)
    else:
        print("No flag given")


if __name__ == "__main__":
    main()
