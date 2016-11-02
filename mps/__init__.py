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


@m_s.route('/demo/sendmsg', methods=['POST','GET'])
def demo():
        return render_template('demo.html')

@m_s.route('/demo/viewmsg', methods=['POST','GET'])
def demo1():
        c = get_msg("B")
        code = "<h3> Messages Received By Service B </h3> <ul>"
        for elem in c:
                code = code + "<li>" + elem[1] + " : " +elem[2] + "</li>"
        code =  code + "</ul>"
        code = code + "<h3> Messages Received By Service C </h3> <ul>"
        c = get_msg("C")
        for elem in c:
                code = code + "<li>" + elem[1] + " : " +elem[2] + "</li>"
        code =  code + "</ul>"
        code = code + "<h3> Messages Received By Service D </h3> <ul>"
        c = get_msg("D")
        for elem in c:
                code = code + "<li>" + elem[1] + " : " +elem[2] + "</li>"
        code =  code + "</ul>"
        return code

@m_s.route('/demo',methods=['POST','GET'])
def demo2():
        c="<body><p><a href='http://raviranjan.xyz/demo/sendmsg' target='_blank'>Send Message</a></p><p><a href='http://raviranjan.xyz/demo/viewmsg' target='_blank'>Show Received Messages By Services</a></p></body>"
        return c