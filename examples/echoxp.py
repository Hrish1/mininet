#!/usr/bin/python

"""
echoxp.py: test the echo application on two XIA hosts.
One XIA host acts as the echo server and the other as echo client.
The client sends a text or a file to the server which is echoed
back to the client.
"""

import sys
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Link
from mininet.net import Mininet
from mininet.node import XIAHost

def topology():
    "A topology for net-echo experiment"

    net = Mininet( controller=None )

    info( "*** creating nodes\n" )
    xia1 = net.addHost( 'xia1', cls=XIAHost, hid='foo', xdp=True )
    xia2 = net.addHost( 'xia2', cls=XIAHost, hid='bar', xdp=True )

    info("*** creating links\n")
    net.addLink( xia1, xia2 )

    info( "*** starting network \n" )
    net.build()
    CLI( net )

    info( "*** stopping network\n" )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
