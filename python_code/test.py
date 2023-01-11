import os
# if not os.path.exists("./directory"):
#     os.makedirs("./directory")
import time

now = str(time.ctime()).split(" ")
length = len(now)
time_tag = "most recent update (" + now[0] + " " + now[1] + " " + now[length-3] + " " + now[length-1]  + ")"

print(now[length-3].zfill(2))


print(time_tag)
'''
['Sun', 'Dec', '', '4', '09:44:35', '2022']
['Sun', 'Dec', '11', '01:29:52', '2022']
Sun Dec 11 01:29:52 2022
'''
print(time.ctime())