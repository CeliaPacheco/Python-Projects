import argparse



def four_bytes(byte_str):
    string = "".join(hex(x)[2:] for x in byte_str) #convert bytes into string
    hex_val_lst = [] #list of hex values of 4 byte increments
    i = 0
    while i < len(string):
        tmpstr = string[i:i+8]
        if len(tmpstr) < 8: #zero pad string
            while len(tmpstr) < 8:
                tmpstr += "0"
        tmphex = int(tmpstr, 16)
        hex_val_lst.append(tmphex)
        i += 8
    return hex_val_lst

def encode(hexlist):
    """ encodes the string """
    print(hexlist)
    ascii_85 = []
    for hex_val in hexlist:
        print(hex_val)
        while hex_val != 0:
            ascii_85.append(hex_val % 85)
            hex_val = hex_val // 85
    for i in range(len(ascii_85)):
        ascii_85[i] += 33
#    ascii_85.reverse()
    return ascii_85

def decode(hexlist):
    """ decodes the string """
    ascii_85 = []
    for hex_val in hexlist:
        while hex_val != 0:
            ascii_85.append(hex_val % 85)
            hex_val = hex_val // 85
    for i in range(len(ascii_85)):
        ascii_85[i] -= 33
    #ascii_85.reverse()
    return ascii_85

def get_str (ascii_85):
    "get the string from hex values"
    new_string = "".join(chr(x) for x in ascii_85)
    print(new_string)


def main():
    """ main function """
    parser = argparse.ArgumentParser(description="Encode or Decode to ASCII85")
    parser.add_argument("string", help="convert stirng to ascii85")
    parser.add_argument("-e", "--encode", help="encode to ascii85", action="store_true")
    parser.add_argument("-d", "--decode", help="decode from ascii85", action="store_true")
    args = parser.parse_args()

    b = args.string.encode() #get byte value of string
    hex_val_list = four_bytes(b)

    if args.encode:
        ascii_85 = encode(hex_val_list)
        print(ascii_85)
        get_str(ascii_85)
    elif args.decode:
        ascii_85 = decode(hex_val_list)
        print(ascii_85)
        get_str(ascii_85)






if __name__ == "__main__":
    main()
