# Input string pada baris pertama
S = input("Masukkan string: ")

# Input bilangan n pada baris kedua
n = int(input("Masukkan jumlah angka (n): "))

# Input bilangan x pada baris ketiga sebanyak n kali
x_list = list(map(int, input(f"Masukkan {n} angka dipisahkan dengan spasi: ").split()))

if len(x_list) != n:
    print("Format tidak valid")
else:
    # Panjang string dan n
    if len(S) > 100:
        print("Panjang string tidak boleh lebih dari 100.")
    elif n > 50:
        print("Jumlah angka tidak boleh lebih dari 50.")
    else:
        # Setiap x harus <= panjang string
        if all(0 <= x < len(S) for x in x_list):
            # Gabungkan charnya
            hasil_sandi = ''.join([S[x] for x in x_list])
            print("Isi pesan yang sudah dipecahkan:", hasil_sandi)
        else:
            print("Indeks x melebihi panjang string.")
