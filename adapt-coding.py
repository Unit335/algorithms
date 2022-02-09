from collections import Counter
from decimal import Decimal
import random, string, decimal
import sys

def segmentation(alphabet): #alphabet: set of unique characters in message
    # Defining starting lenghts of segments
    p = Decimal(1)/Decimal(len(alphabet))
    left = Decimal(0)
    right = p
    segments = dict()
    for i in alphabet:
        segments[i] = [left, right, Decimal(1)]
        left = right
        right = right + p
    return segments

def resize(segments):
    # resizing segments after changes in symbol weight
    l = Decimal(0)
    s = Decimal(0)
    for i in segments:
        s = s + segments[i][2]
    for i in segments:
        segments[i][0] = l
        segments[i][1] = l + (segments[i][2] / s)
        l = segments[i][1]
    return segments

def ad_coding(s): #s: str - message to encode
    segments = segmentation(set(s))
    left = Decimal(0)
    right = Decimal(1)
    for i in s:
        segments[i][2] = segments[i][2] + Decimal(1)
        newright = left + (right - left) * segments[i][1]
        newleft = left + (right - left) * segments[i][0]
        left = newleft
        right = newright
        resize(segments)
    return (left + right)/Decimal(2)

def ad_decoding(code, alphabet, l): #code: descimal - message to decode
                                    #alphabet: set of unique characters in message
                                    #l: int - expected length of message
    segments = segmentation(alphabet)
    s = []
    for i in range(l):
        for j in alphabet:
            if code >= segments[j][0] and code < segments[j][1]:
                s.append(j)
                segments[j][2] = segments[j][2] + Decimal(1)
                code = (code - segments[j][0]) / (segments[j][1] - segments[j][0])
                resize(segments)
                break
    return s

def enc(toencode, output):   #toencode: str - filepath to datasource for encoding
                             #output: str - filepath for output
    with open(toencode, 'r') as f:
        s = f.read()
    l = len(s)
    alphabet = set(s)
    code = str(l) + '\n' + ''.join(alphabet) + '\n' + str(ad_coding(s))
    with open(output, 'w') as f:
        f.write(str(code))

def dec(todecode, output):      #todecode: str - filepath to datasource for decoding
                                #output: str - filepath for output
    with open(todecode, 'r') as f:
        lines = f.readlines()
    msg = ad_decoding(Decimal(lines[2]), list(lines[1])[:-1], int(lines[0]))

    with open(output, 'w') as f:
        f.write(''.join(msg))

def main(args):
    decimal.getcontext().prec = 400 # maximum length of decimals, determines precision of encoding/decoding
    msg = "Usage: python adapt-coding.py encode input output: encode text from file and write result as output\npython adapt-coding.py decode input output: decode file and write result as output"
    if len(args) != 3:
        sys.exit(msg)
    if args[0] == 'encode':
        enc(args[1], args[2])
    elif args[0] == 'decode':
        dec(args[1], args[2])
    else:
        sys.exit(msg)


if __name__ == '__main__':
    main(sys.argv[1:])