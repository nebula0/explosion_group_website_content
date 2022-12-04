import os
# if not os.path.exists("./directory"):
#     os.makedirs("./directory")
import time

now = str(time.ctime()).split(" ")
time_tag = "most recent update (" + now[0] + " " + now[1] + " " + now[3] + " " + now[5]  + ")"
print(time_tag)


print(now)
'''
['Sun', 'Dec', '', '4', '09:44:35', '2022']

'''
print(time.ctime())