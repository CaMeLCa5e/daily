import urllib.request
import os 
import time

path = "users/j/documents/yahooData"

def check_yahoo():
	# headers = {}
	statspath = path+"/_KeyStats"
	stock_list = [x[0] for x in os.walk(statspath)]

	for e in stock_list[1:]:
		try:
			e = e.replace("users/j/documents/yahooData", "")
			link = "http://finance.yahoo.com/q/ks?s="+e.upper()+"+Key+Statistics"
			resp = urllib.request.urlopen(link).read()

			save = "forward/" +str(e)+".html"
			store = open(save, "w")
			store.write(str(resp))
			store.close()

		except Exception as e:
			print str(e)
			time.sleep(2)

check_yahoo()