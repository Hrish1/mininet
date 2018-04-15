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
        graphml.set("xsi:schemaLocation",
                    "http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd")

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

        #link = ET.SubElement(graph, "edge", id="e0")
        #link.set("source", "n0")
        #link.set("target", "n1")
        #link = ET.SubElement(graph, "edge", id="e1")
        #link.set("source", "n0")
        #link.set("target", "n2")

        Tree = ET.ElementTree(graphml)
        filename = os.path.basename(sys.argv[0])
        Tree.write(filename.split(".py", 1)[0] + ".graphml", encoding="UTF-8")


