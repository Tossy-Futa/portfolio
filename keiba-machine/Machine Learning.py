import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import lightgbm as lgb
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import log_loss  
from sklearn.metrics import roc_auc_score

#csv3.ipynbファイルにより作成されたcsvを読み込み→dfに入れる
df = pd.read_csv("re_keiba_data.csv")

#date列は日本語が含まれるのでインデックスにしてしまう
df.set_index('date', inplace=True)

#余分な列は削除（ranking列も日本語が含まれるので削除）
df_1 = df.drop(["ranking", "dust1", "dust2", "dust3", "dust4"], axis=1)#余分な列は削除（ranking列も日本語が含まれるので削除）
df_1 = df.drop(["ranking", "dust1", "dust2", "dust3", "dust4"], axis=1)

#1着かどうかを表すtop列を削除し、それ以外の列を説明変数とする→Xに入れる
x = df_1.drop('top',axis=1).values
#top列を目的変数とする→yに入れる
y = df_1['top'].values
#データの8割を訓練用、2割をテスト用　ランダムは無し
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.50, random_state=0)
#他の学習器だと上手く行かなかったので、色々調べた結果LightGBMを使う
model = lgb.LGBMClassifier()
model.fit(x_train, y_train)

# テストデータの予測(予測(0 or 1)を返す)
y_pred = model.predict(x_test)
# テストデータのクラス予測確率 (0の予測確率,1の予測確率を返す)
y_pred_prob = model.predict_proba(x_test)

# 真値と予測値の表示
df_1_pred = pd.DataFrame({'Answer':y_test,'Forecast':y_pred})
display(df_1_pred)

# 真値と予測確率の表示
df_1_pred_prob = pd.DataFrame({'Answer':y_test, 'probability_0':y_pred_prob[:,0], 'probability_1':y_pred_prob[:,1]})
display(df_1_pred_prob)

print("正解率 ＝ ", accuracy_score(y_test,y_pred))

