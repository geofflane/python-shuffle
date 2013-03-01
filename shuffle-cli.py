#!/usr/bin/env python
"""
Usage: %(program)s [options] ... [-b <number>] [-s <number>] [-g <number>]
Options:
  -h, --help    This help message
  -b, --blocks  The number of blocks (default: 20)
  -s, --size    The number of participants in each group (default: 10)
  -g, --groups  The number of groups in eahc block (default: 2)
"""

import random, sys, getopt
import shuffle

program = sys.argv[0]

class CliShuffler(shuffle.Shuffler):
    def __init__(self):
        shuffle.Shuffler.__init__(self, 20, 10, 2)
        
    def print_results(self):
        for i in  range(self.blocks):
            print ' '.join([str(i) for i in self.shuffle()])

    def usage(self):
        print >> sys.stderr, __doc__ % globals()
        sys.exit()
    
    def run(self, argv):    
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hg:s:b:", ["help", "groups=", "size=", "blocks="])
        except getopt.GetoptError, err:
            # print help information and exit:
            print str(err) # will print something like "option -a not recognized"
            self.usage()
            sys.exit(2)

        for opt, arg in opts:
            if opt in ("-b", "--blocks"):
                try:
                    self.blocks = int(arg)
                except ValueError:
                    self.usage()
            elif opt in ("-s", "--size"):
                try:
                    self.blockSize = int(arg)
                except ValueError:
                    self.usage()
            elif opt in ("-g", "--groups"):
                try:
                    self.groups = int(arg)
                except ValueError:
                    self.usage()
            elif opt in ("-h", "--help"):
                self.usage()
            else:
                assert False, "unhandled option"
        
        if not self.is_valid_group_size():
            print("Block Size must be evenly divisible by groups to get an even grouping.")
            self.usage()
            sys.exit()

        self.print_results()
    
if __name__ == "__main__":
    shuffler = CliShuffler()
    shuffler.run(sys.argv[1:])
