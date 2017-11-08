# -*- coding: utf-8 -*-

import re

s = '<html><head><title>testanddeploy</title></head><body><h1>HTML is very easy</h1><p>easy modal...</p></body></html>'
ptn = '<([^>]*)>'

match = re.findall(ptn, s)

print ('array: %s\n' % match)

cnt = len(match)

print ('Count: %s\n' % cnt)

