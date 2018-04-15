#!/usr/bin/python
import sys
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Link
from net import Mininet_xia
from node import Node_xia
from plotEd import TopologyVisualiser as tviz

def topology():
	"Create a network"

	net = Mininet_xia(controller=None)

	info("*** creating nodes\n")

	xia1 = net.addHost('h1' )
	xia2 = net.addHost('h2' )
	xia3 = net.addHost('h3' )
	xia4 = net.addHost('h4' )
	net.addLink( xia1 , xia2 )
	net.addLink( xia1 , xia3 )
	net.addLink( xia1,  xia4 )
	
	info("*** starting network \n")
	net.build()
	tviz(net.hosts,net.links)
	
	CLI(net)

	
	info("*** stopping network\n")
	net.stop()
	
if __name__ == '__main__':
	setLogLevel('info')
	topology()

