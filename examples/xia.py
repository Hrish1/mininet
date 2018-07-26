#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Host, XIAHost
from mininet.nodelib import LinuxBridge
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class LinuxRouter( Host ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

def xiamultippal():
    "A large experiment to demonstrate co-existence of TCP/IP and XIA"
    net = Mininet( controller=None )
    info( '*** Adding hosts\n' )

    r1 = net.addHost( 'r1', cls=LinuxRouter, ip='172.16.0.1/16' )
    r2 = net.addHost( 'r2', cls=LinuxRouter, ip='192.168.100.1/24' )

    br1 = net.addSwitch( 'br1', cls=LinuxBridge )
    br2 = net.addSwitch( 'br2', cls=LinuxBridge )

    net.addLink( br1, r1, params2={ 'ip': '172.16.0.1/16' } )
    net.addLink( br2, r2, params2={ 'ip': '192.168.100.1/24' } )
    net.addLink( r1, r2, params1={ 'ip': '10.0.0.1/8' }, params2={ 'ip': '10.0.0.2/8' } )

    xia1 = net.addHost( 'xia1', cls=XIAHost, ip='172.16.0.2/16', defaultRoute='via 172.16.0.1',
                        u4id={ 'ipaddr': '172.16.0.2', 'port': '0x52a3', 'tunnel': True }, xdp=True, hid=[ 'xia1_hid1' ] )
    xia2 = net.addHost( 'xia2', cls=XIAHost, ip='172.16.0.3/16', defaultRoute='via 172.16.0.1' )
    xia3 = net.addHost( 'xia3', cls=XIAHost, ip='192.168.100.2/24', defaultRoute='via 192.168.100.1',
                        u4id={ 'ipaddr': '192.168.100.2', 'port': '0x52a1', 'tunnel': True }, xdp=True, hid=[ 'xia3_hid1' ] )

    for s,d in [ ( xia1, br1 ), ( xia2, br1 ), ( xia3, br2 ) ]:
        net.addLink( s, d )

    r1.cmd( 'ip route add 192.168.100.0/24 via 10.0.0.2 src 10.0.0.1' )
    r2.cmd( 'ip route add 172.16.0.0/16 via 10.0.0.1 src 10.0.0.2' )

    info( '*** Starting network\n')
    net.start()
    CLI( net )
    info( '*** Stopping network' )
    net.stop()


if __name__=='__main__':
    setLogLevel( 'info' )
    xiamultippal()
