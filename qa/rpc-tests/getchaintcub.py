#!/usr/bin/env python2
# Copyright (c) 2014 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

# Exercise the getchaintcub API.  We introduce a network split, work
# on chains of different lengths, and join the network together again.
# This gives us two tcub, verify that it works.

from test_framework import BitcoinTestFramework
from util import assert_equal

class GetChainTcubTest (BitcoinTestFramework):

    def run_test (self):
        BitcoinTestFramework.run_test (self)

        tcub = self.nodes[0].getchaintcub ()
        assert_equal (len (tcub), 1)
        assert_equal (tcub[0]['branchlen'], 0)
        assert_equal (tcub[0]['height'], 200)
        assert_equal (tcub[0]['status'], 'active')

        # Split the network and build two chains of different lengths.
        self.split_network ()
        self.nodes[0].setgenerate (True, 10);
        self.nodes[2].setgenerate (True, 20);
        self.sync_all ()

        tcub = self.nodes[1].getchaintcub ()
        assert_equal (len (tcub), 1)
        shortTip = tcub[0]
        assert_equal (shortTip['branchlen'], 0)
        assert_equal (shortTip['height'], 210)
        assert_equal (tcub[0]['status'], 'active')

        tcub = self.nodes[3].getchaintcub ()
        assert_equal (len (tcub), 1)
        longTip = tcub[0]
        assert_equal (longTip['branchlen'], 0)
        assert_equal (longTip['height'], 220)
        assert_equal (tcub[0]['status'], 'active')

        # Join the network halves and check that we now have two tcub
        # (at least at the nodes that previously had the short chain).
        self.join_network ()

        tcub = self.nodes[0].getchaintcub ()
        assert_equal (len (tcub), 2)
        assert_equal (tcub[0], longTip)

        assert_equal (tcub[1]['branchlen'], 10)
        assert_equal (tcub[1]['status'], 'valid-fork')
        tcub[1]['branchlen'] = 0
        tcub[1]['status'] = 'active'
        assert_equal (tcub[1], shortTip)

if __name__ == '__main__':
    GetChainTcubTest ().main ()
