gaji = 1500000
perhari = 15000
tunjangan = 750000

Profil = {
    "rio" :{
    "Nama" : "Rio Darmawan",
    "Status" : "tetap",
    },
    "fajar" : {
    "Nama" : "Fajar Amrullah",
    "Status" : "kontrak",
    },
    "suhada" :{
    "Nama" : "Rafsanzani Suhada",
    "Status" : "kontrak",
    },
    "bayu" : {
    "Nama" : "Bayu Fedra Abdillah",
    "Status" : "tetap",
    },
    "fauzan" :{
    "Nama" : "Ahmad Fauzzan Maghribi",
    "Status" : "kontrak",
    },
    "malik" : {
    "Nama" : "Malik al-Qorni",
    "Status" : "kontrak",
    },
}

name = str(input("Masukan Nama  : "))
kehadiran = int(input("Masukan Hari Kehadiran : "))

if Profil[name]["Status"] == "tetap" :
        hadir = kehadiran * perhari 
        homepay = gaji + tunjangan + hadir
elif Profil[name]["Status"] == "kontrak" :
        homepay = gaji
else :
    print(" ")

print("Nama :" ,Profil[name]["Nama"])
print("Status :",Profil[name]["Status"])
print("Kehadiran:",kehadiran, "Hari")
print("Take Home Pay:","Rp."+ str(homepay))
