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
  

# -------------------------------------------------------------------------- # 



# otam = {"ism":"davron", "yosh":43, "kasbi":"tadbirkor", "shaxri":"angren"}
# ism = otam["ism"].title()
# yosh = otam["yosh"]
# shaxar = otam["shaxri"].title()
# print(f" Otamning ismi {ism} yoshi {yosh} da, yashash joyi {shaxar} shahrida !")



# taomlar = {
#     "otam":"palov",
#     "buvim":"shorva",
#     "dadam":"shashlik",
#     "onam":"pizza",
#     "opam":"lavash"
#     }
# taom = taomlar["otam"]
# taom_2 = taomlar["dadam"]
# taom_3 = taomlar["opam"]
# print(f" Otamning sevimli taomi {taom} ! ")
# print(termins["integer"].title())
# print(termins["bool"].title())
# print(termins["print"].title())
# print(termins["list{}"].title())
# print(termins["github"].title())




# python_izohli_lugati = {
#    "integer": "Butun son",
#    "float": "O'nlik son",
#    "string": "Matn",
#    "list": "Ro'yxat",
#    "tuple": "O'zgarmas ro'yxat",
# }
# key = input(" Kerakli soznini kiriting : ").lower()
# termin = python_izohli_lugati.get(key) 
# if termin == None:
#     print(" Bunday soz mavjud emas ! ")
# else:
#     print(f"{key.title()} sozining manosi \
# {python_izohli_lugati[key]} deb tarjima qilinadi !")


# -------------------------------------------------------------------------- #




# elon_musk = {
#             "ism":"elon",
#             "familiya":"musk",
#             "t_yil":"1971",
#             "t_shaxri":"pretoriya",
#             "companies":['spacex', 'tesla']
#         }
# bill_gates = {
#             "ism":"bill",
#             "familiya":"gates",
#             "t_yil":"1955",
#             "t_shaxri":"ssietl",
#             "companies":['microsoft', 'macintosh']
#         }
# jeff_bezos = {
#             "ism":"jeff",
#             "familiya":"bezos",
#             "t_yil":"1964",
#             "t_shaxri":"albukerk",
#             "companies":['amazon', 'amazon.com']
#         }
# abdumanabov_doston = {
#             "ism":"doston",
#             "familiya":"abdumanabov",
#             "t_yil":"2002",
#             "t_shaxri":"angren",
#             "companies":['a_d_d_2002', 'add.inc']
#         }
# mark_zuckerberg = {
#             "ism":"mark",
#             "familiya":"zuckerberg",
#             "t_yil":"1984",
#             "t_shaxri":"white plains",
#             "companies":['facebook', 'meta']
#         }

# famous = [elon_musk, bill_gates, jeff_bezos, abdumanabov_doston, mark_zuckerberg]



# for person in famous:
#         print(f"{person['ism'].title()} {person['familiya'].title()}, "
#               f"{person['t_shaxri'].title()} da "
#               f"{person['t_yil']} - da tavallud topgan ! ")

# for person in famous:
#     ism = person['ism']
#     familiya = person['familiya']
#     print(f" \n{ism.title()} {familiya.title()}ning kompaniyalari : ", end='')
#     for company in person['companies']:
#         print(company.title(), end=' ')

# dostlar = {
#     'ali':['spider-man', 'venom'],
#     'vali':['iron-man', 'deadpool'],
#     'husan':['super-man', 'marvel'],
#     'hasan':['capitain america', 'hulk']
#     }
# for dost in dostlar:
#     ism = dost.title()
#     filmlar = dostlar[dost]
#     print(f" \n{ism}ning sevimli filmlari : ")
#     for film in filmlar:
#         print(f"{film.title()} ", end='')
    



# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")
  
      
# -------------------------------------------------------------------------- #      
      
# print(' Sonning kvadratini hisoblaydigan dastur ! ')
# savol = ' Kerakli sonni kiriting : '  
# qiymat = True
# while qiymat:
#     qiymat = input(savol)
#     if qiymat.lower() == 'exit':
#       qiymat = False
#     else:
#         print(" Javob : ", float(qiymat)**2)
# print(' Dastur tugadi !')     
 


# print('\n Barcha yahshi ko\'rgan kitoblarizni kiriting,', 
#       'agar dasturni to\'xtatmoqchi bo\'sangiz \'stop\' deb yozing !')    
# savol = ' Yahshi ko\'rgan kitobizni kiriting : '
# bool = True
# books = []
# while bool:
#     book = input(savol)
#     books.append(book)
#     if book.lower() == 'stop':
#         bool = False
#         del books[-1]
#         print(f' \nSiz yahshi ko\'rgan kitoblar {books} ! ')
        
        
    
