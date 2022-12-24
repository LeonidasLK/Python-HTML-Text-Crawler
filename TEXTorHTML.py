import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

z = input("Γράψε text αν θες να δεις το text της σελίδας.\nΓράψε html αν θες να δείς τον HTML κώδικα της σελίδας.\n")

if z=="html":
    
    x = input("Ποιό website?:")

    y = input("Γράψτε αν ειναι .gr η .com\n")

    url = 'https://'+x+y
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    r = requests.get(url,headers=headers)
    f=open("htmlcode.txt", 'w')
    f.write(r.text)
    f.close()
    print (r.text)

else:
      x2 = input("Δώσε ενα website:\nπχ: Αν θες να δείς τι περιέχει το https://google.com γράψε google\n")

      y2 = input("Γράψε αν ειναι .gr η .com\n")

      url = "https://"+x2+y2
      
      html = urlopen(url).read()
      
      headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
      r = requests.get(url,headers=headers)
      
      soup = BeautifulSoup(html, features="html.parser")


      for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
      text = soup.get_text()
      
    # break into lines and remove leading and trailing space on each
      lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
      chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
      text = '\n'.join(chunk for chunk in chunks if chunk)

      print(text)
      









