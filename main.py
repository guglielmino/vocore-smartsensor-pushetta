

# The MIT License (MIT)
#
# Copyright (c) 2015 Fabrizio Guglielmino
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
##

__author__ = 'Fabrizio Guglielmino, guglielmino@gmail.com'

import time
from pushetta import sendNotification
from pin import DigitalIO
from pin import GPIO0

pin = DigitalIO.get_input(GPIO0)
while True:
    read = pin.state()
    if read == 0:
       print "Something move"
       # NOTE: API_KEY and MYCHANNEL must be updated with values
       #       created in pushetta web site in the previous steps
       sendNotification("API_KEY", "MYCHANNEL", "ALARM!!! Something move")
    else:
       print "No motion" 
    time.sleep(0.5)
