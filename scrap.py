from bs4 import BeautifulSoup
import requests

user_name = 'gaurav3010'
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


# repo
for list_all in soup.find_all('li', class_ = 'pinned-repo-item'):
    repo = list_all.span.span.a.span.text
    print('Repo name : ', repo)

    # repo link
    repo_link = list_all.span.span.a['href']
    print('Repo link : ' ,repo_link)

    # language and star
    lan = list_all.span.find('p', class_='f6').text.strip()
    all = " ".join(lan.split())
    lan_star = all.split()
    language = lan_star[0]
    #star = lan_star[1]
    print('Language : ', language)
    #print('Star : ', star)


    # inside repo
    inside_url = github_url + repo_link + '/commits/master'
    print(inside_url)
    inside_source = requests.get(inside_url).text
    inside_soup = BeautifulSoup(inside_source, 'lxml')
    #print(inside_soup)

    commit_date = []
    for com_date in inside_soup.find_all('div', class_ = 'commit-group-title'):
        commit_date.append(com_date.text.strip())
    #print(commit_date)

    commit_date_count = 0
    for all_commit_ol in inside_soup.find_all('ol', class_ = 'commit-group'):
        print('Commit Date : ', commit_date[commit_date_count])
        for ol_all_li in all_commit_ol.find_all('li', class_ = 'commits-list-item'):
            commit_message = ol_all_li.div.p.a.text
            print(commit_message)
        print()
        commit_date_count += commit_date_count

    print('------------------------------------')



