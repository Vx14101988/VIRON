import pywaves as pw
import bip39
import json

def buatSeedPhrase():
    mnemonic = bip39.generate_mnemonic()
    return mnemonic

def buatAlamatBaru(seed_phrase):
    try:
        new_address = pw.Address(seed=seed_phrase)
        return {
            'Address': new_address.address,
            'Public Key': new_address.publicKey,
            'Private Key': new_address.privateKey,
            'Seed': seed_phrase
        }
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None

file_name = 'wallet.json'
seed_phrase = buatSeedPhrase()
print("Seed Phrase:", seed_phrase)

Alamatinfo = buatAlamatBaru(seed_phrase)
if Alamatinfo:
    print("New Address Created:")
    print("Address:", Alamatinfo['Address'])
    print("Public Key:", Alamatinfo['Public Key'])
    print("Private Key:", Alamatinfo['Private Key'])
    print("Seed:", Alamatinfo['Seed'])

    data = {
        'id_asset': 'id_asset_sudah_ditentukan',
        'Address': Alamatinfo['Address'],
        'Public Key': Alamatinfo['Public Key'],
        'Private Key': Alamatinfo['Private Key'],
        'Seed': Alamatinfo['Seed']
    }

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

    print("Data telah disimpan ke file wallet.json")
