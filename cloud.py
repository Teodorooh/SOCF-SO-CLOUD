import os
import platform
import psutil

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Servidor funcionando! Use /info ou /metricas</h2>"

@app.route("/info")
def info():
    nome = "Eduardo Teodoro Moreira de Souza"
    return f"<h1>{nome}</h1>"

@app.route("/metricas")
def metricas():

    proc =  psutil.Process(os.getpid())
    pid = proc.pid

    memoria_bytes = proc.memory_info().rss
    memoria_mb = memoria_bytes / (1024*1024)

    uso_cpu = proc.cpu_percent(interval=0.1)

    so = platform.platform()

    dados = {
        "Process ID" : pid,
        "Memoria (MB)" : round(memoria_mb, 2),
        "CPU (%)" : uso_cpu,
        "SO" : so
    }

    return jsonify(dados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
