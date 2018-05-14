#!/usr/bin/python
import sys
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Link
from net import Mininet_xia
from node import Node_xia

def topology():
	"Create a network"

	net = Mininet_xia(controller=None)

	info("*** creating nodes\n")

	xia1 = net.addXia('xia1', hid= 'a,b' , ethid='eth0, eth1')
	xia2 = net.addXia('xia2' )
	xia3 = net.addXia('xia3' )
	net.addLink( xia1 , xia2 )
	net.addLink( xia1 , xia3 )
	
	
	info("*** starting network \n")
	net.build()

	
	CLI(net)

	info("*** stopping network\n")
	net.stop()
	
if __name__ == '__main__':
	setLogLevel('info')
	topology()

