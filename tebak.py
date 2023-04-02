# Garis
def garis():
    print("===========================")
# Masukin Dulu Angkanya
import random
angka_rahasia = random.randint(1, 100)
# Tebak Angka
garis()
print("Kami telah memiliki angka, Silahkan tebak!")
garis()
# Pertanyaan/QuizS
while True:
    jawaban = int(input("\n Masukan Angka : "))
    if jawaban == angka_rahasia:
        print("Selamat, Anda Menebak Dengan Benar!")
    else:
        print(
            'tebakan mu terlalu '
            'kecil' if jawaban < angka_rahasia else 'besar'
        )