# savol = '\n Yoshingizni kiriting : '
# yoshlar = 2000    
# osmirlar = 5000
# kattalar = 10000
# qarilar = 'bepul'
# app = True
# savol = int(input(savol))
# while app:
#     if savol < 7:
#         print(f' {savol} yoshlilar uchun chipta narxi {yoshlar} so\'m !')   
#         app = False
#     elif savol > 7 and savol <= 18:
#         print(f' {savol} yoshlilar uchun chipta narxi {osmirlar} so\'m !')      
#         app = False    
#     elif savol > 18 and savol <= 65:
#         print(f' {savol} yoshlilar uchun chipta narxi {kattalar} so\'m !')      
#         app = False
#     elif savol > 65:
#         print(f' {savol} yoshlilar uchun chipta narxi {qarilar} !')      
#         app = False 
        
 
        
 
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# 
# while True:
#     qiymat = input(savol)
#     if qiymat.lower() == 'exit':
#         break
#    elif int(qiymat) < 0:
#         continue    
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")        
# print(' Dastur tugadi ! ')       
        
        
# --------------------------------------------------------------------------        
        
        
        
        
# print(' Do\'stlaringizni royhatini tuzadigan dastur ! ')
# dostlar = []
# n = 1
# while True:
#     savol = (f' {n} - do\'stingizni kiriting : ')
#     ism = input(savol)
#     dostlar.append(ism)
#       takrorlash = input(' Yana do\'stingizni qo\'shmoqchimisiz ? (ha/ yo\'q) : ')
#     n += 1
#     if takrorlash != 'ha':
#         break
# print(' Yaqin do\'stlaringiz ro\'yhati : ', dostlar)       
        
        
# dostlar = {}

# ishora =True
# n = 1
# while ishora:
#     ism = input(f' {n} - do\'stingizni kiriting : ')
#     yosh = input(f' {ism.title()}ning yoshini kiriting : ')
#     n += 1
#     dostlar[ism] = int(yosh)  
      
#     javob = input(' Yana do\'stingizni qo\'shasizmi (ha/yo\'q) ? >>>> ')
#     if javob != 'ha':
#        ishora = False
# print(' Do\'stlaringiz haqida malumot : ')
# for ism, yosh in dostlar.items():
#     print(f' {ism.title()}ning yoshi {yosh} yoshda ! ')
    



# menu = []
# ishora = True
# n = 1   

# print(' Kerakli mahsulotlarni kiritin, "stop" so\'zini dasturni to\'xtatish uchun yozing ! ')
# while ishora:
#     savol = (f' {n} - mahsulotlarni kiriting : ')
#     mahsulot = input(savol)
#     mahsulotlar = menu.append(mahsulot)
#     n += 1
#     if mahsulot.lower() == 'stop':
#         ishora = False
#         del menu[-1]
# print(f' Siz kiritgan mahsulotlar : {menu}')
      
        
# ishora = True
# bozor = {}
# n = 1
# while ishora:
#       savol_1 = (f' {n} - mahsulotni kiriting => ')
#       mahsulot = input(savol_1)
#       savol_2 = (f' {mahsulot} mahsulotining narxini kiriting => ')
#       narx = input(savol_2)
#       savol_3 = (' Davom etamizmi ? => ')
#       savol = input(savol_3)
#       bozor[mahsulot] = narx
#       n += 1
#       if savol != 'ha':
#           break
# print(' Bozor mahsulotlari : ') 
# for mahsulot, narx in bozor.items():   
#     print(f' {mahsulot.title()}ning narxi {narx} so\'m')    
 
    
 
# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")    
 

    
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000,
#                'pepsi':10000,
#                'non':1500,
#                'go\'sht':75000,
#                'sabzi':4000,
#                'piyoz':2500,
#                'karam':7000,
#                'suv':3000,
#                'shokolad':7500    
#     }
# print('\n Do\'kondagi mahsulotlar va ularning narxlari : \n')     
# for items, prices in mahsulotlar.items():    
#     print(f' {items.title()}  -  {prices} so\'m ')     
# buyurtmalar = []
# buyurtmalar_nomi = []
# n = 1
# ishoralar = input(' Nechta mahsulot harid qilmoqchisiz ? ==>>>  ')
# ishoralar= int(ishoralar)
# print(' \n Kerakli mahsulotlarni kiriting : ')
# while ishoralar:
#     savol_1 = (f' {n} - mahsulotni kiriting => ')
#     mahsulot = input(savol_1)
#     if mahsulot in mahsulotlar.keys():
#         buyurtmalar.append(mahsulotlar[mahsulot])
#         if mahsulot in mahsulotlar.keys():
#             buyurtmalar_nomi.append(mahsulot)
#     else:
#         print(' Bizda bunday mahsulot yo\'q ! ')
#     n += 1
#     ishoralar -= 1    
# summa = 0
# for narxlar in buyurtmalar:
#     summa += narxlar
# print('\n Umumiy sotib olgan mahsulotlariz : ')
# for o_mahsulotlar in buyurtmalar_nomi:
#     print(f' {o_mahsulotlar.title()} ')
# print(' Umummiy summa : ', summa, ' so\'m ! ') 
    


