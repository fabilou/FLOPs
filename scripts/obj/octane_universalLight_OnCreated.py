import hou
import traceback
import FLOPs_Utils as flops

def updateNodeColor(node, event_type, **kwargs):
	parmTuple = kwargs["parm_tuple"]

	if parmTuple is not None:
		c = hou.Color((0.8, 0.8, 0.8))

		r, g, b = flops.getColorParm(node, "Color_RGB_A_VALUE")

		tr, tg, tb = flops.getColorTempParm(node, "Emission_BlackBody_temperature")

		if any(parmTuple.name() == x for x in ["Color_RGB_A_VALUE", "Emission_BlackBody_temperature", "light_enabled"]):
			if node.parm("light_enabled").eval() == 0:
				c.setRGB((0.1, 0.1, 0.1))

				try:
					node.setColor(c)
					node.setComment("off")
					node.setGenericFlag(hou.nodeFlag.DisplayComment, True)

				except:
					pass

			else:
				if node.parm("UI_Emission_Type").eval() == 1:
						c.setRGB((r * tr, g * tg, b * tb))
			
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