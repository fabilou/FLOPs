import hou
import traceback
import FLOPs_Utils as flops

def updateNodeColor(node, event_type, **kwargs):
	parmTuple = kwargs["parm_tuple"]

	if parmTuple is not None:
	
		c = hou.Color()

		v = node.parm("A_VALUE").eval()
		
		if any(parmTuple.name() == x for x in ["A_VALUE"]):
			c.setRGB((v, v, v))

			try:
				node.setColor(c)

			except:
				pass

try:
	node = kwargs["node"]

	if node is not None:
		node.addEventCallback((hou.nodeEventType.ParmTupleChanged, ), updateNodeColor)

except:
	print(traceback.format_exc())