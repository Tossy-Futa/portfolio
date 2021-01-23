import csv
import pandas as pd
from sklearn import preprocessing

#で作ったcsvを読み込み→dfに入れる
df = pd.read_csv("keiba_data1.csv", header=0, index_col=0, encoding="UTF-8")
#列のインデックスを改名
df_1 = df.rename(columns={'0': 'date', '1': 'field', '2':'race_name', '3':'race_features', '4':'weather', '5':'race_state', '6':'start_time', '7':'ranking', '8':'big_frame', '9':'small_frame', '10':'horse_name', '11':'sex_age', '12':'weight','13':'jockey', '14':'record', '15':'distance', '16':'dust1', '17':'positioning', '18':'speed', '19':'odds', '20':'popular', '21':'body_weight','22':'dust2','23':'dust3','24':'dust4', '25':'trainer', '26':'owner', '27':'prize'})

#LabelEncoderを使って、データをひたすら数値に変換
re = preprocessing.LabelEncoder()
df_1['field'] = re.fit_transform(df_1.field.values)
df_1['race_name'] = re.fit_transform(df_1.race_name.values)
df_1['race_features'] = re.fit_transform(df_1.race_features.values)
df_1['weather'] = re.fit_transform(df_1.weather.values)
df_1['race_state'] = re.fit_transform(df_1.race_state.values)
df_1['start_time'] = re.fit_transform(df_1.race_state.values)
df_1['big_frame'] = re.fit_transform(df_1.race_state.values)
df_1['small_frame'] = re.fit_transform(df_1.race_state.values)
df_1['horse_name'] = re.fit_transform(df_1.race_name.values)
df_1['sex_age'] = re.fit_transform(df_1.race_name.values)
df_1['weight'] = re.fit_transform(df_1.race_name.values)
df_1['jockey'] = re.fit_transform(df_1.race_name.values)
df_1['record'] = re.fit_transform(df_1.race_name.values)
df_1['distance'] = re.fit_transform(df_1.race_name.values)
df_1['positioning'] = re.fit_transform(df_1.race_name.values)
df_1['speed'] = re.fit_transform(df_1.race_name.values)
df_1['odds'] = re.fit_transform(df_1.race_name.values)
df_1['popular'] = re.fit_transform(df_1.race_name.values)
df_1['body_weight'] = re.fit_transform(df_1.race_name.values)
df_1['trainer'] = re.fit_transform(df_1.race_name.values)
df_1['owner'] = re.fit_transform(df_1.race_name.values)
df_1['prize'] = re.fit_transform(df_1.race_name.values)

#後で使えるかもしれないので、2020年〇月×日のデータであれば2020といったようなデータを入れる列を作る
df_1['label'] = df_1.date.str[0:4]
#新たにtop列を作る→1着の馬はtop列に1を、それ以外の着順だった馬はtop列に0を入れていく
df_1.loc[df_1['ranking'] == "1", 'top'] = 1
df_1.loc[~(df_1['ranking'] == "1"), 'top'] = 0
#本当に変換されているか一応確認する
print(df_1['top'])

#改めてcsvに起こす
df_1.to_csv("re_keiba_data.csv")
