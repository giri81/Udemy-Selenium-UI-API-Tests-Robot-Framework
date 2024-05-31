from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random


class APIRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_data = {'message': 'Welcome to the API!'}
            response_json = json.dumps(response_data)
            self.wfile.write(response_json.encode())
        elif self.path == '/random_number':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_data = {'random_number': random.randint(1, 100)}
            response_json = json.dumps(response_data)
            self.wfile.write(response_json.encode())
        else:
            self.send_error(404, 'Resource not found')

    def do_POST(self):
        if self.path == '/echo':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data_decoded = post_data.decode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_data = {'echo': post_data_decoded}
            response_json = json.dumps(response_data)
            self.wfile.write(response_json.encode())
        else:
            self.send_error(404, 'Resource not found')


def run(server_class=HTTPServer, handler_class=APIRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting HTTP server on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping HTTP server...')
        httpd.server_close()


if __name__ == '__main__':
    run()
