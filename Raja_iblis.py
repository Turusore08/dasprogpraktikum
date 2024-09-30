U = int(input("Masukkan HP darah ucup   :   "))
M = int(input("Masukkan jumlah minion lawan :   "))
K = int(input("Masukkan banyak knight iblis :   "))



AP_U = 100
AP_M = 2
AP_K = 5
AP_RI = 100
HP_M = 100
HP_K = 500
HP_RI = 1000
attack_K = HP_K // AP_U
attack_RI = HP_RI // AP_U


if U - (AP_M * (M// 2))   > 0 :
    U = U - (AP_M * (M// 2)) 
    
else:
    print("Yah! Ucup meninggoy")



if U - (AP_K * (K//2)) * attack_K> 0 :
    U -= (AP_K * (K//2)) * attack_K



else :
    print (" Lemah banget cup")



if U - (AP_RI) * attack_RI> 0 :
    U -= (AP_RI) * attack_RI 
    print(f"Yey! Ucup menang ! HP tersisa : {U}")
else :
    print (" Lemah banget cup")
   