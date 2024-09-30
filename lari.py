N = int(input("Masukan Luas gua "))
x,vx = list(map(int,input("Masukkan lokasi anda dan kecepatan anda  ").split( )))
x1,v1 = list(map(int,input("Masukkan lokasi Penjahat 1 dan kecepatan Penjahat 1 ").split( )))
x2,v2 = list(map(int,input("Masukkan lokasi Penjahat 2 dan kecepatan Penjahat 2 ").split( )))
# x = 5 vx = 3 x1 = 2 v1 = 4 x2 = 3 v2 = 2 blx = 2

blx = (N + 1 - x) // vx
bsx = x  / vx

if (N + 1 - x) % vx != 0 :
    blx = blx + 1
if  x % vx != 0 :
    bsx += 1 

if x1 < x and x2 < x :
    if x + (blx*vx) > x1 + blx*v1 :
        print("Bebas")
    else :
        print("Tertangkap")

if x1 > x and x2 > x :
    if -x - blx*vx + x1 + blx*x1 > blx :
        print("Bebas")
    else :
        print ("Tertangkap")
if (x1 > x and x2 < x) or (x1 < x and x2 > x) :
    print("Tertangkap")