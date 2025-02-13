import hou
import traceback
import FLOPs_Utils as flops

def updateNodeColor(node, event_type, **kwargs):
	parmTuple = kwargs["parm_tuple"]

	if parmTuple is not None:
	
		c = hou.Color()

		r, g, b = flops.getColorParm(node, "color")

		tr, tg, tb = flops.getColorTempParm(node, "temperature")
		
		if any(parmTuple.name() == x for x in ["color", "colorMode", "light_enabled", "temperature"]):
			if node.parm("light_enabled").eval() == 0:
				c.setRGB((0.1, 0.1, 0.1))

				try:
					node.setColor(c)
					node.setComment("off")
					node.setGenericFlag(hou.nodeFlag.DisplayComment, True)

				except:
					pass
			else:
				if node.parm("colorMode").eval() == "0":
					c.setRGB((r, g, b))

				elif (node.parm("colorMode").eval() == "1"):
					c.setRGB((tr, tg, tb))

				else:
					c.setRGB((r * tr, g * tg, b * tb))
				
				try:
					node.setColor(c)
					node.setComment("")

				except:
					pass

try:
	node = kwargs["node"]

	if node is not None:
		node.addEventCallback((hou.nodeEventType.ParmTupleChanged, ), updateNodeColor)

except:
	print(traceback.format_exc())