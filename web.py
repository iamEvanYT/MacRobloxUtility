from utils.roblox import *
from utils.LoadFFlags import loadFFLags
from flags.fflags_updater import getFflagsData
from flask import Flask, jsonify
from flask_cors import CORS
from utils.constants import *
import re

app = Flask(__name__)

CORS(app)

@app.route("/", methods=["GET"])
def index():
    return jsonify({'status': 'ok'})

@app.route("/openRoblox", methods=["GET"])
def open_roblox_route():
    try:
        open_roblox()
        return jsonify({'message': "success"})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route("/closeRoblox", methods=["GET"])
def close_roblox_route():
    try:
        close_roblox()
        return jsonify({'message': "success"})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route("/getConfigFFlags", methods=["GET"])
def get_config_fflags_route():
    try:
        fflags = getFflagsData()
        return jsonify({'fflags': fflags})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route("/getFFlags", methods=["GET"])
def get_fflags_route():
    try:
        fflags =  loadFFLags()
        return jsonify({'fflags': fflags})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route("/getParsedFFLags", methods=["GET"])
def getParsedFFLags():
    try:
        fflags =  loadFFLags()
        temp = []
        for fflag in fflags:
            
            processed_fflag_name = re.sub(r"\[.*?\]\s", "", fflag)

            behaviour = None
            for behaviorId, behaviorName in BEHAVIOR_MAP.items():
                if processed_fflag_name.startswith(behaviorId):
                    behaviour = behaviorId
            if not behaviour:
                continue

            # Synchronized Fast Flags can only be updated on the server
            if (behaviour == "SF"):
                continue

            fflag_name_without_behavior = processed_fflag_name[len(behaviour):]

            data_type = None
            for typeId, typeName in TYPE_MAP.items():
                if fflag_name_without_behavior.startswith(typeId):
                    data_type = typeName
            if not data_type:
                continue

            fflag_real_name = fflag_name_without_behavior[len(data_type):]
            temp.append({
                'behaviour': behaviour,
                'name': fflag_real_name,
                'type': data_type
            })
        return jsonify({'fflags': temp})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route("/updateFFlags", methods=["GET"])
def update_fflags_route():
    return jsonify({'message': 'WIP'})

app.run(host='0.0.0.0', port=39457)