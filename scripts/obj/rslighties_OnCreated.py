import hou
import traceback
import FLOPs_Utils as flops

def updateNodeColor(node, event_type, **kwargs):
	parmTuple = kwargs["parm_tuple"]

	if parmTuple is not None:
	
		c = hou.Color()

		r = node.parm("colorr").eval()
		g = node.parm("colorg").eval()
		b = node.parm("colorb").eval()

		t = flops.__colorTempToRGB(node.parm("temperature").eval())
		
		if any(parmTuple.name() == x for x in ["color", "colorMode","temperature"]):
			
			if node.parm("colorMode").eval() == "0":
				c.setRGB((r, g, b))

			elif (node.parm("colorMode").eval() == "1"):
				c.setRGB(t)

			else:
				c.setRGB((r * t[0], g * t[1], b * t[2]))

			try:
				node.setColor(c)

			except:
				pass

		elif parmTuple.name() == "light_enabled":
			if parmTuple.eval()[0] == 0:
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
					c.setRGB(t)

				else:
					c.setRGB((r * t[0], g * t[1], b * t[2]))
				
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