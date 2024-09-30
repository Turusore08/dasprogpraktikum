# Masukkan nilai x1, y1, xs, ys, xf, yf
x1, y1 = map(int, input().split())
xs, ys = map(int, input().split())
xf, yf = map(int, input().split())

# Menghitung jarak dari titik awal ke pusat lingkaran
jarak_awal = abs(x1 - xs) + abs(y1 - ys)

# Menghitung jarak dari titik akhir ke pusat lingkaran
jarak_akhir = abs(x1 - xf) + abs(y1 - yf)

# Menghitung jarak perjalanan yang ditempuh King
jarak_king = abs(xs - xf) + abs(ys - yf)

# Jika King bisa mencapai titik akhir tanpa menyentuh lingkaran
if jarak_akhir > jarak_king:
    print("Yes")
else:
    print("No")
