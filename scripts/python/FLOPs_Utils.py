import hou
import math

def __colorTempToRGB(temp):
	temp = temp / 100
	
	# Calculate red
	if temp <= 66:
		red = 1.0
	else:
		red = temp - 60
		red = 329.698727446 * (red ** -0.1332047592)
		red = max(0, min(1, red / 255))
	
	# Calculate green
	if temp <= 66:
		green = temp
		green = 99.4708025861 * math.log(green) - 161.1195681661
	else:
		green = temp - 60
		green = 288.1221695283 * (green ** -0.0755148492)
	green = max(0, min(1, green / 255))
	
	# Calculate blue
	if temp >= 66:
		blue = 1.0
	elif temp <= 19:
		blue = 0.0
	else:
		blue = temp - 10
		blue = 138.5177312231 * math.log(blue) - 305.0447927307
		blue = max(0, min(1, blue / 255))
	
	return (red, green, blue)




def setLightColor(node):
	color = hou.Color()

	# Redshift
	if (node.type().name() == "rslight"):
		r = node.parm("light_colorr").eval()
		g = node.parm("light_colorg").eval()
		b = node.parm("light_colorb").eval()
			
		temp = __colorTempToRGB(node.parm("Light1_temperature").eval())

		if (node.parm("Light1_colorMode").eval() == "0"):
			color.setRGB((r, g, b))

		elif (node.parm("Light1_colorMode").eval() == "1"):
			color.setRGB(temp)

		else:
			color.setRGB((r * temp[0], g * temp[1], b * temp[2]))

		node.setColor(color)

	elif (node.type().name() == "rslightdome::2.0"):
		r = node.parm("light_colorr").eval()
		g = node.parm("light_colorg").eval()
		b = node.parm("light_colorb").eval()
		color.setRGB((r, g, b))
		node.setColor(color)

	elif (node.type().name() == "rslightsun"):
		r = node.parm("PhysicalSky1_sun_tintr").eval()
		g = node.parm("PhysicalSky1_sun_tintg").eval()
		b = node.parm("PhysicalSky1_sun_tintb").eval()
		color.setRGB((r, g, b))
		node.setColor(color)

	#Octane
	elif (node.type().name() == "octane_light"):
		if (node.parm("switch").eval() == 0):
			colorTemp = __colorTempToRGB(node.parm("NT_EMIS_BLACKBODY1_temperature").eval())
			
			r = node.parm("blackbody_efficiency_color_A_VALUEr").eval() * colorTemp[0]
			g = node.parm("blackbody_efficiency_color_A_VALUEg").eval() * colorTemp[1]
			b = node.parm("blackbody_efficiency_color_A_VALUEb").eval() * colorTemp[2]
			color.setRGB((r, g, b))
			node.setColor(color)

		else:
			r = node.parm("emission_efficiency_color_A_VALUEr").eval()
			g = node.parm("emission_efficiency_color_A_VALUEg").eval()
			b = node.parm("emission_efficiency_color_A_VALUEb").eval()
			color.setRGB((r, g, b))
			node.setColor(color)

	elif (node.type().name() == "octane_universalLight"):
		if (node.parm("UI_Emission_Type").eval() == 1):
			colorTemp = __colorTempToRGB(node.parm("Emission_BlackBody_temperature").eval())
			
			r = node.parm("Color_RGB_A_VALUEr").eval() * colorTemp[0]
			g = node.parm("Color_RGB_A_VALUEg").eval() * colorTemp[1]
			b = node.parm("Color_RGB_A_VALUEb").eval() * colorTemp[2]
			color.setRGB((r, g, b))
			node.setColor(color)

		else:
			r = node.parm("Color_RGB_A_VALUEr").eval()
			g = node.parm("Color_RGB_A_VALUEg").eval()
			b = node.parm("Color_RGB_A_VALUEb").eval()
			color.setRGB((r, g, b))
			node.setColor(color)

	elif (node.type().name() == "octane_toonLight"):
		r = node.parm("light_colorr").eval()
		g = node.parm("light_colorg").eval()
		b = node.parm("light_colorb").eval()
		color.setRGB((r, g, b))
		node.setColor(color)

	# Houdini Lights
	elif any(node.type().name() == x for x in ["envlight", "hlight::2.0", "indirectlight", "ambient"]):
		r = node.parm("light_colorr").eval()
		g = node.parm("light_colorg").eval()
		b = node.parm("light_colorb").eval()
		color.setRGB((r, g, b))
		node.setColor(color)