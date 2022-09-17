from tkinter import *
from tkinter import filedialog

from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
# Generate 1024-bit RSA key pair (private + public key)
keyPair = RSA.generate(bits=1024)
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")
# Sign the message using the PKCS#1 v1.5 signature scheme (RSASP1)
#msg = b'A message for signing'

def opena():
    text_file= filedialog.askopenfilename(initialdir="C:/Users/jayanth/Desktop/srp2/",title="Open Text File")
    with open("C:/Users/jayanth/Desktop/srp2/main.txt", 'rb') as msg:
        msg=msg.read()
        my_text.insert(END,msg)
def signa():
    with open("C:/Users/jayanth/Desktop/srp2/main.txt", 'rb') as msg:
        msg=msg.read()
        
        msg=msg.strip()
        hash = SHA256.new(msg)
        signer = PKCS115_SigScheme(keyPair)
        signature = signer.sign(hash)
        
        return signature
        #print("Signature:", binascii.hexlify(signature))
# Verify valid PKCS#1 v1.5 signature (RSAVP1)

signature=signa()
def verifya():
    
    msg1 = my_text.get(1.0, "end-1c")
    with open("C:/Users/jayanth/Desktop/srp2/verify.txt", 'w') as msg:
        msg.write(msg1)
    with open("C:/Users/jayanth/Desktop/srp2/verify.txt", 'rb') as msg2:
        msg2=msg2.read()
        msg2=msg2.strip()
        hash = SHA256.new(msg2)
        signer = PKCS115_SigScheme(keyPair)
        signature2= signer.sign(hash)
        if signature==signature2:
            
            #print(signer.verify(hash, signature))
            lbl.config(text = "Signature is valid.")
        else:
            lbl.config(text = "Signature is invalid.")
        
root=Tk()
root.title("SRP_2")
root.geometry("500x500")
my_text = Text(root,width=40,height=10,font=("Helvetica",16))
my_text.pack(pady=20)
open_button = Button(root,text="Open Text File",command=opena)
open_button.pack(pady=20)
lbl = Label(root, text = "")
lbl.pack()
verify_button = Button(root,text="verify",command=verifya)

verify_button.pack(pady=20)
root.mainloop()