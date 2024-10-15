# kriptografi

![Screenshot 2024-10-15 091401](https://github.com/user-attachments/assets/09878395-77bf-46bb-b50e-a73367ec8513)



# Enkripsi Playfair Cipher

 Enkripsi Playfair Cipher menggunakan matriks kunci yang dihasilkan dari kunci yang diberikan. Untuk kunci "TEKNIK INFORMATIKA", matriks kunci 5x5 yang dihasilkan adalah sebagai berikut:

![Screenshot 2024-10-15 085900](https://github.com/user-attachments/assets/e4b1ec51-5d2f-4cb2-b4e9-cd2a0505d9d5)

### Contoh Enkripsi
Berikut adalah beberapa contoh plaintext yang dienkripsi menggunakan matriks kunci di atas:

#### Plaintext 1: GOOD BROOM SWEEP CLEAN

- Pasangan Huruf: GO, OD, BR, OM, SW, EE, PC, LE, AN
- Hasil Enkripsi: DN, RC, DO, FA, PY, KK, WL, TP, MI

#### Plaintext 2: REDWOOD NATIONAL STATE PARK

- Pasangan Huruf: RE, DW, OD, NA, TI, ON, AL, ST, AT, EP, AR, KX
- Hasil Enkripsi: OK, CX, RC, IM, EN, FM, TP, LP, MF, TW, MA, QW
  
#### nPlaintext 3: JUNK FOOD AND HEALTH PROBLEMS
- Pasangan Huruf: JU, NK, FO, OD, AN, DX, HE, AL, TH, PR, OB, LE, MS
- Hasil Enkripsi: IZ, IN, OR, RC, MI, QW, AC, TP, IA, QO, FD, TP, AU
  
### Penjelasan Proses Enkripsi
Matriks Kunci: Matriks kunci dibangun dari huruf-huruf yang ada di dalam kunci, dengan menghilangkan huruf yang berulang dan menggantikan 'J' dengan 'I'.


Menyiapkan Teks: Plaintext disiapkan dengan mengabaikan spasi dan membagi teks menjadi pasangan huruf. Jika terdapat huruf yang sama dalam pasangan (seperti "EE"), huruf kedua diganti dengan "X".


Enkripsi: Setiap pasangan huruf dienkripsi menggunakan aturan Playfair Cipher berdasarkan posisi mereka dalam matriks kunci.
