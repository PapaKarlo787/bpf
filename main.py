import sys
import argparse

import dpkt
from assembler import BPFAssembler

def main():
    parser = argparse.ArgumentParser(description='Videos to images')
    parser.add_argument('input', type=str, help='Input file')
    args = parser.parse_args()
    with open(args.input, "r") as f: 
        data = f.read()

    assembler = BPFAssembler()

    program = assembler.assemble(data)
    if not program:
        sys.stderr.write("Assembler failed\n")
        return 1

    for line in program:
        print('{ 0x%x, %d, %d, 0x%08x }' % line)
if __name__ == '__main__':
    main()
