import requests
from bs4 import BeautifulSoup

def get_notice_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    notices = soup.find_all('div', class_='notice')
    notice_list = []

    for notice in notices:
        a_tag = notice.find('a', href=True)
        if a_tag:
            notice_title = a_tag.get_text(strip=True)
            notice_link = a_tag['href']
            notice_list.append((notice_title, notice_link))
    
    return notice_list

def main():
    notice_url = 'https://www.uiu.ac.bd/notice'
    notices = get_notice_links(notice_url)
    
    for title, link in notices:
        print(f"Notice: {title}\nLink: {link}\n")

if __name__ == "__main__":
    main()
