#!/usr/bin/env python3
import sys
import argparse
import os
import datetime

def getArgs(argv=None):
    parser = argparse.ArgumentParser(description="Log times worked on a project \
            or whatever you want to log times for")
    parser.add_argument('--start', action='store_true', default=False)
    parser.add_argument('--stop', action='store_true', default=False)
    parser.add_argument('--calc', action='store_true',  default=False)
    parser.add_argument('-p', '--part', action='store')
    parser.add_argument('-n', '--note', action='store', default="N/A")
    parser.add_argument('file')
    return parser.parse_args(argv)

def writeBeginning(file):
    with open('/home/cel/opt/timetracker/format.txt') as f:
        for line in f:
            file.write(line)

def StartLog(file):
    d = datetime.datetime.now()
    date = d.strftime('%m/%d')
    time = d.strftime('%H:%M')
    if os.path.isfile(file):
        try:
            with open(file, 'a') as f:
               f.write("\n"+ date + "\t" + time + "\t")
        except IOError as e:
            print(e)
    else:
        try:
            with open(file, 'w+') as f:
                writeBeginning(f)
                f.write(date + "\t" + time + '\t')
        except IOError as e:
            print(e)

def StopLog(file, part, note):
    d = datetime.datetime.now()
    time = d.strftime('%H:%M')
    try:
        with open(file, 'a') as f:
            f.write(time + "\t" + part + "\t" + note)
    except IOError as e:
        print(e)

def CalcLog(file):
    times = []
    total_time = datetime.datetime.strptime('00:00', '%H:%M')
    try:
        with open(file, 'r') as f:
            f.readline()
            for line in f:
                if ":" in line:
                    times.append(line.split('\t')[1:3])
        for pair in times:
            time1 = datetime.datetime.strptime(pair[0], '%H:%M')
            time2 = datetime.datetime.strptime(pair[1], '%H:%M')
            time_delta = time2 - time1
            total_time += time_delta 
        print(total_time)
    except IOError as e:
        print(e)

def main():
    args = getArgs()

    if args.start:
        StartLog(args.file)
    elif args.stop:
        StopLog(args.file, args.part, args.note)
    elif args.calc:
        CalcLog(args.file)
    else:
        print("No flag given")


if __name__ == "__main__":
    main()
