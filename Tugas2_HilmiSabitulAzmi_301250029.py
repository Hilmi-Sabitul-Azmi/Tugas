#soal 1 - menentukan bilangan positif, negatif, atau nol
#menentukan fungsi
def menentukan_bilangan(bilangan):
    if bilangan > 0:
        return 'positif'
    elif bilangan < 0:
        return 'negatif'
    elif bilangan == 0:
        return 'nol'

#meminta input dari pengguna
bilangan = int(input('masukaan bilangan :'))
#membuat variable hasil agar variable bilangan di eksekusi bersama fungsi
hasil = menentukan_bilangan(bilangan)
#output
print('bilangan',hasil)


#soal 2 menentukan nilai huruf 
#menentukan fungsi
def menentukan_nilai(nilai):
    if nilai >= 85:
        return 'A'
    elif nilai >= 70:
        return 'B'
    elif nilai >= 55:
        return 'C'
    elif nilai >= 40:
        return 'D'
    else:
        return 'E'

#meminta input dari pengguna 
nilai = int(input('masukkan nilai :'))
#membuat variable hasil agar variable nilai dieksekusi bersama fungsi
hasil = menentukan_nilai(nilai)
#output
print('nilai huruf :',hasil)


#soal 3 - program kasir diskon
#menentukan fungsi
def hitung_diskon (total):
    if total >= 500_000:
        persen = 20
    elif total >= 250_000:
        persen = 10
    else :
        persen = 0
    return total * persen / 100

print('=====masukkan harga barang disini=====')
#meminta input dari pengguna
barang_1 = float(input('masukkan harga (Rp):'))
barang_2 = float(input('masukkan harga (Rp):'))
#membuat variable untuk output
total_belanja = barang_1 + barang_2
diskon = hitung_diskon(total_belanja)
total_bayar = total_belanja - diskon

#output
print('=====struk pembayaran=====')
print(f'total belanja : Rp. {total_belanja:,.0f}'. replace(',','.'))
print(f'diskon : Rp. {diskon:,.0f}'. replace(',','.'))
print(f'total bayar : Rp. {total_bayar:,.0f}'. replace(',','.'))

