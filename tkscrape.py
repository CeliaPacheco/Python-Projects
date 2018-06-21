import tkinter as tk
import requests
from bs4 import BeautifulSoup

class Scrape(tk.Tk):
    def __init__(self):
        super().__init__()
        self.links = []
        self.title("Scraper App")
        self.geometry("300x400")

        self.url_label = tk.Label(self, text="Enter URL here")
        self.url_entry = tk.Entry(self)

        for link in self.links:
            link.pack()

        self.url_label.pack()
        self.url_entry.pack()

        self.bind("<Return>", self.open_url)


    def open_url(self, event):
        url = self.url_entry.get().strip()
        print(url)
        #url = 'https://www.reddit.com/r/dailyprogrammer/'
        headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'}
        response = requests.get(url, headers=headers)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')

        self.get_soup(soup)
        return

    def get_soup(self, soup):
        for link in soup.find_all('a'):
            for h2 in link.find_all('h2'):
                if "[Intermediate]" in str(h2):
                    #TODO work on displaying a hyperlinks
                    new_link = tk.Label(self, text=str(link), pady=10)
                    new_link.pack(side=tk.TOP, fill=tk.X)
                    self.links.append(new_link)


if __name__ == "__main__":
    scraper = Scrape()
    scraper.mainloop()
