#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Script to generate mental calculations.
""" 

import sys
import time
import random
import math

from ctes import * 

def calculate(res, ran_op, ran_in):
    
    new_res = 0
    
    if ran_op == 0:
        new_res = res + ran_in
    elif ran_op == 1:
        new_res = res - ran_in
    elif ran_op == 2:
        new_res = res * ran_in
    elif ran_op == 3:
        new_res = res / ran_in
        
    return new_res
                
def generate_mencal():
    
    res = 0    
    times = []
    
    random.seed()
    
    for _ in range(MENCAL_LENGTH):
        
        ran_op = random.randint(0, MENCAL_OPS - 1)
        
        ran_in = random.randint(1, math.pow(10, MENCAL_SIZE[ran_op]) - 1)
        
        if not res:
            res = ran_in
            
            print ran_in
        else:
            res = calculate(res, ran_op, ran_in)
            
            print "%s %d" % (MENCAL_OP_STR[ran_op], ran_in)
            
            res_len = len(str(res))
            
            t1 = time.time()
        
            #time.sleep(res_len * MENCAL_DELAY[ran_op])
            sys.stdin.read(1)
            
            t2 = time.time()
            
            times.append(t2 - t1)
        
    print "Result is: %d" % res
    print "Times are: %s" % ["%.1f" % t for t in times]
    print "Total time is: %.1f" % sum(times)
    
def main():
    """Main function.
    """    

    generate_mencal()
        
    print "Program finished."
    
    return 0

# Where all begins ...
if __name__ == "__main__":
    
    sys.exit(main())    
