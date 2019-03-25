import httplib
import json

#flow rules for total 13 switches in this loop topology
#these flow rules make connections in non-loop way

class StaticFlowPusher(object):
  
    def __init__(self, server):
        self.server = server
  
    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
  
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
  
    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200
  
    def rest_call(self, data, action):
        path = '/wm/staticflowpusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret
  
pusher = StaticFlowPusher('192.168.53.3')

#flow rules for switch s1
table1 = [1]
for i in range (1, 13):
	table1.append(2)

#flow rules for switch s2
table2 = [2, 1, 3, 3]
for i in range (4, 13):
	table2.append(5)

#flow rules for switch s3
table3 = [3, 3, 1, 4]
for i in range (4, 13):
	table3.append(3)

#flow rules for switch s4
table4 = [4, 4, 4, 1]
for i in range (4, 13):
	table4.append(4)

#flow rules for switch s5
table5 = []
for i in range(4):
	table5.append(2)
table5.append(1)
for i in range(5, 13):
	table5.append(3)

#flow rules for switch s6
table6 = []
for i in range(5):
	table6.append(2)
table6.append(1)
for i in range(6, 10):
	table6.append(3)
table6.append(4)
table6.append(4)
table6.append(4)

#flow rules for switch s7
table7 = []
for i in range(6):
	table7.append(3)
table7.append(1)
for i in range(7, 10):
	table7.append(4)
table7.append(3)
table7.append(3)
table7.append(3)	

#flow rules for switch s8
table8 = []
for i in range(7):
	table8.append(2)
table8.append(1)
for i in range(8, 10):
	table8.append(3)
table8.append(2)
table8.append(2)
table8.append(2)

#flow rules for switch s9
table9 = []
for i in range(8):
	table9.append(3)
table9.append(1)
table9.append(4)
table9.append(3)
table9.append(3)
table9.append(3)

#flow rules for switch s10
table10 = []
for i in range(9):
	table10.append(4)
table10.append(1)
table10.append(4)
table10.append(4)
table10.append(4)

#flow rules for switch s11
table11 = []
for i in range(10):
	table11.append(2)
table11.append(1)
table11.append(3)
table11.append(3)

#flow rules for switch s12
table12 = []
for i in range(11):
	table12.append(3)
table12.append(1)
table12.append(4)

#flow rules for switch s13
table13 = []
for i in range(12):
	table13.append(2)
table13.append(1)
	
ttable = [table1, table2, table3, table4, table5, table6, table7, table8, table9, table10, table11, table12, table13]

b=0
#set flow rules for switch s1 to s13
for i in range(1, 14):
	for j in range(1, 14):
		b += 1
		flow = {
		'switch':"00:00:00:00:00:00:00:0%s" % (format(i,'x')),
		"name":"flow_mod_new_%s" % b,
		"ipv4_dst":"10.0.0.%s"% j,
		"eth_type":"0x0800",
		"cookie":"0", 
		"priority":"32768",
		"active":"true",
		"actions":"output=%s" % (ttable[i-1][j-1])
		}
		pusher.set(flow)

