#!/usr/bin/env python3
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/run", methods = ["POST"])
def runSil():
    if (not request.json["code"]):
        return jsonify({ "status": False, "stderr": "Invalid request" })
    sil = subprocess.run(["/silang/sil", "--parseTree", "-i", request.json["code"]],
                         stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout = sil.stdout.decode("utf8")
    stderr = sil.stderr.decode("utf8")
    if len(stderr) == 0:
        parseTree = stdout.split("\n\n")[0]
        stdout = "\n\n".join(stdout.split("\n\n")[1:])
        return jsonify({ "status": True, "stdout": stdout, "parseTree": parseTree })
    else:
        return jsonify({ "status": False, "stderr": stderr })

if __name__ == "__main__":
    port = 5000
    app.run(host = "0.0.0.0", port = port)
