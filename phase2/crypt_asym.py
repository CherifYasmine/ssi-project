# import rsa
# import elgamal
#
# publicKeyRsa, privateKeyRsa = rsa.newkeys(512)
# elgamal_keys = elgamal.generate_keys(128)
# publicKeyElGamal = elgamal_keys["publicKey"]
# privateKeyElGamal = elgamal_keys["privateKey"]
#
# def encrypt_rsa():
#     message = input("entrer le message à chiffrer RSA : ")
#     crypted_message: bytes = rsa.encrypt(message.encode(), publicKeyRsa)
#     print (crypted_message.hex())
#
# def decrypt_rsa():
#     message = input("entrer le message à déchiffrer RSA : ")
#     decrypted_message: bytes = rsa.decrypt(bytes.fromhex(message), privateKeyRsa)
#     print(decrypted_message.decode("utf-8").strip())
#
# def encrypt_elgamal():
#     message = input("entrer le message à chiffrer elgamal : ")
#     crypted_message = elgamal.encrypt(publicKeyElGamal, message)
#     print (crypted_message)
#
# def decrypt_elgamal():
#     message = input("entrer le message à déchiffrer elgamal : ")
#     decrypted_message = elgamal.decrypt(key=privateKeyElGamal, cipher=message)
#     print(decrypted_message)