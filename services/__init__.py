from flask import Flask, render_template, request, url_for
from flask import jsonify
from db_operation import *
from flask import Blueprint

s_s = Blueprint('s_s', __name__)


@s_s.route('/a/userdetails/ping', methods=['POST'])
def app_A_ping():
    if request.args:
        msgid = request.args.get('msgid')
        msgdata = request.args.get('msgdata')
    if request.form:
        msgid = request.form.get('msgid')
        msgdata = request.form.get('msgdata')
    try:
        store_msg("A", {"msgid": msgid, "msgdata": msgdata})
        response = {"Status": "Success"}
    except:
        response = {"Status": "Failed"}
    return jsonify(**response)


@s_s.route('/b/userdetails/ping', methods=['POST'])
def app_B_ping():
    if request.args:
        msgid = request.args.get('msgid')
        msgdata = request.args.get('msgdata')
    if request.form:
        msgid = request.form.get('msgid')
        msgdata = request.form.get('msgdata')
    try:
        store_msg("B", {"msgid": msgid, "msgdata": msgdata})
        response = {"Status": "Success"}
    except:
        response = {"Status": "Failed"}
    return jsonify(**response)


@s_s.route('/c/userdetails/ping', methods=['POST'])
def app_C_ping():
    if request.args:
        msgid = request.args.get('msgid')
        msgdata = request.args.get('msgdata')
    if request.form:
        msgid = request.form.get('msgid')
        msgdata = request.form.get('msgdata')
    try:
        store_msg("C", {"msgid": msgid, "msgdata": msgdata})
        response = {"Status": "Success"}
    except:
        response = {"Status": "Failed"}
    return jsonify(**response)


@s_s.route('/d/userdetails/ping', methods=['POST'])
def app_D_ping():
    if request.args:
        msgid = request.args.get('msgid')
        msgdata = request.args.get('msgdata')
    if request.form:
        msgid = request.form.get('msgid')
        msgdata = request.form.get('msgdata')
    try:
        store_msg("D", {"msgid": msgid, "msgdata": msgdata})
        response = {"Status": "Success"}
    except:
        response = {"Status": "Failed"}
    return jsonify(**response)
