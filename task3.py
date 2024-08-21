import requests
from bs4 import BeautifulSoup

url='https://www.imperva.com/learn/application-security/web-scraping-attack/#:~:text=Web%20scraping%20is%20the%20process,replicate%20entire%20website%20content%20elsewhere.' 

response=requests.get(url)

if(response.status_code==200):
    soup=BeautifulSoup(response.text,'html.parser') #to parse content on the page
    
    page_text=soup.get_text() #gets all the page text
    
    links=[a['href'] for a in soup.find_all('a',  href=True)] #extracts all the links
    
    images=[img['src'] for img in soup.find_all('img', src=True)] # extracts all the images
    
    print('Page Text : ')
    print(page_text)
    
    print("\n links: ")
    for link in links:
        print(link)   
    
    print("\nimages")
    for image in images:
        print(image)
        
else:
    print(f"failed to retrive the web page. status code: {response.status_code}")
         
    
