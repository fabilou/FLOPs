import hou
import traceback

try:
	node = kwargs["node"]

	if node is not None:
		node.parm("prerender").setExpression("import hou\nimport datetime\nnow = datetime.datetime.now()\nd = now.strftime('%Y%m%d')\nt = now.strftime('%H%M%S')\nhou.putenv('DATE', d)\nhou.putenv('TIME', t)", hou.exprLanguage.Python, True)
		node.parm("lprerender").set("python")

except:
	print(traceback.format_exc())