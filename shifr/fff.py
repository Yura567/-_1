alphabet = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
message = input('Введіть рядок: ').lower()
key = int(input('Введіть ключ: '))
encrypted = ''
for letter in message:
    if letter in alphabet:
        t = alphabet.find(letter)
        new_key = (t + key) % len(alphabet)
        encrypted += alphabet[new_key]
    else:
        encrypted += letter
print('Ваш результат:', encrypted)