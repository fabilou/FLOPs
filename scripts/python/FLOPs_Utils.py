import hou
import math

def __colorTempToRGB(temperature):
	t = temperature / 100
	
	# Calculate red
	if t <= 66:
		r = 1.0
	else:
		r = t - 60
		r = 329.698727446 * (r ** -0.1332047592)
		r = max(0, min(1, r / 255))
	
	# Calculate green
	if t <= 66:
		g = t
		g = 99.4708025861 * math.log(g) - 161.1195681661
	else:
		g = t - 60
		g = 288.1221695283 * (g ** -0.0755148492)
	g = max(0, min(1, g / 255))
	
	# Calculate blue
	if t >= 66:
		b = 1.0
	elif t <= 19:
		b = 0.0
	else:
		b = t - 10
		b = 138.5177312231 * math.log(b) - 305.0447927307
		b = max(0, min(1, b / 255))
	
	return (r, g, b)