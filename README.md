# Cubex-Network Core Wallet

Cubex-Network Core staging tree 1.0.0.0
===============================

https://www.cubexcoin.net


What is Cubex-Network?
----------------

Cubex is an experimental new digital currency that enables anonymous, instant
payments to anyone, anywhere in the world. Cubex-Network uses peer-to-peer technology
to operate with no central authority: managing transactions and issuing money
are carried out collectively by the network. Cubex-Network Core is the name of the open
source software which enables the use of this currency.

For more information, as well as an immediately useable, binary version of
the Cubex-Network Core software, see https://www.cubexcoin.net | https://github.com/cubex-network/cubex/releases.

##  Cubex-Network Specifications:

       Ticker: CUB
       Algorithm: X11
       Masternode colletral: 10000 CUB
       Masternode rewards: 75%
       Block reward till block: 2880 - 1 CUB
       Block reward: 300
       Block Timer: 60 seconds
       Maturity: 50 blocks
       Max supply: 21 000 000 CUB

License
-------

Cubex Core is released under the terms of the MIT license. See [COPYING](https://github.com/cubex-network/cubex/blob/master/COPYING) for more
information or see https://opensource.org/licenses/MIT.

Development Process
-------------------

The `master` branch is meant to be stable. Development is normally done in separate branches.
[Tags](https://github.com/cubex-network/cubex/tags) are created to indicate new official,
stable release versions of Cubex-Network Core.

The contribution workflow is described in [CONTRIBUTING.md](https://github.com/cubex-network/cubex/blob/master/CONTRIBUTING.md).

Testing
-------

Testing and code review is the bottleneck for development; we get more pull
requests than we can review and test on short notice. Please be patient and help out by testing
other people's pull requests, and remember this is a security-critical project where any mistake might cost people
lots of money.

### Automated Testing

Developers are strongly encouraged to write [unit tests](/doc/unit-tests.md) for new code, and to
submit new unit tests for old code. Unit tests can be compiled and run
(assuming they weren't disabled in configure) with: `make check`

There are also [regression and integration tests](/qa) of the RPC interface, written
in Python, that are run automatically on the build server.
These tests can be run (if the [test dependencies](/qa) are installed) with: `qa/pull-tester/rpc-tests.py`


### Manual Quality Assurance (QA) Testing

Changes should be tested by somebody other than the developer who wrote the
code. This is especially important for large or high-risk changes. It is useful
to add a test plan to the pull request description if testing the changes is
not straightforward.

Translations
------------

Changes to translations as well as new translations can be submitted to
[Cubex-Network Core's Discord Page](https://discord.gg/QHjwumq).


**Important**: We do not accept translation changes as GitHub pull requests.

## Donate CUB to support this project
###### Donation address: CVa72Tuicm3C9KCmLXbZUdcG6mJJoRwQUg

> Copyright © 2018 Cubex Network
