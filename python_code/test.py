import os
# if not os.path.exists("./directory"):
#     os.makedirs("./directory")
import time

now = str(time.ctime()).split(" ")
time_tag = "most recent update (" + now[0] + " " + now[1] + " " + now[2] + " " + now[4]  + ")"
print(time_tag)


