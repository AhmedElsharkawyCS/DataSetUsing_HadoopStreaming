#!/usr/bin/env python
import sys
import string

def _format1(line,split_sig="\t"):
    return  line.strip().split(split_sig)

def reducer():
   previous_id=None
   actual_location=""
   location_count=0
   
   
   for line in sys.stdin:
            single_line=_format1(line)
            curr_product_id,curr_location=single_line
	    if len(single_line) != 2:
		        continue
	    try:
		    curr_product_id=int(curr_product_id)#convert curr_product_id into integer
 
	    except ValueError:
		          continue

            if not previous_id:
		       previous_id=curr_product_id
		       actual_location=curr_location
		       location_count=1
            if curr_product_id == previous_id:
                   if curr_location != actual_location:
		           actual_location=curr_location
		           location_count =location_count +1
	    else:
		         print '%s\t%s'%(previous_id,location_count)
		         previous_id=curr_product_id
		         actual_location=curr_location
		         location_count=1 
          
           
    
   print '%s\t%s'%(previous_id,location_count) 

if __name__=='__main__': 
  reducer()
