status = ''

def username():
    print()
    inputan = input("Masukkan Username : ")
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3 = inputan.capitalize()

    if cek1 > 9 and cek2 == False and cek3 == inputan:
        status = "Berhasil"
        return inputan, status
    else :
        inputan = "Username tidak valid"
        status = "Gagal"
        return inputan, status

def email():
        inputan = input("Masukkan Email : ")
        cek1 = len(inputan)
        cek2 = ' ' in inputan
        cek3 = '@' and '.' in inputan

        if cek1 > 7 and cek2 == False and cek3 == True:
            status = "Berhasil"
            return inputan, status

        else :
            inputan = "Email tidak valid"
            status = "Gagal"
            return inputan, status

def nomor():
    inputan = input("Masukan Nomor Handphone :")
    cek1 = len(inputan)
    cek2 = ' ' in inputan 
    cek3 = inputan.isdigit()
    
    if cek1 > 7 and cek2 == False  and cek3 == True  :
        status = "Berhasil"
        return inputan, status 
    
    else :
        inputan = "Nomor handphone salah "
        status ="Gagal"
        return inputan , status
        

while True:
    u1, u2 = username()
    e1, e2 = email()
    i1, i2 = nomor()

    print("\nUsername = ", u1)
    print("Status = ", u2)
    
    print("\nEmail = ", e1)
    print("\nStatus = ", e2)

    print ("\nNomor Handphone=",i1)
    print ("Status =",i2)
    