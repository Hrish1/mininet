import os, sys
import xml.etree.cElementTree as ET


class TopologyVisualiser:

    def __init__(self, nodes, links={}):
        # Links need to be added
        self.nodes = nodes
        self.links = links
        self.buildElements()

    def setNode(self, node):

        Node = ET.Element("node", id=node)
        data = ET.SubElement(Node, "data", key=node)
        shapeNode = ET.SubElement(data, "y:ShapeNode")
        Fill = ET.SubElement(shapeNode, "y:Fill")
        Fill.set("color", "#FF0000")

        return Node

    def setLink(self, sourceIntf, targetIntf, linkId):

        source = sourceIntf.node.name
        target = targetIntf.node.name
        Link = ET.Element("edge", id=linkId)
        Link.set("source", source)
        Link.set("target", target)

        return Link

    def buildElements(self):

        graphml = ET.Element("graphml", xmlns="http://graphml.graphdrawing.org/xmlns")
        graphml.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        # graphml.set("xsi:schemaLocation",
        #            "http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd")
        graphml.set("xsi:schemaLocation",
                    "http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd")
        graphml.set("xmlns:java", "http://www.yworks.com/xml/yfiles-common/1.0/java")
        graphml.set("xmlns:sys", "http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0")
        graphml.set("xmlns:x", "http://www.yworks.com/xml/yfiles-common/markup/2.0")
        graphml.set("xmlns:y", "http://www.yworks.com/xml/graphml")
        graphml.set("xmlns:yed", "http://www.yworks.com/xml/yed/3")

        nodeKey = ET.SubElement(graphml, "key", id="d0")
        nodeKey.set("for", "node")
        nodeKey.set("yfiles.type", "nodegraphics")

        edgeKey = ET.SubElement(graphml, "key", id="d1")
        edgeKey.set("for", "edge")
        edgeKey.set("yfiles.type", "edgegraphics")

        graph = ET.SubElement(graphml, "graph", id="G")
        graph.set("edgedefault", "undirected")
        # node = ET.SubElement(graph ,"node", id="n0")
        # node = ET.SubElement(graph ,"node", id="n1")
        # node = ET.SubElement(graph ,"node", id="n2")

        for node in self.nodes:
            Node = self.setNode(node.__str__())
            graph.append(Node)

        for link in self.links:
            Link = self.setLink(link.intf1, link.intf2, link.__str__())
            graph.append(Link)

        # link = ET.SubElement(graph, "edge", id="e0")
        # link.set("source", "n0")
        # link.set("target", "n1")
        # link = ET.SubElement(graph, "edge", id="e1")
        # link.set("source", "n0")
        # link.set("target", "n2")

        Tree = ET.ElementTree(graphml)
        filename = os.path.basename(sys.argv[0])
        Tree.write(filename.split(".py", 1)[0] + ".graphml", encoding="UTF-8")


