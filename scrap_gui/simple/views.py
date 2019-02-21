from django.shortcuts import render
from django.http import HttpResponse
from simple.forms import UseridForm

from bs4 import BeautifulSoup
import requests


def index(request):
    if request.method == 'POST':
        form = UseridForm(request.POST)
        #print('gaurav_if')
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            #print(user_id)

            #--------------   scrap.py ---------------#
            user_name = user_id
            github_url = 'https://github.com/'
            user_url = github_url + user_name
            source = requests.get(user_url).text

            soup = BeautifulSoup(source, 'lxml')

            #print(soup.prettify())

            # name and username
            name_source = soup.find('h1', class_ = 'vcard-names')
            name_source = name_source.find_all('span')
            # name
            name = name_source[0].text
            print(name,"")

            # user name
            username = name_source[1].text
            print(username,"")


            # img-link
            img_url_source = soup.find('a', class_ = 'u-photo')
            img_url = img_url_source.img['src']
            print(img_url,"")

            repo_dict = {}
            for list_all in soup.find_all('li', class_ = 'pinned-item-list-item'):
                repo = list_all.span.span.a.span.text
                #print('Repo name : ', repo)
               

                repo_link = list_all.span.span.a['href']
                #print('Repo link : ' ,repo_link)
                repo_dict[repo] = repo_link









        context = {
            'name':name,
            'username':username,
            'img_url':img_url,
            'repo_dict':repo_dict
        }
        form = UseridForm()
        var = 'gaurav'
        return render(request, 'index1.html', context)
    else:
        #print('gaurav_else')
        form = UseridForm()
        return render(request, 'index.html', {'form':form})
    


    
    
