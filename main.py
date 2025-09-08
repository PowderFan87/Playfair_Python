import string

def prepare_text(text, for_encryption=True):
    text = text.upper().replace("J", "I")
    text = ''.join(filter(str.isalpha, text))
    if for_encryption:
        prepared = ""
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i + 1] if i + 1 < len(text) else 'X'
            if a == b:
                prepared += a + 'X'
                i += 1
            else:
                prepared += a + b
                i += 2
        if len(prepared) % 2 != 0:
            prepared += 'X'
        return prepared
    else:
        return text if len(text) % 2 == 0 else text + 'X'

def create_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    seen = set()
    matrix = []
    for char in keyword + string.ascii_uppercase:
        if char not in seen and char != 'J':
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def display_matrix(matrix):
    print("\nPlayfair Cipher Matrix:")
    for row in matrix:
        print(" ".join(row))
    print()

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def encrypt_pair(matrix, a, b):
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

def decrypt_pair(matrix, a, b):
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:
        return matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

def playfair_encrypt(text, keyword):
    prepared = prepare_text(text, for_encryption=True)
    matrix = create_matrix(keyword)
    display_matrix(matrix)
    encrypted = ""
    for i in range(0, len(prepared), 2):
        encrypted += encrypt_pair(matrix, prepared[i], prepared[i+1])
    return encrypted

def playfair_decrypt(text, keyword):
    prepared = prepare_text(text, for_encryption=False)
    matrix = create_matrix(keyword)
    display_matrix(matrix)
    decrypted = ""
    for i in range(0, len(prepared), 2):
        decrypted += decrypt_pair(matrix, prepared[i], prepared[i+1])
    return decrypted

# Main interaction
if __name__ == "__main__":
    choice = input("Do you want to encrypt or decrypt? (E/D): ").strip().upper()
    if choice == 'E':
        plaintext = input("Enter the text to encrypt: ")
        keyword = input("Enter the keyword: ")
        encrypted_text = playfair_encrypt(plaintext, keyword)
        print("Encrypted text:", encrypted_text)
    elif choice == 'D':
        ciphertext = input("Enter the text to decrypt: ")
        keyword = input("Enter the keyword: ")
        decrypted_text = playfair_decrypt(ciphertext, keyword)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")