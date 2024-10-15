
```
def generate_key_matrix(key):
    key = key.upper().replace("J", "I")  # Mengganti 'J' dengan 'I'
    matrix = []
    seen = set()

    # Menambahkan karakter dari kunci ke dalam matriks
    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)

    # Menambahkan huruf yang tersisa ke dalam matriks
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Menggunakan 'I' menggantikan 'J'
        if char not in seen:
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]  # Membuat matriks 5x5

def prepare_text(plaintext):
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    text = ""

    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        if not char1.isalpha():
            i += 1
            continue

        if i + 1 < len(plaintext):
            char2 = plaintext[i + 1]
        else:
            char2 = "X"  # Tambahkan 'X' jika tidak ada pasangan

        if char1 == char2:
            text += char1 + "X"  # Ganti dengan 'X' jika huruf sama
            i += 1
        else:
            text += char1 + char2
            i += 2

    if len(text) % 2 != 0:
        text += "X"  # Tambahkan 'X' jika jumlah huruf ganjil

    return text

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def encrypt_pair(matrix, char1, char2):
    pos1 = find_position(matrix, char1)
    pos2 = find_position(matrix, char2)

    if pos1 is None or pos2 is None:
        raise ValueError(f"Karakter '{char1}' atau '{char2}' tidak ditemukan dalam matriks")

    row1, col1 = pos1
    row2, col2 = pos2

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt_playfair(plaintext, key):
    matrix = generate_key_matrix(key)
    prepared_text = prepare_text(plaintext)
    ciphertext = ""

    for i in range(0, len(prepared_text), 2):
        char1 = prepared_text[i]
        char2 = prepared_text[i + 1]
        ciphertext += encrypt_pair(matrix, char1, char2)

    return ciphertext

def decrypt_pair(matrix, char1, char2):
    pos1 = find_position(matrix, char1)
    pos2 = find_position(matrix, char2)

    if pos1 is None or pos2 is None:
        raise ValueError(f"Karakter '{char1}' atau '{char2}' tidak ditemukan dalam matriks")

    row1, col1 = pos1
    row2, col2 = pos2

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_playfair(ciphertext, key):
    matrix = generate_key_matrix(key)
    prepared_text = ""
    
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]
        prepared_text += decrypt_pair(matrix, char1, char2)

    # Menghapus 'X' yang ditambahkan sebagai padding
    prepared_text = prepared_text.replace('X', '')  # Menghapus semua 'X' dari hasil dekripsi

    return prepared_text

# Input kunci dan plaintext
key = "TEKNIK INFORMATIKA"
plaintexts = [
    "GOOD BROOM SWEEP CLEAN",
    "REDWOOD NATIONAL STATE PARK",
    "JUNK FOOD AND HEALTH PROBLEMS"
]

# Hasil enkripsi
for i, plaintext in enumerate(plaintexts, 1):
    try:
        ciphertext = encrypt_playfair(plaintext, key)
        print(f"Plaintext {i}: {plaintext}")
        print(f"Ciphertext {i}: {ciphertext}\n")
    except ValueError as e:
        print(f"Error pada Plaintext {i}: {e}")

# Contoh dekripsi
ciphertexts = [
    "CMRCDFRWRAPYKWOWBPIOKY",
    "OKCXRWRCIMETMEFULNFIOWFMRK",
    "AZINORRCMIGBIOVFCUMRLVNOQY"
]

for i, ciphertext in enumerate(ciphertexts, 1):
    try:
        decrypted_text = decrypt_playfair(ciphertext, key)
        print(f"Ciphertext {i}: {ciphertext}")
        print(f"Decrypted Plaintext {i}: {decrypted_text}\n")
    except ValueError as e:
        print(f"Error pada Ciphertext {i}: {e}")
```


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
