# -*- coding: utf-8 -*-
"""CreditScore.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17ddF36Cmezv2Ixjt471hE0sHAlRoCQf6
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

# Veri kümesini yüklüyoruz
file_path = "/content/drive/MyDrive/Colab Notebooks/299PyhtonProject/train.csv"
try:
    data = pd.read_csv(file_path)
    print("Veri kümesi başarıyla yüklendi. İlk birkaç satır:")
    print(data.head())  # İlk 5 satırı gösterir
except FileNotFoundError:
    print(f"Belirtilen dosya yolunda dosya bulunamadı: {file_path}")
except Exception as e:
    print(f"Beklenmeyen bir hata oluştu: {e}")

print(data.info())

print(data.isnull().sum())

data["Credit_Score"].value_counts()

fig = px.box(data,
             x="Occupation",
             color="Credit_Score",
             title="Credit Scores Based on Occupation",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.show()

fig = px.box(data,
             x="Credit_Score",
             y="Annual_Income",
             color="Credit_Score",
             title="Credit Scores Based on Annual Income",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
             x="Credit_Score",
             y="Monthly_Inhand_Salary",
             color="Credit_Score",
             title="Credit Scores Based on Monthly Inhand Salary",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
             x="Credit_Score",
             y="Num_Bank_Accounts",
             color="Credit_Score",
             title="Credit Scores Based on Number of Bank Accounts",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
             x="Credit_Score",
             y="Num_Credit_Card",
             color="Credit_Score",
             title="Credit Scores Based on Number of Credit cards",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
             x="Credit_Score",
             y="Credit_History_Age",
             color="Credit_Score",
             title="Credit Scores Based on Credit History Age",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
             x="Credit_Score",
             y="Monthly_Balance",
             color="Credit_Score",
             title="Credit Scores Based on Monthly Balance Left",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

"""Credit Score Classification Model"""

data["Credit_Mix"] = data["Credit_Mix"].map({"Standard": 1,
                               "Good": 2,
                               "Bad": 0})

from sklearn.model_selection import train_test_split
x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary",
                   "Num_Bank_Accounts", "Num_Credit_Card",
                   "Interest_Rate", "Num_of_Loan",
                   "Delay_from_due_date", "Num_of_Delayed_Payment",
                   "Credit_Mix", "Outstanding_Debt",
                   "Credit_History_Age", "Monthly_Balance"]])
y = np.array(data[["Credit_Score"]])

xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                    test_size=0.33,
                                                    random_state=42)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(xtrain, ytrain)

print("Kredi Skoru Tahmini:")
a = float(input("Yıllık Gelir: "))
b = float(input("Aylık Net Maaş: "))
c = float(input("Banka Hesaplarının Sayısı: "))
d = float(input("Kredi Kartlarının Sayısı: "))
e = float(input("Faiz Oranı: "))
f = float(input("Kredi Sayısı: "))
g = float(input("Kişinin Ortalama Gecikme Gün Sayısı: "))
h = float(input("Gecikmiş Ödeme Sayısı: "))
i = input("Kredi Karışımı (Kötü: 0, Standart: 1, İyi: 3): ")
j = float(input("Ödenmemiş Borç: "))
k = float(input("Kredi Geçmişi Yaşı: "))
l = float(input("Aylık Bakiye: "))

# Özellikleri bir NumPy dizisine dönüştürüyoruz
features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])

# Modelden tahmini alıyoruz (model'in daha önce eğitilmiş olması gerekiyor)
print("Tahmin Edilen Kredi Skoru = ", model.predict(features))
