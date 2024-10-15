def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    seen = set()

    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            matrix.append(char)
            seen.add(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def prepare_text(plaintext):
    # Mengabaikan spasi dan mengganti 'J' dengan 'I'
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
            char2 = "X"

        if char1 == char2:
            text += char1 + "X"
            i += 1
        else:
            text += char1 + char2
            i += 2

    if len(text) % 2 != 0:
        text += "X"

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
