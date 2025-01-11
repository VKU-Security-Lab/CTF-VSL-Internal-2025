import socketserver
import http.server
import urllib.parse
import requests

class ProxyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # Luu vao file log
    def log_message(self, format, *args):
        with open("logfake2.txt", "a") as f:
            # 192.168.25.1 - - [12/Jan/2025:01:00:59 +0700] "GET /?data=7f454c46020101000000000000000000 HTTP/1.1" 200 597 "http://crypto.vsl.dev/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"

            f.write("192.168.25.1 - - [%s] %s \"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0\"\n" % ( self.log_date_time_string(), format%args))
            
            
    def do_GET(self):
        # Lấy URL từ yêu cầu
        url = self.path
        parsed_url = urllib.parse.urlparse(url)
        
        # Gửi yêu cầu GET đến máy chủ đích
        response = requests.get(url)
        
        # Gửi lại phản hồi cho client
        self.send_response(response.status_code)
        self.send_header("Content-type", response.headers["Content-Type"])
        self.end_headers()
        
        # Truyền dữ liệu phản hồi về cho client
        self.wfile.write(response.content)

    def do_POST(self):
        # Lấy URL từ yêu cầu
        url = self.path
        parsed_url = urllib.parse.urlparse(url)

        # Đọc dữ liệu body từ yêu cầu POST
        content_length = int(self.headers['Content-Length'])  # Lấy kích thước dữ liệu body
        post_data = self.rfile.read(content_length)  # Đọc dữ liệu từ request body
        
        # In ra dữ liệu body nhận được (bắt dữ liệu)
      # In ra dữ liệu (giả sử dữ liệu là dạng chuỗi UTF-8)

        # Gửi POST request đến máy chủ đích với dữ liệu body
        response = requests.post(url, data=post_data, headers=self.headers)

        # Gửi lại phản hồi cho client
        self.send_response(response.status_code)
        self.send_header("Content-type", response.headers["Content-Type"])
        self.end_headers()
        
        # Truyền dữ liệu từ phản hồi về cho client
        self.wfile.write(response.content)
        self.log_message("POST %s %s - %s", url, response.status_code, post_data.decode('utf-8'))
        print("Received POST data:")
        print(post_data.decode('utf-8')) 
    def do_PUT(self):
        # Lấy URL từ yêu cầu
        url = self.path
        parsed_url = urllib.parse.urlparse(url)

        # Đọc dữ liệu body từ yêu cầu PUT
        content_length = int(self.headers['Content-Length'])  # Lấy kích thước dữ liệu body
        put_data = self.rfile.read(content_length)  # Đọc dữ liệu từ request body
        
        # In ra dữ liệu body nhận được (bắt dữ liệu)
        print("Received PUT data:")
        print(put_data.decode('utf-8'))  # In ra dữ liệu (giả sử dữ liệu là dạng chuỗi UTF-8)

        # Gửi PUT request đến máy chủ đích với dữ liệu body
        response = requests.put(url, data=put_data, headers=self.headers)

        # Gửi lại phản hồi cho client
        self.send_response(response.status_code)
        self.send_header("Content-type", response.headers["Content-Type"])
        self.end_headers()
        
        # Truyền dữ liệu từ phản hồi về cho client
        self.wfile.write(response.content)

    def do_DELETE(self):
        # Lấy URL từ yêu cầu
        url = self.path
        parsed_url = urllib.parse.urlparse(url)

        # Gửi DELETE request đến máy chủ đích
        response = requests.delete(url)
        
        # Gửi lại phản hồi cho client
        self.send_response(response.status_code)
        self.send_header("Content-type", response.headers["Content-Type"])
        self.end_headers()
        
        # Truyền dữ liệu từ phản hồi về cho client
        self.wfile.write(response.content)

# Thiết lập Proxy Server
PORT = 8888
Handler = ProxyHTTPRequestHandler
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    print(f"Proxy server running on localhost:{PORT}")
    httpd.serve_forever()
