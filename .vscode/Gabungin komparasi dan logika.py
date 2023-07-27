print("====KOMPARASI DAN LOGIKA")

inputUser = float(input("Masukan nilai kurang dari 3 lebih besar dari 10 adalah "))

#kurang dari
iskurangdari = (inputUser < 3)
print('Kurang dari 3 ', iskurangdari)


#lebih dari
islebihdari = (inputUser > 10)
print('Lebih dari 10 ', islebihdari)

isCorrect = iskurangdari or islebihdari
print("(or) Angka yang anda masukan adalah", isCorrect)

inputUser = float(input("Masukan nilai kurang dari 3 lebih besar dari 10 adalah "))

#kurang dari
iskurangdari = (inputUser < 3)
print('Kurang dari 3 ', iskurangdari)


#lebih dari
islebihdari = (inputUser > 10)
print('Lebih dari 10 ', islebihdari)

isCorrect = iskurangdari and islebihdari
print("(and) Angka yang anda masukan adalah", isCorrect)