# -*- coding: utf-8 -*-

import requests
import sys

param   = len(sys.argv) - 1
param_a = param % 2
param_b = param / 2
headers, res = "", "";
URL = sys.argv[param]

class function:
    URL = sys.argv[param]
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

    def request(self, res):
	self.res = requests.get(URL, headers=self.headers)
	self.restxt = self.res.text

    def response(self):
	return self.res

    def responsetxt(self):
	return self.restxt

    def UA(self, headers):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

    def main(self):
        print "[*]Starting GET Request Process..."
        if sys.argv[1] == "-u":
            self.UA(self)
            self.request(self)
	    print self.response()
	    print self.responsetxt()
        elif sys.argv[1] == "-s":
            sub1()
        elif sys.argv[1] == "-h":
            fnc.help()

    def sub1():
        print sys.argv[param]
        if param_a == 1:
            print "True!"
            print param_b
        else:
            print "False"

if __name__ == '__main__':
    m = function()
    m.main()
