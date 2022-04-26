from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from os import path , makedirs
from pathlib import Path
import sys

import exeptions

def encrypyFile(filePath, outputFilename, key):
    # Defines working directory
    DIR = path.abspath(str(Path(sys.argv[0]).parent.resolve()))

    # create "file directory if dont´t exist
    if not path.exists(DIR + "\\files\\"):
        makedirs(DIR + "\\files\\")

    # creates key model
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b"salt", iterations=100000)
    extension = Path(filePath).suffix.encode() # encodes file extensions
    
    # creates fernet with key
    key = key.encode()
    f = Fernet(urlsafe_b64encode(kdf.derive(key)))

    # file to encrypt does not exist
    if not path.exists(path.abspath(filePath)):
        raise exeptions.fileDoesNotExist

    # check if is file
    if not path.isfile(filePath):
        raise exeptions.isNotFile

    # read file to encrypt
    FileToCrypt = open(path.abspath(filePath), 'rb')
    FileString = FileToCrypt.read()
    FileToCrypt.close()

    # writes a ".txt" file with encrypted data and encrypted extension
    EncriptRecord = open(DIR + "\\files\\" + outputFilename + ".txt", 'wb+')
    EncriptRecord.write(f.encrypt(FileString) + '\n'.encode() + f.encrypt(extension))
    EncriptRecord.close()

    return key.decode()

def decryptFile(filePath, outputfilename, key):
    # Defines working directory
    DIR = path.abspath(str(Path(sys.argv[0]).parent.resolve()))

    # create "file directory if dont´t exist
    if not path.exists(DIR + "\\files\\"):
        makedirs(DIR + "\\files\\")

    # creates a key model with same salt
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b"salt", iterations=100000)
    f = Fernet(urlsafe_b64encode(kdf.derive(key.encode())))

    if not path.exists(path.abspath(filePath)):
        raise exeptions.fileDoesNotExist

    # check if is file
    if not path.isfile(filePath):
        raise exeptions.isNotFile

    # read file to decrypt
    EncriptRecord = open(filePath, 'rb')
    EncriptedFileString = EncriptRecord.read()
    EncriptRecord.close()
    EncriptedFileData = EncriptedFileString.split("\n".encode())

    # decrypt data, if launch INVALID_key exeption, ends
    try:
        DecryptedData = f.decrypt(EncriptedFileData[0])
    except:
        raise exeptions.invalidKey

    # write decryted data with extension
    FileToDecrypt = open(path.abspath(DIR + '\\files\\' + outputfilename + f.decrypt(EncriptedFileData[1]).decode()), 'wb+')
    FileToDecrypt.write(DecryptedData)
    FileToDecrypt.close()
    
    return 1