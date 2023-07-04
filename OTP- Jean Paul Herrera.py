import numpy as np
from secrets import choice   # Se utiliza para producir valores hexadecimales aleatorios confiables
from string import printable # Lista de caracteres imprimibles para validar


def generate_key(length:int) -> str:
    #Genera una clave de caracteres ASCII imprimibles al azar
    
  
    key = ""

    abecedario = ['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    numeros_primos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    combined = np.append(abecedario, numeros_primos)

    np.random.shuffle(combined)

    for index in range(length):
        # Elije un caracter aleatorio
        key_letter =  choice(combined)
        key += (key_letter)

    return key

def encrypt(text:str, key:str) -> str:
    #Cifra el texto de entrada y devuelve el ciphertext
    
   
    ciphertext = ""

    for text_character, key_character in zip(text, key):
        if text_character not in printable:
            raise ValueError(f"Text value: {text_character} Error")

        # Funcion XOR
        xored_value = ord(text_character) ^ ord(key_character)

        # Toma el resultado de la funcion XOR y lo convierte en un caracter
        ciphertext_character = chr(xored_value)

        # Agrega el caracter generado al  ciphertext
        ciphertext += (ciphertext_character)

    return ciphertext

def decrypt(key:str, ciphertext:str) -> str:
    #Descifra el texto cifrado usando la llave usada
    
    
    plaintext = ""

    for key_character, ciphertext_number in zip(key, ciphertext):
        xored_value = ord(key_character) ^ ord(ciphertext_number)
        plaintext += chr(xored_value)



    return plaintext




if __name__ == "__main__":
    # El texto a cifrar
    text = '''Ey,ey, mas despacio, cerebrito'''

    # Genera una clave de la misma longitud que el texto
    key = generate_key(len(text))
    print(f"The key is: {key}")

    # Genera el ciphertext usando la llave y el plaintext
    ciphertext = encrypt(text, key)
    print(f"\nThe ciphertext is: {ciphertext}")

    # Decrypta y devuelve el plaintext original
    plaintext = decrypt(key, ciphertext)
    print(f"\nThe decrypted plaintext is: {plaintext}")
