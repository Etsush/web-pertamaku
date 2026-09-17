nama = "putra"
nilai_awal = 85
Nilai_UTS = 90 

nilai_akhir = (nilai_awal*0.6 +  Nilai_UTS*0.4)
if nilai_akhir >= 85:
    print(nama + " lulus dengan nilai akhir " + str(nilai_akhir))
else:
    print(nama + " tidak lulus dengan nilai akhir " + str(nilai_akhir))
    