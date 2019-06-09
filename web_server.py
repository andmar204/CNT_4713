from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from os import curdir, sep, startfile

PORT = 8080

class Handler(BaseHTTPRequestHandler):

	def do_GET(self):
		if self.path == '/':
			self.path = '/web_content.html'
		elif self.path == '/v':
			self.path = '/video.mp4'
		elif self.path == '/a':
			self.path = '/audio.mp3'

		try:
			send = False

			if self.path.endswith('.html'):
				mType = 'text/html'
				send = True
			if self.path.endswith('.mp4'):
				mType = 'video/mp4'
				send = True
			if self.path.endswith('.mp3'):
				mType = 'audio/mpeg'
				send = True

			if send == True:
				path = curdir + sep + self.path			
				theFile = open(path)
				self.send_response(200)
				self.send_header('Content-type', mType)
				self.end_headers()

				if mType == 'text/html':
					output = theFile.read()
					self.wfile.write(output.encode('utf-8'))
				elif mType == 'video/mp4':
					startfile('.\/video.mp4')
				elif mType == 'audio/mpeg':
					startfile('.\/audio.mp3')

				theFile.close()
			return

		except Exception as e:
			print('e:', e) 
			self.send_error(404, 'File not found: ' + str(self.path), 'The file ' + str(self.path) + ' was not found in the directory.')

try:
	server = HTTPServer(('', PORT), Handler)
	print('HTTPServer started on port', PORT)
	server.serve_forever()
except KeyboardInterrupt:
	print('^C received, web server is shutting down.')
	server.socket.close()