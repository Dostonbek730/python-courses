# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -------------------------------------------------------------------------- #

# ismlar = ["Doston", "Dior", "Azizz"]
# print(ismlar)
# print("\nSalom", ismlar[1], "bugun choyhona bormi?")
# print(ismlar[2], "choyhonaga boramizmi?")

# -------------------------------------------------------------------------- #

# tarixiy_shaxslar = ["Ibn Sino", "Al-Xorazmiy", "Navoiy"]
# zamonaviy_shaxslar = ["Bill Geyts", "Jeff Bezos", "Ilon Musk"]
# tarixiy_shaxs = tarixiy_shaxslar.pop(2) 
# zamonaviy_shaxs = zamonaviy_shaxslar.pop(2)
# print("Men tarixiy shaxslardan", tarixiy_shaxs, "bilan uchrashishni istardim,")
# print("zamonaviy shaxslardan esa", zamonaviy_shaxs, "bilan suxbatlashishni istardim.")

# -------------------------------------------------------------------------- #

# friends = []
# friends.append("Dior")
# friends.append("Aziz")
# friends.append("Damir")
# friends.append("Doston")
# friends.append("Shox")
# friends.append("Vohid")
# friends.append("Eldor")
# friends.insert(0, "Axror")

# print("Barcha dostlarim : ", friends)
# friends.remove("Shox")
# mehmonlar = []
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(2))
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(3))
# print("\nMehmonga kelolmagan dostlarim : ", friends)
# print("\nMehmonga kelgan dostlarim : ", mehmonlar)

# -------------------------------------------------------------------------- #

# countries = ["Uzbekistan", "USA", "Turkey", "Russia"]
# print(countries)
# print("\n Siz kiritgan davlatlar soni :", len(countries))
# countries.sort()
# print(" Royhat tartibli joylashgan nushasi :", countries)
# countries.sort(reverse=True)
# print(" Royhatning asl nusxasi :", countries)

# sonlar = list(range(120, 1200, 2))
# print(sonlar)
# print("\n Barsha royhatdagi sonlara yigindisi :", sum(sonlar))
# print(" Royhatdagi eng katta va eng kichik sonlar ayirmasi :", max(sonlar)-min(sonlar))
# print(" Royhatdagi elementlar soni :", len(sonlar))
# print(" Royhatdagi birinchi 20 ta son :", sonlar[0:21])
# print(" Royhatning ortadasidagi 20 ta son :", sonlar[270:291])
# print(" Royhatning oxirgi 20 ta son :", sonlar[520:541])

# taomlar = ["Osh", "Manti", "Mastava", "Shorva", "Qozon kabob"]
# nonushta = taomlar[:]
# nonushta.remove("Osh")
# nonushta.remove("Manti")
# nonushta.remove("Qozon kabob")
# nonushta.append("Kasha")
# nonushta.append("Bulochka")
# print("\n Barcha kiritngan taomlaringiz :", taomlar)
# print(" Barcha nonushtaga yeyiladigan taomlaar :", nonushta)
# nonushta.insert(0, "Non va choy")
# print(" Barcha nonushtaga yeyiladigan taomlaar :", nonushta)
# nonushta = tuple(nonushta)
# nonushta.insert(0, "Non")
# print(" Ozgarmas royhatga aylandi", nonushta)
# print(" Ozgarmas royhatning birinchi taomi :", nonushta[0])

# -------------------------------------------------------------------------- #

# ismlar = ["Doston", "Aziz", "Dior", "Damir", "Vohid"]
# for ism in ismlar:
#     print(" Salom", ism, "\n")
# print(" Kod", len(ism), "martda takorlandi")

# toq_sonlar = list(range(11, 101, 2))
# for sonlar_kubi in toq_sonlar:
#     print(sonlar_kubi**3)

# films = []
# print(" Filmlar nomini kiritig !")
# for film in range(5):
#      films.append(input(f"{film+1} - film : "))
# print("\n Siz kiritgan filmlar : ", films)

# odamlar = []
# print(" Bugun nechta inson bilan subhatlawdiz ?")
# for k in range(5):
#     odamlar.append(input(k+1, " - inson : "))
# print(" Siz subhatlawgan insonlar : ", odamlar)

# -------------------------------------------------------------------------- #

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#   if car !='gm':
#     print(car.title())
#   else:
#     print(car.upper())
# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin.
# Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring.
# Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.



# ismlar = input("Ismingizni kiriting : ")
# if ismlar.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {ismlar}!")



# login = input("Login kiriting: ")
# if login.lower() == 'admin':
#     print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {login.title()}!")



# son_1 = input(" 1 - sonni kiriting : ")
# son_2 = input(" 2 - sonni kiriting : ")
# if son_1 == son_2:
#     print("", son_1, "va", son_2, " teng ekan !" )
# else:
#     print("", son_1, "va", son_2, " teng emas ekan !")



# son = int(input(" Son kiriting : "))
# if son > 0:
#     print(" Musbat son kirittingiz !")
# else:
#    print(" Manfiy son kirittingiz !")



# son = int(input(" Son kiriting : "))
# if son > 0:
#     print(son**(1/2))
# else:
#     print(" Musbat son kiriting !")

# -------------------------------------------------------------------------- #

# son = int(input(" Juft son kiriting : "))
# if son % 2 == 0:
#     print(" Rahmat ! ")
# else:
#     print(" Bu juft son emas ! ")    
    


# yosh = int(input(" Yoshingizni kiriting : "))
# if yosh <= 4 or yosh >= 60:
#     print(" Sizga kirish bepul ! ")
# if yosh < 18 and yosh > 4:
#     print(" Sizga kirish 10.000 so'm !")
# if yosh > 18 and yosh < 60:
#     print(" Sizga kirish 20.000 so'm !")
    

# son_1 = int(input(" 1 - sonni kiriting : "))
# son_2 = int(input(" 2 - sonni kiriting : "))
# if son_1 > son_2:
#     print(f"\n {son_1} > {son_2}")
# elif son_1 < son_2:
#     print(f"\n {son_1} < {son_2}")
# else:
#     print(f"\n {son_1} = {son_2}")
   

# dokon = ["uzum" , "anor" , "nok" , "olma" , "banan" , "ananas" , "pomidor" ,
#          "bodring" , "piyoz" , "kartoshka"]
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1} - mahsulotni kiriting : "))
# for mahsulot in savat:
#     if mahsulot in dokon:
#         print(f"{mahsulot} dokonda bor !")
#     else:
#         print(f"{mahsulot} dokonda yoq !")


# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 
# 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan 
# va do'konda bor mahsulotlarni yangi bor_mahsulotlar degan ro'yxatga,
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.
# Agar mavjud_emas ro'yxati bo'sh bo'lsa, 
# "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni,
# aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." 
# degan xabarni chiqaring.


# print("\n")    
# cars = ["damas", "gentra", "spark", "captiva"]
# print(cars)
# print(" 2 ta avtomobil tanlag !")
# selected = []
# for n in range(2):
#     selected.append(input(f" {n+1} - avtomobilni kiriiting : "))
# bor_avtolar = []
# yoq_avtolar = []
# for car in selected:
#     if car in cars:
#         bor_avtolar.append(car)
#     else:
#         yoq_avtolar.append(car)       
# if yoq_avtolar:
#     print(" Bizda ushbu avtolar yoq")
#     for car in yoq_avtolar:
#         print("", car)
# else:
#     print(" Bizda hamma avtolar bor !")
        


    










