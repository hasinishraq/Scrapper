import requests
from bs4 import BeautifulSoup
import time
import logging
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global variable to store notices
notices = []

def get_notice_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        notice_elements = soup.find_all('div', class_='notice')
        notice_list = []

        for notice in notice_elements:
            a_tag = notice.find('a', href=True)
            if a_tag:
                notice_title = a_tag.get_text(strip=True)
                notice_link = a_tag['href']
                notice_list.append((notice_title, notice_link))
        
        return notice_list
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching notices: {e}")
        return []

def monitor_notices():
    global notices
    notice_url = 'https://www.uiu.ac.bd/notice'
    while True:
        logging.info("Checking for new notices...")
        notices = get_notice_links(notice_url)
        # Print notices to console
        for title, link in notices:
            print(f"Notice: {title}\nLink: {link}\n")
        
        # Wait for an hour before checking again
        time.sleep(3600)

class NoticeHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html_content = '<html><head><title>Notices</title></head><body>'
            html_content += '<h1>Latest Notices</h1><ul>'
            for title, link in notices:
                html_content += f'<li><a href="{link}" target="_blank">{title}</a></li>'
            html_content += '</ul></body></html>'
            
            self.wfile.write(html_content.encode('utf-8'))
        else:
            super().do_GET()

def start_http_server():
    port = int(os.environ.get("PORT", 10000))
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, NoticeHandler)
    logging.info(f"Starting HTTP server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    # Start the notice monitoring in a separate thread
    notice_thread = threading.Thread(target=monitor_notices)
    notice_thread.start()
    
    # Start the HTTP server
    start_http_server()
