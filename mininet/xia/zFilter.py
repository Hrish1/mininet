#!/usr/bin/python

"""
zFilter.py: This example stores the Mininet topology for zFilter experiment.
The experiment will feature new and more specific functions as and when they are created.

h1-eth0:br1-eth1
	
h2-eth0:br1-eth2
	
h3-eth0:br1-eth3

h1 resembles the host, h2 resembles con0 and h3 resembles con1 of the original zFilter experiment

"""


from mininet.nodelib import LinuxBridge
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def zFilter():
	"The zFilter underlying topology"

	net = Mininet()
	
	info( '*** Adding hosts\n' )
	h1 = net.addHost( 'h1' )
    	h2 = net.addHost( 'h2' )
	h3 = net.addHost( 'h3' )
	
	info( '*** Adding switch\n' )
	br1 = net.addSwitch( 'br1', cls=LinuxBridge)

	info( '*** Adding links\n' )
	net.addLink( h1, br1 )
	net.addLink( h2, br1 )
	net.addLink( h3, br1 )

	info( '*** Starting network\n')
    	net.start()

    	info( '*** Running CLI\n' )
    	CLI( net )

    	info( '*** Stopping network' )
    	net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    zFilter()	



