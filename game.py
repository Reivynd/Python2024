import random


# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_fails = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")

# Selección de nivel
print("Seleccione un nivel de dificultad:")
print("-Ingrese 1 para dificultad fácil:")
print("-Ingrese 2 para dificultad media:")
nivel = int(input())
while nivel < 1 or nivel > 2:
    print("Seleccione un nivel de dificultad válido")
    print("Ingrese 1 para dificultad fácil:")
    print("Ingrese 2 para dificultad media:")
    nivel = int(input())
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = ""

# Mostrar la palabra con pistas para nivel fácil
if nivel == 1:
    for letter in secret_word:
        if letter in "aeiou":
            word_displayed += letter
        else:
            word_displayed += "-"

    print(f"Palabra: {word_displayed}")

# Mostrar la palabra con pistas para nivel medio

elif nivel == 2:
    word_normal = secret_word[0]
    word_normal += "-" * (len(secret_word) - 2)  # Agrega guiones para las letras ocultas
    word_normal += secret_word[-1]
    
    print(word_normal)

while max_fails > 0:

    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    #Se evita que se de por acierto un ingreso vacío
    if len(letter) == 0:
        print("Error.No has ingresado ninguna letra")
        max_fails -= 1
        continue

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
       print("Ya has intentado con esa letra. Intenta con otra.")
       continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        max_fails -= 1
        print("Lo siento, la letra no está en la palabra.")
 
    # Mostrar la palabra parcialmente adivinada para nivel fácil
    if nivel==1:
       word_displayed = ""
       for char in secret_word:
          if char in guessed_letters or char in "aeiou":
              word_displayed += char
          else:
              word_displayed += "-"

    # Mostrar la palabra parcialmente adivinada para nivel medio
    elif nivel == 2:
       new_word = ""
       first_char = secret_word[0]
       last_char = secret_word[-1]
       for char in secret_word[1:-1]:
          if char in guessed_letters:
              new_word += char
          else:
             new_word += "-"
       word_displayed = first_char + new_word + last_char
    
    print(f"Palabra: {word_displayed}")
 
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
  print(f"¡Oh no! Has agotado tus {max_fails} fallos disponibles.")
  print(f"La palabra secreta era: {secret_word}")