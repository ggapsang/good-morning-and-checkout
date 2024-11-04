from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200) # 응답 상태 코드
        self.send_header("Content-type", "text/html") # 응답 콘텐츠 타입
        self.end_headers() # 응답 헤더 종료

        self.wfile.write(b'Hello, world!')

server_address = ('', 8080)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print('Server started at http://localhost:8080')
httpd.serve_forever()
