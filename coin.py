#!/usr/bin/env python

import sys
import ConfigParser

def catchacoin():
    if sys.argv[1] == None:
        print 'Enter coin type'
        return
    else:
            if sys.argv[1].lower() == 'zet':
                print 'ZETACOINZ'
            elif sys.argv[1].lower() == 'btc':
                print 'BITCOINZ'
            elif sys.argv[1].lower() == 'frc':
                print 'FREI'
            elif sys.argv[1].lower() == 'trc':
                print 'TERROR'
            else:
                print 'NO COINZ'

if __name__ == '__main__':
    catchacoin()