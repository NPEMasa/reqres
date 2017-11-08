# -*- coding: utf-8 -*-

import requests
import sys

param   = len(sys.argv) - 1
param_a = param % 2
param_b = param / 2
headers, res = "", "";
URL = sys.argv[param]

class reqres():
    def msg(self):
        help = """
+--------------+
| Command help |
+--------------+

-v  : This Program Version

-u <UA-code> : User-Agent prefix

<UA-code>
a6   : android 6.x
a7   : android 7.x
s    : Apple Safari
c    : Google Chrome
i    : Internet Explorer
f    : Mozzila FireFox

[User-Agent Usage]
$ python requndres.py -u s http://example.com/
$ python requndres.py -u i http://example.com/

"""
        print (help)

    def request(self):
        headers = self.UA()
        self.res = requests.get(URL, headers=headers)
        self.res_txt = self.res.text

    def res_state(self):
        return self.res

    def res_txt(self):
        return self.res_txt

    def UA(self):
        if sys.argv[2] == "a6":
            self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 6.0.1; ja-jp; Nexus 6P) AppleWebKit/533.1 (KHTML, like Gecko) Version/6.0 Mobile Safari/533.1'}
        elif sys.argv[2] == "a7":
            self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 7.0; ja-jp; Nexus 6P) AppleWebKit/533.1 (KHTML, like Gecko) Version/6.0 Mobile Safari/533.1'}
        elif sys.argv[2] == "s":
            self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'}
        elif sys.argv[2] == "c":
            self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36'}
        elif sys.argv[2] == "i":
            self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko'}
        elif sys.argv[2] == "f":
            self.headers = {'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/20100101 Firefox/firefoxversion'}

def main():
    global r
    r = reqres()
    if sys.argv[1] == "-u":
        print ("[*]Starting GET Request Process...")
        r.UA()
        r.request()
        print (r.res_txt.encode('utf-8'))

    elif sys.argv[1] == "-h":
        r.msg()

if __name__ == '__main__':
    main()
