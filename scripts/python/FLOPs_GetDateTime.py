import hou
import datetime

now = datetime.datetime.now()

d = now.strftime("%Y%m%d")
t = now.strftime("%H%M%S")

hou.putenv("DATE", d)
hou.putenv("TIME", t)
