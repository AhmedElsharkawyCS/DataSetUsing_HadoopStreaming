#!/usr/bin/env python
import sys
for line in sys.stdin:
    # Setting some defaults
	user_id = ""
	product_id = "none"
	location = "none"
        #amount="-"

	line = line.strip()
	splits = line.split("\t")
	#for item dtatset
        if len(splits) == 5:
		user_id = splits[2]
		product_id = splits[1]
                #amount=splits[3]
	else:#for user dataset
		user_id = splits[0]
		location = splits[3] 
                #print location
                #amount=splits[3]                  
	print '%s\t%s\t%s' % (user_id,product_id,location)
