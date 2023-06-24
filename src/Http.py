import pycurl, io
"""
"Http" is a lightweight and user-friendly HTTP library that simplifies the process of making HTTP requests in Python. Powered by the powerful pycurl library, "Http" provides a simple interface for sending GET requests and will soon support POST requests as well.
Coded by Farhan Ali
Give Credit If You want To use it
https://github.com/farhanaliofficial
"""
class Http:
	def get(self, url, headers=[]):
		curl = pycurl.Curl()
		buffer = io.BytesIO()
		curl.setopt(curl.URL, url)
		curl.setopt(curl.WRITEDATA, buffer)
		curl.setopt(curl.HTTPHEADER, headers)
		curl.perform()

		resp = buffer.getvalue().decode("utf-8")
		curl.close()
		return resp
	# post method coming soon
