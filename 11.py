S = input("Masukkan string soal ujian: ") # Masukkan soal yang ada di kertas



if len(S) >= 100000 or len(S) <= 1 :
    print ("Format tidak valid")
else :
    sandi = ""
    
    for char in S:
        if char not in sandi and char != " ":
            sandi += char

    print(sandi)
