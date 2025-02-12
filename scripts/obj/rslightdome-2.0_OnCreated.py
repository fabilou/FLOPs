import hou
import traceback

def updateNodeColor(node, event_type, **kwargs):
	parmTuple = kwargs["parm_tuple"]

	if parmTuple is not None:
	
		c = hou.Color()

		r = node.parm("light_colorr").eval()
		g = node.parm("light_colorg").eval()
		b = node.parm("light_colorb").eval()
		
		if parmTuple.name() == "light_color":
			c.setRGB((r, g, b))

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
				c.setRGB((r, g, b))
				
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