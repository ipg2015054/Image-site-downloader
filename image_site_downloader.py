import requests,os,bs4
search  = input('Enter the item for which you need images : ')
url = 'http://www.imagesbazaar.com/advancesearchresult.aspx?id='+ search +'&idtot='+ search +'&exec=True&nonexec=True&mostview=0'
os.makedirs('images', exist_ok=True)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
img_element = soup.select('.productImage img')
for i in range(10):
    print (img_element[i].getText)
    try:
        img_url = img_element[i].get('src')
        print('Downloading image %s...' % (img_url))
        res = requests.get(img_url)
        res.raise_for_status()
        imageFile = open(os.path.join('images', os.path.basename(img_url)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    except:
        print ('unable to download')

    
