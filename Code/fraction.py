def gcf(a, b):
    while b:
        c = a % b
        a = b
        b = c
    return a


def main():
    filename = input("File name: ")
    file = open(filename, "r")
    s = file.readline()
    while s:
        stlist = s.split(" ")
        num = int(stlist[0])
        den = int(stlist[1])
        s = file.readline()
        greatest = gcf(num , den)
        print(num // greatest,"/",den // greatest)
    file.close()

if __name__ == '__main__':
    main()
