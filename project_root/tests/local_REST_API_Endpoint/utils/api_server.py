from http.server import BaseHTTPRequestHandler, HTTPServer
import json


# Define the handler for HTTP requests
class APIRequestHandler(BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        # Set response status code
        self.send_response(200)
        # Set response headers
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # Define API response data
        response_data = {'message': 'Hello, this is your REST API response!'}
        # Encode response data as JSON
        response_json = json.dumps(response_data)
        # Send response body
        self.wfile.write(response_json.encode())


# Define the function to start the HTTP server
def run(server_class=HTTPServer, handler_class=APIRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting HTTP server on port {port}...')
    try:
        # Start the HTTP server
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Handle keyboard interrupt to gracefully stop the server
        print('\nStopping HTTP server...')
        httpd.server_close()


if __name__ == '__main__':
    # Run the HTTP server on port 8000 by default
    run()
