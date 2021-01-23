import os
import requests
import time
import chromedriver_binary
import csv
import collections
import copy
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#GoogleChromeを使ってWEBスクレイピングを進める
#ヘッドレスブラウザを利用する
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

#netkeiba様よりデータを集める
URL = "https://db.netkeiba.com/?pid=race_search_detail"
driver.get(URL)
time.sleep(1)

#検索フォームのチェックボックス等にチェックを入れたり入力したりする
for i in range(1,3):
    terms_track = driver.find_element_by_id("check_track_"+ str(i))
    terms_track.click()
#2017年～2020年のデータを集める
f_year = 2017
e_year = 2020
start_year_element = driver.find_element_by_name('start_year')
start_year_select = Select(start_year_element)
start_year_select.select_by_value(str(f_year))
end_year_element = driver.find_element_by_name('end_year')
end_year_select = Select(end_year_element)
end_year_select.select_by_value(str(e_year))
for i in range(1,10):
    terms_Jyo = driver.find_element_by_id("check_Jyo_"+ str(i).zfill(2))
    terms_Jyo.click()
for i in range(1,4):
    terms_baba = driver.find_element_by_id("check_baba_"+ str(i))
    terms_baba.click()
for i in range(1,7):
    terms_jyoken = driver.find_element_by_id("check_jyoken_"+ str(i))
    terms_jyoken.click()
for i in range(11,14):
    terms_barei = driver.find_element_by_id("check_barei_"+ str(i))
    terms_barei.click()
for i in range(1,10):
    terms_grade = driver.find_element_by_id("check_grade_"+ str(i))
    terms_grade.click()
#距離は1000m～4000mと入力する（確か1200m～3600mくらいまでのレースがあるはず）
f_field = driver.find_element_by_name("kyori_min")
f_field.send_keys("1000")
e_field = driver.find_element_by_name("kyori_max")
e_field.send_keys("4000")

#検索結果は1ページ100レースずつ表示するようにする
list_element = driver.find_element_by_name('list')
list_select = Select(list_element)
list_select.select_by_value("100")

#データ検索を行う
form = driver.find_element_by_css_selector("#db_search_detail_form > form")
form.submit()
time.sleep(3)

#「keiba_data.txt」というテキストデータを作成し、それぞれのレース結果のurlを入れていく
with open("keiba_data.txt", mode='w') as file_text:
    while True:
        time.sleep(3)
        all_rows = driver.find_element_by_class_name('race_table_01').find_elements_by_tag_name("tr")
        for row in range(1, len(all_rows)):
            race_link=all_rows[row].find_elements_by_tag_name("td")[4].find_element_by_tag_name("a").get_attribute("href")
            file_text.write(race_link+"\n")
        try:
            target = driver.find_elements_by_link_text("次")[0]
            driver.execute_script("arguments[0].click();", target)
        except IndexError:
            break
            
#空のデータフレームを作る
df = pd.DataFrame()
#keiba_data.txtに入っているurlたち（テキストデータ）を変数file_textに入れる
with open("keiba_data.txt") as file_text:
    #keiba_data.txtに入っているurlたちを、1行ずつに分割してリスト化する
    urls = file_text.read().splitlines()
    #urlsリストの中からurl1つ1つを拾ってhtml化して保存していく作業に入る
    for url in urls:
        #urlを変数に入れる
        res = requests.get(url)
        #res.contentはhtmlの形式で、これを渡すと文字化けする可能性が減るらしい
        soup = BeautifulSoup(res.content)
        table = [table.text for table in soup.find_all('td', nowrap='nowrap')]
        #tableリストを21分割する
        table_1 = [table[idx:idx + 21] for idx in range(0,len(table), 21)]
        #table_str = [str(table_1) for table_1 in table_1s]
        souce1_1 = soup.select("li.result_link > a")[0].text
        souce1_2 = souce1_1.replace("のレース結果", "")
        souce1_3 = [souce1_2]
        try:
            souce2_1 = soup.select("ul.race_place > li > a.active")[0].text
        #「阪神」というワードが取れない事象が3回ほど発生するので、その対策
        except IndexError:
            souce2_1 = "阪神"
        souce2_2 = [souce2_1] 
        souce3_1 = soup.select("dl.racedata > dd > h1")[0].text
        souce3_2 = [souce3_1]
        souce4_1 = soup.select("dl.racedata > dd > p > diary_snap_cut > span")[0].text
        #空白で要素を分割すると、要素数が6個のものと7個のものが表れるので、"/"で分ける
        souce4_2 = souce4_1.split("/")
        souce_5 = souce1_3 + souce2_2 + souce3_2 + souce4_2
        #table_1リストの要素の数だけ、souce_5リストを増やしていく
        souce_5s = copy.copy(souce_5)
        while len(souce_5s)/7 < len(table_1):
            souce_5s = souce_5 + souce_5s
        souce_5 = [souce_5s[idx:idx + 7] for idx in range(0,len(souce_5s), 7)]
        #souce_5リストの各要素とtable_1リストの各要素を合体させる
        #　→各レースの各行の頭（table_1リストの各要素）に、日付やレース会場や天気や馬場状態等（souce_5）がくっつく形になる
        keiba_data = np.hstack([souce_5, table_1])
        #データフレームにする
        total_data = pd.DataFrame(keiba_data)
        df = df.append(total_data)
        #一応確認
        print(df)
#データフレームをcsvに起こすことで、チェックポイントとすることができる
df.to_csv("keiba_data.csv")
