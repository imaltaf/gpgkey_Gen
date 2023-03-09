import gnupg

gpg = gnupg.GPG()

name = input('provide you name - ')

key = gpg.generate_key(

    key_type="RSA",

    key_length=2048,

    name_real="John Doe",

    name_email="john.doe@example.com",

    passphrase="my passphrase"

)

key_data = gpg.export_keys(key.fingerprint)

print(key_data)

