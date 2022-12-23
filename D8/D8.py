#caesar cipher

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']    
def caeser(text,shift,direction):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if(direction == 'encode'):
                new_position = position + shift
            elif(direction == 'decode'):
                new_position = position - shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
            
    print(f'the {direction}d text is {cipher_text}')
should_start = True
while (should_start):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt :\n").lower()
    text = input('type your msg :\n').lower()
    shift = int(input('type the shift no :\n'))
    if(shift > 26):
        shift %= 26
    caeser(text,shift,direction)  
    should_continue = input('do you wanna continue? (yes/no)')
    if (should_continue == 'no'):
        should_start = False