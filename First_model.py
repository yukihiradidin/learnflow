from cProfile import label
from cgi import test
from pyexpat import features
from xml.sax.handler import feature_external_ges
from annotated_types import Predicate
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#membaca dataset CSV
dataset_path = '' #Masukin path atau alamat tempat data .CSV di simpan contoh 'C\\[nama_folder]\\gaya_belajar.csv
df = pd.read_csv(dataset_path)

#menentukan fitur dan label
features = ['gaya_belajar', ''] #menambahkan fitur yang nantinya akan di tampilkan di grafik
label = 'hasil_test'


#mengubah data menjadi numerik
#hal ini digunakan karena machine learning memerlukan input numerik
#mengubah nilai categorical menjadi kolom baru dan memberikan nilai 1 dan 0 pada nilai tersebut
#contoh nilai kategorical
#1. Jenis buah : Apel, Jeruk, Pisang
#2. Warna mobil : Merah, Hitam, Putih
#3. Jenis Kelamin : Laki-laki, Wanita
df_encoded=pd.get_dummies(df[features]) 

#Membagi data menjadi set pelatihan dan set uji
X_train, X_test, Y_train, Y_test = train_test_split(df_encoded, df[label], test_size=0.2, random_state=42)

#Membuat model decision tree
model = DecisionTreeClassifier()

#Melatih model
model.fit(X_train, Y_train)

#menguji model
predictions=model.predict(X_test)

#Menghitung akurasi
accuracy = accuracy_score()
print(f'Akurasi Model: {accuracy}')

#new student
new_student_data = pd.DataFrame({''}) #memasukan nilai data siswa baru dengan menambah kolom seperti gaya belajar
new_student_data_encoded = pd.get_dummies(new_student_data) #mengubah data kategorical dalam data new_student_data menjadi 1 dan 0, yang di beri nama (new_student_data)

#prediksi gaya belajar
predicted_result = model.predict(new_student_data_encoded)
print(f'Hasil Tes prediksi untuk siswa baru: {predicted_result[0]}')

