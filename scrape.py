# import libraries
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from datetime import datetime

currentYear = str(datetime.today().year)
weekNum = 1
url = "http://www.nfl.com/schedules/" + currentYear + "/REG"
page = urllib.request.urlopen(url + str(weekNum))
soup = BeautifulSoup(page, "html.parser")

matchup = soup.find_all("div", "list-matchup-row-team")
for i in range(0, len(matchup)):
    print(matchup[i].text.strip())




