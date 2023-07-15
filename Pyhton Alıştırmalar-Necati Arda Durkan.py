#Görev 1
x=8
y=3.2
z=8j+18
a="Hello World"
b=True
c=23<22
l=[1,2,3,4]
d={"Name":"Jake",
   "Age":27,"Adress":"Downtown"}
t=("Machine Learning","Data Science")
s={"Pyhton","Machine Learning","Data Sciene"}
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(l))
print(type(d))
print(type(t))
print(type(s))
#Görev 2
text="The goal is to turn data into information, and information into insight."
text1=text.upper()
print(text1)
text2=text1.replace(",","")
text2=text2.replace(".","")
print(text2)
text_list=text2.split()
print(text_list)
#Görev 3
lst=["D","A","T","A","S","C","I","E","N","C","E"]
#Adım1
eleman_sayilari=len(lst)
print(eleman_sayilari)
#Adım2
print(lst[0])
print(lst[10])
#Adım3
lst1=lst[0:4]
print(lst1)
#Adım4
lst.pop(8)
print(lst)
#Adım5
lst.append("Arda")
print(lst)
#Adım6
lst.insert(8,"N")
print(lst)


#GÖREV 4
dict={'Christian':["America",18],
      'Daisy':["England",12]
   ,'Antonio':["Spain",22],
      'Dante':["Italy",25]}
#Adım1
print(dict.keys())
#Adım2
print(dict.values())
#Adım3
dict['Daisy']=["England",13]
print(dict)
#Adım 4
dict['Ahmet']=["Turkey",24]
print(dict)
#Adım5
dict.pop('Antonio')
print(dict)
#Görev5
def function(List):
    even_list=[]
    odd_list=[]
    for i in List:
        if i% 2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return odd_list,even_list
l=[2,13,18,93,22]
function(l)
#Görev 6
ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
def Sıralama_öğrenci(ogrenciler):

    for i, ogrenci in enumerate(ogrenciler, start=1):
        if i <= 3:
            print(f"Mühendislik fakültesi {i}. öğrenci: {ogrenci}")
        else:
            print(f"Tıp fakültesi {i - 3}. öğrenci: {ogrenci}")

muh_fak = ogrenciler[:3]
tip_fak = ogrenciler[3:]
Sıralama_öğrenci(ogrenciler)
#Görev 7
ders_kod = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]
Tüm_dersler = zip(kredi, ders_kod, kontenjan)

for kredi,ders_kod,kontenjan in Tüm_dersler:
    print(f"Kredisi {kredi} olan {ders_kod} kodlu dersin kontenjanı {kontenjan} kişidir")
#Görev 8
kume1 = set(["data", 'pyhton'])
kume2 = set(["data", "function", "qcut", "lambda", "pyhton", "miuul"])
def kume_farki(kume1,kume2):
    if kume1.issuperset(kume2):
        ortaklar=kume1.intersection(kume2)
        print(ortaklar)
    else:
        farklar=kume2.difference(kume1)
        print(farklar)
kume_farki(kume1,kume2)