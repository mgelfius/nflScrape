# import libraries
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from datetime import datetime
currentYear = str(datetime.today().year)
url = "http://www.nfl.com/schedules/" + currentYear + "/REG"

for n in range(1, 18):
    print('\033[95m' + "WEEK " + str(n) + " GAMES" + '\033[0m' + '\n')
    page = urllib.request.urlopen(url + str(n))
    soup = BeautifulSoup(page, "html.parser")

    matchup = soup.find_all("div", "list-matchup-row-team")
    for i in range(0, len(matchup)):
        print(matchup[i].text.strip() + '\n')
