import re
import urllib.parse
import urllib.request

def get_vid(query):

  try:
    encoded = urllib.parse.quote(query)

url=("https://www.youtube.com/results"
     "?search_query="+encoded)

result = urllib.request.Request(url, header={"User-Agent":"Mozilla/5.0"})

data=urllib.request.urlopen(request,timeout=5).read().decode("utf-8",errors="ignore")

ids=re.findall(r'"videoID":"([^"]+)")"' , data)

return id[*0] if ids else none 
except Exception
return none

def create_youtube_url(command):

  text = command.lower().strip()

pattern=[
  r"play\s+song\s(.+)",
  r"play\s+music\s+(.+)",
  r"play\s+(.+)",
  r"youtubr\s+(.+)"
]

query = command

for pattern in patterns:

  match = re.search(pattern,text)

if match:

  query=match.group(1)
  break

  query=query.strip()

video_id=get_vid(query)

if not video_id:
  return none

return(
  "https://www.youtube.com/embed/ "
  +video_id
  +"?autoplay=1&mute=0"
)

