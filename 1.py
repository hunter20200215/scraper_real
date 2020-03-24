  
import csv
import sys
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait

import requests
from bs4 import BeautifulSoup


import time

output_file = 'newyork_contact.csv'


def add_csv_head():
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Email', 'PostID', 'Jobs_Category','Area', 'MapAddress', 'PostUrl', 'Compensation', 'EmploymentType'])

def add_csv_row(titel, emailaddress, PostID, jobs_category, area, mapaddress, posturl, compensation, employmenttype):
    # print("-----33--------")
    # print(jobs_category)
    with open(output_file, 'a', newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([title, emailaddress, PostID, jobs_category, area, mapaddress, posturl, compensation, employmenttype])

def setUpChrome():
    global driver
    # Using Chrome
    chrome_options = webdriver.ChromeOptions()
    #prefs = {"profile.managed_default_content_settings.images": 2}
    #chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    #chrome_options.add_argument('headless')

    scriptpath = os.path.realpath(__file__)
    foldername = os.path.basename(scriptpath)
    scriptpath = scriptpath[:scriptpath.find(foldername)]

    scriptpath += 'chromedriver'

    driver = webdriver.Chrome(scriptpath, chrome_options=chrome_options)
    return driver

add_csv_head()

base_url = 'https://newyork.craigslist.org/d/jobs/search/que/jjj'

# i = 1
# while i < 168:
#     url = base_url + 'i'

driver = setUpChrome()
driver.get(base_url)

page1 = requests.get(base_url)

soup1 = BeautifulSoup(page1.content, 'html.parser')
# # print(soup1)

soup1.findAll('a', class_='result-title')
# print(soup1.findAll('a', class_='result-title'))
for a in soup1.findAll('a', class_='result-title',  href=True):
    
    # print(a['href'])
    driver.get(a['href'])
    TimeoutException
    posturl=a['href']

    html = driver.page_source
    soup2 = BeautifulSoup(html, 'html.parser')
    # print (soup2)
    # print (soup2.find('a', class_='postingtitletext').text)
    # print(soup2.find_element_by_xpath)
    title=(soup2.find('span', id = 'titletextonly').text)

    PostID=(soup2.findAll('p', class_ = 'postinginfo')[1].text)
    

    attr = soup2.find('p', class_ = 'attrgroup');
    
    
    jobs_categorys=soup2.find('li', class_='crumb category').text
    jobs_category=jobs_categorys.strip()
    # print(jobs_category)
    try:
        areas= soup2.find('span', class_='postingtitletext')
        area=areas.find('small').text
    except:
        area = "N/A"
    try:
        compensation = attr.find('b').text
    # print(compensation)
        employmenttype=(attr.findAll('b')[1].text)
    except:
        compensation="N/A"
        employmenttype="N/A"

    try:
        mapaddress=soup2.find('div', class_='mapaddress').text
    except:
        mapaddress = "N/A"
    # try:
    #     driver.find_element_by_xpath('/html/body/section/section/header/div[2]/div/button').click()
        
    #     emailaddress = driver.find_element_by_xpath("/html/body/section/section/header/div[2]/div/div[1]/aside/ul/li[3]/input").get_attribute("value")
    #     # classname=driver.find_elements_by_class_name('mailapp')
    #     # emailaddress=classname['href']
    #     time.sleep(15)
    #     print(emailaddress)
    # except:
    #     emailaddress = "N/A"


    try:
        driver.find_element_by_xpath('/html/body/section/section/header/div[2]/div/button').click()

        time.sleep(9)
        # emailaddress = driver.find_element_by_xpath("/html/body/section/section/header/div[2]/div/div[1]/aside/ul/li[3]/input").get_attribute("value")
        emailaddress = driver.find_element_by_css_selector('input.anonemail').get_attribute("value")
        # print(emailaddress)    
    except:
        # print ("error")
        emailaddress = "N/A"
    # print (emailaddress)

    # add_csv_row(title, emailaddress)
    
        
        
        #prices = soup2.xpath('/html/body/section/section/section/div[1]/p/span[1]/b').text
        # print(PostID)


        
        # PostID=(soup2.find_element_by_xpath('/html/body/section/section/section/div[2]/p[1]')).text
        # print(PostID)
        # print(title)
        # page2 = requests.get(a['href'])
        # soup2 = BeautifulSoup(page2.content, 'html.parser')
        # print(soup2)
        # print(page2)
        # driver = setUpChrome()
        # driver.get(page2)
        # title = driver.find_element_by_xpath('//*[@id="titletextonly"]')
        # print (title)
        # /html/body/section/section/header/div[2]/div/button
        # /html/body/section/section/header/div[2]/div/button
    # try:
    #     driver.find_element_by_xpath('/html/body/section/section/header/div[2]/div/button').click()
    #     time.sleep(50)
    #     # emailaddress = driver.find_element_by_xpath("/html/body/section/section/header/div[2]/div/div[1]/aside/ul/li[3]/input").get_attribute("value")
    #     classname=driver.find_elements_by_class_name('mailapp')
    #     emailaddress=classname['href']
    #     print(emailaddress)
        # time.sleep(10)
    # mailaddress = (driver.find_elements_by_class_name('anonemail').value)
    # print(mailaddress)
    # mailaddress=(soup2.find('input', class_='anonemail').text)
    # print(mailaddress)
    # mailaddress = driver.find_element_by_xpath('/html/body/section/section/header/div[2]/div/div[1]/aside/ul/li[5]/input').value
    # print ( driver.find_element_by_xpath('/html/body/section/section/header/div[2]/div/div[1]/aside/ul/li[4]/input').text)
    # text = driver.find_element_by_class_name("mailapp").getText();
    # <input type="text" name="inputbox" value="name" class="box">
    
    # print(driver.find_elements(By.class_name("anonemail")).getAttribute("value"))
    # print (driver.find_elements_by_class_name('anonemail')).text
    # contents = driver.find_elements_by_class_name('postingtitletext')
    # print(contents)
    
        
        # print(emailaddress)
        # PostID =  driver.find_element_by_xpath("/html/body/section/section/section/div[2]/p[1]").getText
        # print (PostID)
    # break

    # print("-------------------")
    # print(jobs_category)

    add_csv_row(title, emailaddress, PostID, jobs_category, area, mapaddress, posturl, compensation, employmenttype)

    # print(driver.find_element(By.id("inputTag")).getAttribute("value"))

    # soup2 = BeautifulSoup(driver.content, 'html.parser')
    
    # print (soup2.find('span', id = 'titletextonly').text)

    # print (soup2.find('div', class_='reply-info'))
    
    # break
# # site_link = soup.findAll(attrs={"data-title" : "Store Address"})[0].find('a', attrs={"rel" : "nofollow"}, href = True)
# for a in soup1.findAll(attrs={"data-title" : "Store Address"}):
#     site_link = a.find('a', attrs={"rel" : "nofollow"}, href = True)['href']
#     i_link = "N/A"
#     email = "N/A"
#     f_link = "N/A"
#     # print(site_link['href'])
#     page2 = requests.get(site_link)
#     soup2 = BeautifulSoup(page2.content, 'html.parser')
#     for b in soup2.find_all('a', href = True):
#         # print(b['href'].find('instagram'))
#         if b['href'].find('facebook') != -1:
#             f_link = b['href']
#         if b['href'].find('instagram') != -1:
#             i_link = b['href']
#     if f_link == "N/A":
#         add_csv_row(site_link, "N/A", "N/A")
#         # print("N/A")
#     else:
#         add_csv_row(site_link, f_link, i_link)

#         page3 = requests.get(f_link)
#         soup3 = BeautifulSoup(page3.content, 'html.parser')
#         # soup3.find_all()
#         # print(soup3.findAll('a', attrs={'data-ft' : '{"tn":"-U"}'}, href = True))
#         for c in soup3.findAll('a', attrs={'data-ft' : '{"tn":"-U"}'}, href = True):
#             print(c['href'])
#             print('\n')
#         # email = soup3.find('a', attrs={"data-ft" : '{"tn":"-U"}'}, href = True)['href']
#         # print(f_link)
#     # print(site_link, i_link, f_link)
#     break


# soup.find_all('p', class_='outer-text')
# def add_csv_row(city, titles, po, dd, hd):


print("done")