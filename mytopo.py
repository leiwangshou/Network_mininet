#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost, Controller, RemoteController
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

h = []
s = []

class myTopo(Topo):
	"Create a virtual network with performance settings"
	"total 12 switches, with one host per switch"
	def build(self, n=2):
		for i in range(1, n+1):
			h.append(self.addHost('h%s' % i, ip='10.0.0.%s' % i, mac='00:00:00:00:00:0%s' % format(i, 'x')))
			s.append(self.addSwitch('s%s' % i))
		for i in range(n):
			self.addLink(h[i], s[i])
		"connect among switches A, B, C, D"	
		for i in range(4):
			for j in range(1,4):
				if(i < j):
					self.addLink(s[i], s[j])
		"connect switches B and E"
		self.addLink(s[1], s[4])
		"connect among switches E, F, G"	
		for i in range(4, 7):
			for j in range(5, 7):
				if(i < j):
					self.addLink(s[i], s[j])
		"connect among switches G, H, I, J"	
		for i in range(6, 10):
			for j in range(7,10):
				if(i < j):
					self.addLink(s[i], s[j])
		"connect among switches F, K, L"
		self.addLink(s[5], s[10])
		self.addLink(s[5], s[11])
		self.addLink(s[10], s[11])

def netTest(n):
	"create network and run simple ping test"
	topo = myTopo(n)
	net = Mininet(topo)
	#adding controller
        floodlight = net.addController(name='floodlight' ,
                             controller=RemoteController,
                             ip='192.168.53.3',
                             port=6653)
	net.start()
	#print "Dumping host connections"
	#dumpNodeConnections(net.hosts)
	#set ARP table to each host
	for i in range(n):
		harp = net.get(h[i])
		for j in range(1, n+1):
			if ((i+1) != j):
				harp.cmd('arp -s 10.0.0.%s 00:00:00:00:00:0%s' % (j, format(j, 'x')))
	print "Testing network connectivity"
	CLI(net)
	net.stop()

if __name__ == '__main__':
	# Tell mininet to print useful information
	setLogLevel('info')
	netTest(12)
			