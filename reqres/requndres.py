# -*- coding: utf-8 -*-

import requests
import sys

param   = len(sys.argv) - 1
param_a = param % 2
param_b = param / 2

class function:
    URL = sys.argv[param]
    def UA(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        print headers

#    def log(self):

    def help(self):

        print "+-------------+"
        print "|Command Usage|"
        print "+-------------+"
        print ""
        print "-v  : This Program Version"
        print ""
        print "-u <UA-code> : User-Agent prefix"
	print ""
        print "   <UA-code>"
        print "   a6   : android 6.x"
        print "   a7   : android 7.x"
        print "   s    : safari"
        print "   c    : chrome"
        print "   i    : InternetExplorer"
        print "   f    : FireFox"
	print ""


    def main():
        print "[*]Starting GET Request Process..."
        t = sys.argv[2]
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

        r = requests.get(t, headers=headers)
        print r.text

    def sub1():
        print sys.argv[param]
        if param_a == 1:
            print "True!"
            print param_b
        else:
            print "False"

if __name__ == '__main__':

    fnc = function()
    if sys.argv[1] == "-u":
        fnc.UA()
    elif sys.argv[1] == "-s":
        sub1()
    elif sys.argv[1] == "-h":
        fnc.help()
