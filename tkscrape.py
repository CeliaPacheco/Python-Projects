import tkinter as tk
import requests
import webbrowser
from bs4 import BeautifulSoup

class Scrape(tk.Tk):
    def __init__(self):
        super().__init__()

        self.links = {}
        self.title("Scraper App")
        self.geometry("500x500")

        self.main_frame = tk.Frame(self, width=500, height=300)

        self.url_label = tk.Label(self.main_frame, text="Enter URL here")
        self.url_entry = tk.Entry(self.main_frame)

        self.main_frame.pack()
        self.url_label.pack()
        self.url_entry.pack()

        self.bind("<Return>", self.open_url)

    def open_url(self, event):
        url = self.url_entry.get().strip()
        headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'}
        response = requests.get(url, headers=headers)
        html = response.content
        self.get_links(html)

    def get_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            for h2 in link.find_all('h2'):
                if "[Intermediate]" in str(h2):
                    #new_link = tk.Label(self, text=self.get_link(link), fg="blue", cursor="hand2")
                    self.links[str(h2)] = self.get_link(link)
                    new_link = tk.Label(self, text=str(h2), fg="blue", cursor="hand2")
                    new_link.pack(side=tk.TOP, fill=tk.X)
                    l = self.get_link(link)
                    new_link.bind("<Button-1>", self.callback)

    def get_link(self, link):
        text = "https://www.reddit.com"
        return text + link.get('href')

    def callback(self, event):
        webbrowser.open_new(self.links[event.widget.cget("text")])


if __name__ == "__main__":
    scraper = Scrape()
    scraper.mainloop()
