from flask import Flask
from flask import jsonify
import requests, json, traceback
from flask import Blueprint
from tasks import sendmsg

from flask import render_template, request, url_for
from db_operation import *

m_s = Blueprint('m_s', __name__)

@m_s.route('/mps/acceptmsg', methods=['POST','GET'])
def message_pass():
	senders_endpoint = request.args.get('senders_endpoint')
	msgid = request.args.get('msgid')
	msgdata = request.args.get('msgdata')
	msg_dump(msgid,msgdata,senders_endpoint)	#storing all msg in db
	try:
		endpoints = get_endpoint(senders_endpoint) #get list of endpoints
		for elem in endpoints:
			sendmsg.delay(elem,msgid,msgdata)
		response = {"Status":"Success"}
		return jsonify(**response)
	except:
		response = {"Status":"Fail"}
		return jsonify(**response)