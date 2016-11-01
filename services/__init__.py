from flask import Flask, render_template, request, url_for
from flask import jsonify
from db_operation import *
from flask import Blueprint

s_s = Blueprint('s_s', __name__)

@s_s.route('/a/userdetails', methods=['POST','GET'])
def app_A():
	#print request.method, request.args
	userid = request.args.get('userid')
	print "---------Hi1------------"
	print userid
	try:
		response = get_userdetail("A",userid)
	except:
		response = {"status":"User Not Found"}
	return jsonify(**response)

@s_s.route('/a/userdetails/ping', methods=['POST','GET'])
def app_A_ping():
	print request.args, request.form
	if request.args:
		msgid = request.args.get('msgid')
		msgdata = request.args.get('msgdata')
	if request.form:
		msgid = request.form.get('msgid')
		msgdata = request.form.get('msgdata')
	print msgid, msgdata
	try:
		store_msg("A",{"msgid":msgid,"msgdata":msgdata})
		response = {"Status":"Success"}
	except:
		response = {"Status":"Failed"}
	return jsonify(**response)


@s_s.route('/b/userdetails', methods=['POST','GET'])
def app_B():
	#print request.method, request.args
	userid = request.args.get('userid')
	print "---------Hi1------------"
	print userid
	try:
		response = get_userdetail("B",userid)
	except:
		response = {"status":"User Not Found"}
	return jsonify(**response)

@s_s.route('/b/userdetails/ping', methods=['POST','GET'])
def app_B_ping():
	print request.args, request.form
	if request.args:
		msgid = request.args.get('msgid')
		msgdata = request.args.get('msgdata')
	if request.form:
		msgid = request.form.get('msgid')
		msgdata = request.form.get('msgdata')
	print msgid, msgdata
	try:
		store_msg("B",{"msgid":msgid,"msgdata":msgdata})
		response = {"Status":"Success"}
	except:
		response = {"Status":"Failed"}
	return jsonify(**response)


@s_s.route('/c/userdetails', methods=['POST','GET'])
def app_C():
	#print request.method, request.args
	userid = request.args.get('userid')
	print "---------Hi1------------"
	print userid
	try:
		response = get_userdetail("C",userid)
	except:
		response = {"status":"User Not Found"}
	return jsonify(**response)

@s_s.route('/c/userdetails/ping', methods=['POST','GET'])
def app_C_ping():
	print request.args, request.form
	if request.args:
		msgid = request.args.get('msgid')
		msgdata = request.args.get('msgdata')
	if request.form:
		msgid = request.form.get('msgid')
		msgdata = request.form.get('msgdata')
	print msgid, msgdata
	try:
		store_msg("C",{"msgid":msgid,"msgdata":msgdata})
		response = {"Status":"Success"}
	except:
		response = {"Status":"Failed"}
	return jsonify(**response)

@s_s.route('/d/userdetails', methods=['POST','GET'])
def app_D():
	#print request.method, request.args
	userid = request.args.get('userid')
	print "---------Hi1------------"
	print userid
	try:
		response = get_userdetail("D",userid)
	except:
		response = {"status":"User Not Found"}
	return jsonify(**response)

@s_s.route('/d/userdetails/ping', methods=['POST','GET'])
def app_D_ping():
	print request.args, request.form
	if request.args:
		msgid = request.args.get('msgid')
		msgdata = request.args.get('msgdata')
	if request.form:
		msgid = request.form.get('msgid')
		msgdata = request.form.get('msgdata')
	print msgid, msgdata
	try:
		store_msg("D",{"msgid":msgid,"msgdata":msgdata})
		response = {"Status":"Success"}
	except:
		response = {"Status":"Failed"}
	return jsonify(**response)

