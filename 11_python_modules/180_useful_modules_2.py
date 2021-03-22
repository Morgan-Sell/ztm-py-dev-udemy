import datetime
from array import array

# Create time objects
#print(datetime.time())
#print(datetime.time(5, 45, 2))

# Create date objects
print(datetime.date.today())


"""

Array Object:

- Lists are dynamic. They do not posses a size constraint.
- When I initiate an array, I can set a size/memory constraint.
  ** Requires less memory and performs faster.

- array(type_code, )
   ** By telling an array what type of data it will hold, the performance is enhanced.
"""

arr = array('i', [1, 2, 3])
print(arr[0])