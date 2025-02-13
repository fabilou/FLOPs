import hou
import traceback
import FLOPs_Utils as flops

def updateNodeColor(node, event_type, **kwargs):
	parmTuple = kwargs["parm_tuple"]

	if parmTuple is not None:
		c = hou.Color()

		if any(parmTuple.name() == x for x in ["blackbody_efficiency_color_A_VALUE", "emission_efficiency_color_A_VALUE", "light_enabled", "NT_EMIS_BLACKBODY1_temperature","switch"]):
			if node.parm("light_enabled").eval() == 0:
				c.setRGB((0.1, 0.1, 0.1))

				try:
					node.setColor(c)
					node.setComment("off")
					node.setGenericFlag(hou.nodeFlag.DisplayComment, True)

				except:
					pass
			else:

				if node.parm("switch").eval() == 0:
					r, g, b = flops.getColorParm(node, "blackbody_efficiency_color_A_VALUE")
					tr, tg, tb = flops.getColorTempParm(node, "NT_EMIS_BLACKBODY1_temperature")
					c.setRGB((r * tr, g * tg, b * tb))

				else:
					r, g, b = flops.getColorParm(node, "emission_efficiency_color_A_VALUE")
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