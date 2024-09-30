# Masukkan jumlah bilangan yang akan diuji
n = int(input("Masukkan jumlah bilangan: "))

# Masukkan semua bilangan dalam satu baris, dipisahkan oleh spasi
q_list = list(map(int, input("Masukkan bilangan-bilangan: ").split()))

#kita buat agar jumlah bilangannya tidak melebihi n
if len(q_list) != n :
    print(" Format tidak valdi")
else :

# Uji setiap bilangan yang ada di dalam q_list
    for q in q_list:
    # Jika bilangan tersebut lebih dari 0, maka bilangan tersebut bisa dinyatakan dalam penjumlahan 4 bilangan kuadrat
        if q >= 0:
            print("LEAVE")
        else:
            print("ERASE")
