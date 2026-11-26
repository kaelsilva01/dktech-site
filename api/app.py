
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MinhaAPI(BaseHTTPRequestHandler):

    def responder_json(self, status, dados):
        self.send_response(status)
        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )
        self.end_headers()

        self.wfile.write(
            json.dumps(dados, ensure_ascii=False).encode("utf-8")
        )

    def do_GET(self):

        if self.path == "/":
            resposta = {
                "projeto": "DK TECH",
                "status": "online",
                "mensagem": "API funcionando com sucesso!"
            }

            self.responder_json(200, resposta)

        elif self.path == "/health":
            resposta = {
                "status": "healthy",
                "servico": "DK TECH API"
            }

            self.responder_json(200, resposta)

        else:
            self.responder_json(404, {
                "erro": "Rota nao encontrada"
            })


servidor = HTTPServer(("0.0.0.0", 5000), MinhaAPI)

print("DK TECH API iniciada na porta 5000")

servidor.serve_forever()
