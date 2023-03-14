def julescesar(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_decale = ''
    for lettre in message:
        if lettre in alphabet:
            lettre_decalee = alphabet[(alphabet.index(lettre) + decalage) % 26]
            message_decale += lettre_decalee
        else:
            message_decale += lettre
    return message_decale

message = input ("Ecrivez votre message: ")
decalage = 3
message_decale = julescesar(message, decalage)
print(message_decale)
