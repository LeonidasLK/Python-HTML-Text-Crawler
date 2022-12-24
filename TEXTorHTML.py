import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

z = input("Γράψε text αν θες να δεις το text της σελίδας.\nΓράψε html αν θες να δείς τον HTML κώδικα της σελίδας.\n")

if z=="html":
    
    x = input("Ποιό website?\n")

    y = input("Γράψτε αν ειναι .gr η .com\n")

    url = 'https://'+x+y
    
    r = requests.get(url)

    #Αν θέλουμε να το σώσουμε σε αρχείο
    #f=open("htmlcode.txt", 'w')
    #f.write(r.text)
    #f.close()
    
    print (r.text)

else:
      x2 = input("Ποιό website:\nπχ: Αν θες να δείς τι περιέχει το https://google.com γράψε google\n")

      y2 = input("Γράψε αν ειναι .gr η .com\n")

      url = "https://"+x2+y2
      
      html = urlopen(url).read()
      
    
      r = requests.get(url)
      
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

    #Αν θέλουμε να το σώσουμε σε αρχείο
    #f=open("textcode.txt", 'w')
    #f.write(r.text)
    #f.close()

      print(text)
   