# ismlar = []
# n=1
# while True:
#     ism = input(f' {n} - do\'stingizni ismini kiriting : ')
#     ismlar.append(ism)
#     n+=1
#     takrorlash = input(' Davom etamizmi (ha/yo\'q) ?  ===>>> ')
#     if takrorlash != 'ha':
#         break
# print(' Dostlaringiz toyhati : \n')    
# for dost in ismlar:
#     print(f' {dost.title()} ')
    
 
# dostlar = {}
# ishora = True
#
# while ishora:
#     ism = input(' Do\'stingizni isminini kiriting : ')
#     yosh = input(f' {ism.title()}ning yoshini kiriting : ')
#     dostlar[ism] = int(yosh)
#     javob = input(' Davom etamizmi (ha/yo\'q) ? ==>> ')
#     if javob.lower() != 'ha':
#         ishora = False
# print(' Dostlaringizni malumoti : ')
# for ism, yosh in dostlar.items():
#     print(f' {ism.title()} {yosh} yoshda !')
                

# def ty_hisoblash (ism, yosh):
#     """ Foydalanuvchini tugilgan yilini hisoblovchi dastur !"""
#     print(f' {ism.title()} siz {2022-yosh} - yilda tugilgansiz  !')
# 
# ty_hisoblash(' Doston', 19)



# def kub (son):
#     """ Kiritilgan sonni kubini hisoblovchi funksiya,
#      Kiritilgan sonni kubini hisoblovchi funksiya ! """
#      
#     print(f' {son} sonning kvadrati {son**2} ga teng !')
#     print(f' {son} sonning kubi {son**3} ga teng !') 
# kub(2)



# def toq_juft (son):
#     """ Sonning juft yoki toqligini tekshiruvchi funksiya !"""
#     if son % 2 == 0:
#         print(f' {son} - juft son !') 
#     else:
#         print(f' {son} - toq son !')



# def max_min (son_1, son_2):
#     """ katta sonni aniqlovchi funksiya ! """
#     if son_1 > son_2:
#         print(f' {son_1} > {son_2}')
#     elif son_1 < son_2:
#         print(f' {son_1} < {son_2}')
#     else:
#         print(f' {son_1} = {son_2}')



# def son_daraja (son, daraja):
#     """ Sonning darajasini hisoblovchi funksiya ! """
#     print(f' {son} ning {daraja} darajasi {son**daraja} ga teng ! ')
# son_1 = int(input(' Sonni kiriting : '))
# daraja_1 = int(input(' Darajani kiriitng : '))
# son_daraja(son_1, daraja_1)




# sonlar = list(range(2,11))
# def son (son):
#     for boluvchilar in sonlar:
#         if son %  boluvchilar == 0:
#             print(f' {son} soni {boluvchilar} ga qoldiqsiz bo\'linadi !')
#         else:
#             continue


# def between(min, max, plus=''):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         if plus:
#             min += plus
#         else:
#             min += 1
#     return sonlar
# print(between(2, 10, 3))




# def info(ism, familiya, t_yil, t_joyi, tel_raqam='', el_manzil=''):
#     person = {'ism':ism,
#               'familiya':familiya,
#               't_yil':t_yil,
#               't_joyi':t_joyi,
#               'tel_raqam':tel_raqam,
#               'el_manzil':el_manzil
#               }
#     return person
# Doston = info('doston', 'abdumanabov', 2002, 'angren', '+998940146144', 'abdumanabovdoston@gmail.com')
# Damir =  info('admir', 'abdumanabov', 2012, 'toshkent', '+998935150108', 'danil955954@gmail.com')   
# Diyora = info('diyora', 'abdumanabova', 2001, 'angren', '+998997906144', 'diyoraabdumanabova@gmail.com')
# members = [Doston, Damir, Diyora]
# for info in members:    
#     print(f"{info['familiya'].title()} {info['ism'].title()} "
#           f"{info['t_yil']} yilda {info['t_joyi'].title()} shaxrida tug\'ilgan,"
#           f" telefefon raqami {info['tel_raqam']}")    
    
    
  
    
# def maximum(son1, son2, son3):
#     print(max(son1, son2, son3))
# maximum(2, 3, 1)    
    
 
    
 
# def aylana(radius, diametr='', yuzi=''):
#      pi = 3.14
#      diametr  = radius * 2
#      yuzi = pi * (radius ** 2)
#      info = {'radius':radius,
#              'diametr':diametr,
#              'yuzi':yuzi}
#      return info

# misol1 = aylana(10)
# print(f" {misol1['radius']} sm radiusli" 
#        f" aylananing diametri {misol1['diametr']} sm ga"
#        f" teng va yuzi {misol1['yuzi']} sm.kvadrat ga teng !")


    
   
# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar       
# tub = tub_sonlar_top (2, 20)     

    
 