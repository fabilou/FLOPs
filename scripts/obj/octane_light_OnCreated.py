import hou
import traceback
import FLOPs_Utils as flops

def updateNodeColor(node, event_type, **kwargs):
	parmTuple = kwargs["parm_tuple"]

	if parmTuple is not None:
		c = hou.Color((0.8, 0.8, 0.8))

		if any(parmTuple.name() == x for x in ["blackbody_efficiency_color_A_VALUE", "emission_efficiency_color_A_VALUE", "NT_EMIS_BLACKBODY1_temperature","switch"]):
			
			if node.parm("switch").eval() == 0:
				r = node.parm("blackbody_efficiency_color_A_VALUEr").eval()
				g = node.parm("blackbody_efficiency_color_A_VALUEg").eval()
				b = node.parm("blackbody_efficiency_color_A_VALUEb").eval()

				t = flops.__colorTempToRGB(node.parm("NT_EMIS_BLACKBODY1_temperature").eval())

				c.setRGB((r * t[0], g * t[1], b * t[2]))

			else:
				r = node.parm("emission_efficiency_color_A_VALUEr").eval()
				g = node.parm("emission_efficiency_color_A_VALUEg").eval()
				b = node.parm("emission_efficiency_color_A_VALUEb").eval()
				
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
				if node.parm("switch").eval() == 0:
					r = node.parm("blackbody_efficiency_color_A_VALUEr").eval()
					g = node.parm("blackbody_efficiency_color_A_VALUEg").eval()
					b = node.parm("blackbody_efficiency_color_A_VALUEb").eval()

					t = flops.__colorTempToRGB(node.parm("NT_EMIS_BLACKBODY1_temperature").eval())

					c.setRGB((r * t[0], g * t[1], b * t[2]))

				else:
					r = node.parm("emission_efficiency_color_A_VALUEr").eval()
					g = node.parm("emission_efficiency_color_A_VALUEg").eval()
					b = node.parm("emission_efficiency_color_A_VALUEb").eval()
					
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