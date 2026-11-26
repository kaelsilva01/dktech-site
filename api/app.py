from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MinhaAPI(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            resposta = {
                "projeto": "DK TECH",
                "status": "online",
                "mensagem": "API funcionando com sucesso!"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            self.wfile.write(
                json.dumps(resposta, ensure_ascii=False).encode("utf-8")
            )

        else:
            self.send_response(404)
            self.end_headers()

servidor = HTTPServer(("0.0.0.0", 5000), MinhaAPI)

print("DK TECH API iniciada na porta 5000")

servidor.serve_forever()