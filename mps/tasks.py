from celery import Celery
from db_operation import *
import requests, json, traceback


cel = Celery('tasks', backend='rpc://', broker='amqp://guest@localhost//')
baseurl = "http://localhost:5000/"

@cel.task
def sendmsg(endpoint,msgid,msgdata):
	url = baseurl + endpoint + "/ping"
	payload = {"msgid":msgid,'msgdata':msgdata}
	flag =0
	for x in range(1,4):
		try:
			r = requests.post(url,data=payload)
			print r.text
			data = json.loads(r.text)
			if data["Status"] == "Success":
				print "Succesful"
				flag =1
				break
		except:
			traceback.print_exc()
			flag =0
			pass
	if flag ==1:
		return 1
	else:
		print "Failed"
		sendemail(endpoint,msgid,msgdata)
		return 0


def sendemail(endpoint,msgid,msgdata):
	print "sending email"
	pass
