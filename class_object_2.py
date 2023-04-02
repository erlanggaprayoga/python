# siswa (isinya ada nama dan asal)
# fungsinya atau operation = taaruf

class siswa :
    nama = None
    asal = None

    def taaruf(self):
        print(f'Halo Saya {self.nama} dari {self.asal}')

# kita panggil

juan = siswa()
juan.nama = input("Siapa Nama Anda? :") 
juan.asal = input("asalnya? :")

# panggil fungsinya
juan.taaruf()