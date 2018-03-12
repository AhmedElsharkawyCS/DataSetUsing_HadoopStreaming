#!/usr/bin/env python
import sys
import string

last_value_from_user_id = None
current_location = "none"
#fil=open("out_in",'a')
#user_id,product_id,location
for line in sys.stdin:
    line = line.strip()
    user_id,product_id,location = line.split("\t")

    if not last_value_from_user_id or last_value_from_user_id != user_id:
        last_value_from_user_id = user_id
        current_location = location
    elif user_id == last_value_from_user_id:
        location = current_location
        print'%s\t%s\t%s' % (last_value_from_user_id,product_id,location)#user_id,product_id,location
    
