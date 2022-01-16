from bs4 import BeautifulSoup
from tabulate import tabulate
import requests

class ProxyList:

    def __init__(self):
        self.r = requests.Session()
        self.source = self.r.get("https://free-proxy-list.net/").text
        self.soup = BeautifulSoup(self.source, "html.parser")
        self.su = {
            "host": [],
            "port": [],
            "country": [],
            "https": [],
            "anonymity": [],
            "last_check": []
        }

    def getContent(self):
        self.table = self.soup.find_all("table", {"class":"table table-striped table-bordered"})
        for self.kntol in self.table[0].tbody.find_all("tr"):
            self.su["host"].append(self.kntol.findChildren()[0].text)
            self.su["port"].append(self.kntol.findChildren()[1].text)
            self.su["country"].append(self.kntol.findChildren()[3].text)
            self.su["https"].append(self.kntol.findChildren()[5].text if len(self.kntol.findChildren()[5]) >= 1 else "Unknown")
            self.su["anonymity"].append(self.kntol.findChildren()[4].text)
            self.su["last_check"].append(self.kntol.findChildren()[7].text)
        print(tabulate(self.su, headers="keys", tablefmt="pretty"))


    def main(self):
        self.getContent()

if __name__ == "__main__":
    ProxyList().main()
