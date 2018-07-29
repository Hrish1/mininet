#!/usr/bin/env python

"""
Test for echoxp.py

It's important to note here that XIA's ability is heavily centered
around the principals chosen and the corresponding identifiers. Through
the test below we ensure the proper configurtion of Host Identifiers.
"""

import unittest
import pexpect

class testEchoxp( unittest.TestCase ):

    prompt = 'mininet>'

    def testHid( self ):
        "Check if the HIDs are configured"
        p = pexpect.spawn( 'python -m mininet.examples.echoxp' )
        p.expect( self.prompt )
        hosts = [ 'xia1', 'xia2' ]
        cmd = ' xip hid showaddrs'
        # HID test
        for host in hosts:
            hcmd = host + cmd
            p.sendline( hcmd )
            p.expect ( 'to hid-([a-f0-9]+)' )
            xid = p.match.group( 1 ) if p.match else None
            xidlength = len( xid )
            self.assertEqual( xidlength, 40 )
            p.expect( self.prompt )

        p.sendline( 'exit' )
        p.wait()

if __name__ == '__main__':
    unittest.main()
