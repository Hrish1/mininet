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
	HID = '7ac27f90663ef36da12cfcc37c9a6bb6b85dec96'
	xia1 = net.addXia('xia1', hid= 'a,b' , ethid='  eth0,    eth1')
	xia2 = net.addXia('xia2', hidneigh={'ppalid':HID, 'intf':'eth0'} )
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

