#!/usr/bin/env python3
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/run", methods = ["POST"])
def runSil():
    if (not request.json["code"]):
        return jsonify({ "status": False, "stderr": "Invalid request" })
    sil = subprocess.run(["/silang/silang", "-"], input=request.json["code"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout = sil.stdout
    stderr = sil.stderr
    if len(stderr) == 0:
        pt = subprocess.run(["/silang/silang", "-", "--parseTree"], input=request.json["code"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return jsonify({ "status": True, "stdout": stdout, "parseTree": pt.stdout })
    else:
        return jsonify({ "status": False, "stderr": stderr })

if __name__ == "__main__":
    port = 5000
    app.run(host = "0.0.0.0", port = port)
