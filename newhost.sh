py net.addHost('h13')
py net.addSwitch('s13')
py net.addLink('s13', 'h13')
py s13.attach('s13-eth1')
py net.addLink('s13', 's12')
py s13.attach('s13-eth2')
py s12.attach('s12-eth4')
py net.get('h13').setMAC('00:00:00:00:00:0d')
py net.get('h13').setIP('10.0.0.13')
py net.get('h13').cmd('ifconfig h13-eth0 10.0.0.13')
py net.get('h1').cmd('arp -s 10.0.0.13 00:00:00:00:00:0d')
py net.get('h2').cmd('arp -s 10.0.0.13 00:00:00:00:00:0d')
py net.get('h3').cmd('arp -s 10.0.0.13 00:00:00:00:00:0d')
py net.get('h4').cmd('arp -s 10.0.0.13 00:00:00:00:00:0d')
py net.get('h5').cmd('arp -s 10.0.0.13 00:00:00:00:00:0d')
py net.get('h6').cmd('arp -s 10.0.0.13 00:00:00:00:00:0d')
py net.get('h7').cmd('arp -s 10.0.0.13 00:00:00:00:00:0d')
py net.get('h8').cmd('arp -s 10.0.0.13 00:00:00:00:00:0d')
py net.get('h9').cmd('arp -s 10.0.0.13 00:00:00:00:00:0d')
py net.get('h10').cmd('arp -s 10.0.0.13 00:00:00:00:00:0d')
py net.get('h11').cmd('arp -s 10.0.0.13 00:00:00:00:00:0d')
py net.get('h12').cmd('arp -s 10.0.0.13 00:00:00:00:00:0d')
py net.get('h13').cmd('arp -s 10.0.0.1 00:00:00:00:00:01')
py net.get('h13').cmd('arp -s 10.0.0.2 00:00:00:00:00:02')
py net.get('h13').cmd('arp -s 10.0.0.3 00:00:00:00:00:03')
py net.get('h13').cmd('arp -s 10.0.0.4 00:00:00:00:00:04')
py net.get('h13').cmd('arp -s 10.0.0.5 00:00:00:00:00:05')
py net.get('h13').cmd('arp -s 10.0.0.6 00:00:00:00:00:06')
py net.get('h13').cmd('arp -s 10.0.0.7 00:00:00:00:00:07')
py net.get('h13').cmd('arp -s 10.0.0.8 00:00:00:00:00:08')
py net.get('h13').cmd('arp -s 10.0.0.9 00:00:00:00:00:09')
py net.get('h13').cmd('arp -s 10.0.0.10 00:00:00:00:00:0a')
py net.get('h13').cmd('arp -s 10.0.0.11 00:00:00:00:00:0b')
py net.get('h13').cmd('arp -s 10.0.0.12 00:00:00:00:00:0c')
py s13.start(net.controllers)