def encrypt(plaintext: str, key: int) -> str:
    chipertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            chipertext[col] += plaintext[pointer]
            pointer += key
    return "".join(chipertext)

def decrypt(chipertext: str, key: int) -> str:
    num_of_cols = int(len(chipertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(chipertext)
    plaintext = [""] * num_of_cols
    col = 0
    row = 0
    
    for symbol in chipertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return "".join(plaintext)