from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
      <head>
        <title>info page</title>
    </head>
    <body>
      <h1>Name:RAKSHANA A - 26005835</h1> 
      <table border="10" bgcolor="white" cellspacing="10" cellpading="2">
        <caption>My Laptop Configuration</caption>
        <tr bgcolor="grey">
            <th>S.no</th>
            <th>Device Name</th>
            <th>Device info</th>
        </tr>
        <tr>
            <td>1.</td>
            <td>Device name</td>
            <td>TL15-53M-G2</td>
        </tr>
        <tr>
            <td>2.</td>
            <td>processor</td>
            <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
        </tr>
            <td>3.</td>
            <td>Installed RAM</td>	
            <td>16.0 GB (15.7 GB usable)</td>
        <tr>
            <td>4.</td>
            <td>Graphics card</td>
            <td>Intel(R) Graphics (128 MB)</td>
        <tr>
            <td>5.</td>
            <td>Storage</td>	
            <td>116 GB of 477 GB used</td>
        <tr>
            <td>6.</td>
            <td>Device ID</td>	
            <td>541E369A-9079-4D5F-8638-3875F740CA20</td>
        <tr>
            <td>7.</td>
            <td>Product ID</td>	
            <td>00342-42954-11575-AAOEM</td>
        <tr>
            <td>8.</td>
            <td>System type</td>	
            <td>64-bit operating system, x64-based processor</td>
        <tr>
            <td>9.</td>
            <td>Pen and touch</td>
            <td>No pen or touch input is available for this display</td>
        </tr>
      </table>
    </body>  
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()