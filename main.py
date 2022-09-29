import requests
from func import downloadGame, makeDir

GameID = input("Enter Game ID (must be a 2006 to early 2008 game): ")
rootPath = "ROBLOX Games"
makeDir(rootPath)
url = 'http://web.archive.org/web/200710im_/http://www.roblox.com/Place.aspx?id=' + GameID
req = requests.get(url)

if req.status_code == 200:
  print("Found Game")
  downloadGame(GameID, url)
else:
  code = "Failed: " + GameID + " Error Code: " + str(req.status_code)
  print(code)
