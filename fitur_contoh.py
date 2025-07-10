def kalkulator_sederhana(angka1, angka2, operasi):
    if operasi == 'tambah':
        return angka1 + angka2
    elif operasi == 'kurang':
        return angka1 - angka2
    elif operasi == 'kali':
        return angka1 * angka2
    elif operasi == 'bagi':
        if angka2 != 0:
            return angka1 / angka2
        else:
            return "Error: Pembagian dengan nol tidak diperbolehkan."
    else:
        return "Error: Operasi tidak dikenali."