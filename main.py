# ! /usr/bin/python3
from sys import exit as sysExit
import sys
import os.path
import time

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtWidgets import QStackedWidget, QFileDialog

class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("main.ui", self)
        self.is_keyfile = True
        self.is_encrypt = True
        self.filename = ""
        self.keytext_filename = ""
        self.extension = "txt"
        self.key_extension = "pub"
        self.c_hex = None
        self.arr_pb = None
        self.keytext = None
        self.input_p.setValidator(QIntValidator())
        self.input_q.setValidator(QIntValidator())
        self.jenis_file.setChecked(True)
        self.metode_encrypt.setChecked(True)
        self.input_key.setPlaceholderText("Masukkan kunci")
        self.input.setPlaceholderText("Pilih file pesan")
        self.save_filename.setPlaceholderText("Masukkan nama file")
        self.button.clicked.connect(self.generate)
        self.jenis_file.clicked.connect(self.change_jenis_key)
        self.jenis_ketik.clicked.connect(self.change_jenis_key)
        self.metode_encrypt.clicked.connect(self.change_method)
        self.metode_decrypt.clicked.connect(self.change_method)
        self.save_button.clicked.connect(self.save_file)
        self.browse_button.clicked.connect(self.browse_file)

        # self.input_p = "11"
        # self.input_q = "11"
        # self.input_p.textChanged.connect(self.is_prime(self.input_p))
        # self.input_q.textChanged.connect(self.is_prime(self.input_q))

        # input_validator = self.is_prime(self.input_q)
        # self.input_q.setValidator(input_validator)

    def change_jenis_key(self):
        if(self.jenis_ketik.isChecked()):
            self.is_keyfile = False
            self.save_name = ""
            self.filename = ""
            self.extension = "txt"
        else:
            self.is_keyfile = True
        self.alert.setText("")
        self.alert.setStyleSheet("color: black;")
    
    def change_method(self):
        if(self.metode_encrypt.isChecked()):
            self.is_encrypt = True
            self.key.setText("Public Key")
            self.judul_input.setText("Plainteks")
            self.judul_output.setText("Cipherteks")
            self.button.setText("Encrypt")
        else:
            self.is_encrypt = False
            self.key.setText("Private Key")
            self.judul_input.setText("Cipherteks")
            self.judul_output.setText("Plainteks")
            self.button.setText("Decrypt")
        self.input.setText("")
        self.output.setText("")
        self.alert.setText("")
        self.alert.setStyleSheet("color: black;")
        self.c_hex = None
        self.arr_pb = None
        self.browse_filename.setText("")
        
    def generate(self):
        if self.jenis_file.isChecked():
            self.is_keyfile = True
        else:
            self.is_keyfile = False
            self.input_text = self.input_key.toPlainText()
        
        if self.metode_encrypt.isChecked():
            self.is_encrypt = True
            if(self.is_keyfile and (self.keytext_filename == "")):
                self.key_filename.setText("Upload file dulu!")
            else:
                if(self.filename == ""):
                    self.browse_filename.setText("Upload file dulu!")
                else:
                    self.encrypt()
        else:
            self.is_encrypt = False
            if(self.is_keyfile and (self.keytext_filename == "")):
                self.key_filename.setText("Upload file dulu!")
            else:
                if(self.filename == ""):
                    self.browse_filename.setText("Upload file dulu!")
                else:
                    self.decrypt()
    
    def browse_keyfile(self):
        file = QFileDialog.getOpenFileName(self)
        self.keytext_filename = file[0]
        self.key_filename.setText(self.keytext_filename)
        self.key_extension = os.path.splitext(file[0])[1][1:]
        self.alert.setText("")
        self.alert.setStyleSheet("color: black;")

        f = open(self.keytext_filename,"rb")
        key_text = f.read()
        f.close()
        self.input_key.setText(key_text)
    
    def browse_file(self):
        file = QFileDialog.getOpenFileName(self)
        self.filename = file[0]
        self.browse_filename.setText(self.filename)
        self.extension = os.path.splitext(file[0])[1][1:]
        self.alert.setText("")
        self.alert.setStyleSheet("color: black;")
        
        arr = []
        if(self.is_encrypt):
            f = open(self.filename,"rb")
            file_bytes = f.read()
            f.close()

            for byte in file_bytes:
                arr.append(chr(byte))
            self.input.setText(''.join(arr))
        else:
            f = open(self.filename, "r")
            c_hex = f.read()
            arr_cb = c_hex.split(" ")
            f.close()
            self.input.setText(' '.join(arr_cb))
            

    def save_file(self):
        self.save_name = self.save_filename.text()
        if(self.is_encrypt):
            if(self.c_hex is None):
                self.alert.setText("Enkripsi dulu!")
                self.alert.setStyleSheet("color: red;")
            else:
                w=open(self.save_name + "." + self.extension, "wb")
                w.write(self.c_hex)
                w.close()
                self.alert.setText("File berhasil disimpan!")
                self.alert.setStyleSheet("color: black;")
        else:
            if(self.arr_pb is None):
                self.alert.setText("Dekripsi dulu!")
                self.alert.setStyleSheet("color: red;")
            else:
                w=open(self.save_name + "." + self.extension, "wb")
                w.write(self.arr_pb)
                self.alert.setText("File berhasil disimpan!")
                self.alert.setStyleSheet("color: black;")

    def generate_private_key(self):
        k = 1
        d = 0.1
        totient = (self.input_p-1) * (self.input_q-1)
        while(d%1 != 0):
            d = (1 + k * totient)/self.input_key
            k += 1
        d = int(d)
        self.private_key = d

    def save_keyfile(self):
        if(self.keytext is None):
                self.alert.setText("Upload file key dulu!")
                self.alert.setStyleSheet("color: red;")
        else:
            if(self.is_encrypt):
                w=open("publickey" + "." + "pub", "w")
                w.write(self.public_key)
                w.close()
                
            w=open("privatekey" + "." + "pri", "w")
            w.write(self.private_key)
            w.close()

            self.alert.setText("File key berhasil disimpan!")
            self.alert.setStyleSheet("color: black;")

    def encrypt(self):
        f = open(self.filename,"rb")
        file_bytes = f.read()
        f.close()

        n = self.input_p * self.input_q
        self.c_hex = ""
        i = 0
        for byte in file_bytes:
            self.c_hex += self.DecToHex(byte**self.public_key % n)
            if i < len(file_bytes)-1:
                self.c_hex += " "
            i += 1
        
    def is_prime(self, type):
        if(type=="p"):
            a = self.input_p.text()
        else:
            a = self.input_q.text()
        a_prime = True
        # if (not a.isinstance()):
        #     a_prime = False
        a = int(a)
        if(a > 1):
            i = 2
            while(a_prime and i <= a//2):
                if(a % i == 0):
                    a_prime = False
                i += 1
        else:
            a_prime = False

        if(not a_prime):
            if (type=="p"):
                self.alert.setText("Nilai p tidak prima")
            else:
                self.alert.setText("Nilai q tidak prima")
            self.alert.setStyleSheet("color: red;")

    def fpb(self, a, b):
        if(b == 0):
            return a
        else:
            return self.fpb(b, a % b)
        
    def DecToHex(self, x):
        i = 0
        while ((x // 16**i) != 0):
            i += 1
            
        ArrSize = i
        temp1 = x
        temp2 = x
        Arr = [" " for i in range(ArrSize)]
        
        for i in range(ArrSize-1,-1,-1):
            temp1 = temp1 // 16
            sisa = temp2 % 16
            temp2 = temp1
            if (sisa == 0):
                Arr[i] = "0"
            elif (sisa == 1):
                Arr[i] = "1"
            elif (sisa == 2):
                Arr[i] = "2"
            elif (sisa == 3):
                Arr[i] = "3"
            elif (sisa == 4):
                Arr[i] = "4"
            elif (sisa == 5):
                Arr[i] = "5"
            elif (sisa == 6):
                Arr[i] = "6"
            elif (sisa == 7):
                Arr[i] = "7"
            elif (sisa == 8):
                Arr[i] = "8"
            elif (sisa == 9):
                Arr[i] = "9"
            elif (sisa == 10):
                Arr[i] = 'a'
            elif (sisa == 11):
                Arr[i] = 'b'
            elif (sisa == 12):
                Arr[i] = 'c'
            elif (sisa == 13):
                Arr[i] = 'd'
            elif (sisa == 14):
                Arr[i] = 'e'
            elif (sisa == 15):
                Arr[i] = 'f'

        return "".join(Arr)

    def HexToDec(self, x):
        sum = 0
        for i in range(len(x)):
            if (x[i] == '0'):
                sum = sum + (0 * (16**(len(x)-1-i)))
            elif (x[i] == '1'):
                sum = sum + (1 * (16**(len(x)-1-i)))
            elif (x[i] == '2'):
                sum = sum + (2 * (16**(len(x)-1-i)))
            elif (x[i] == '3'):
                sum = sum + (3 * (16**(len(x)-1-i)))
            elif (x[i] == '4'):
                sum = sum + (4 * (16**(len(x)-1-i)))
            elif (x[i] == '5'):
                sum = sum + (5 * (16**(len(x)-1-i)))
            elif (x[i] == '6'):
                sum = sum + (6 * (16**(len(x)-1-i)))
            elif (x[i] == '7'):
                sum = sum + (7 * (16**(len(x)-1-i)))
            elif (x[i] == '8'):
                sum = sum + (8 * (16**(len(x)-1-i)))
            elif (x[i] == '9'):
                sum = sum + (9 * (16**(len(x)-1-i)))
            elif (x[i] == 'A') or (x[i] == 'a'):
                sum = sum + (10 * (16**(len(x)-1-i)))
            elif (x[i] == 'B') or (x[i] == 'b'):
                sum = sum + (11 * (16**(len(x)-1-i)))
            elif (x[i] == 'C') or (x[i] == 'c'):
                sum = sum + (12 * (16**(len(x)-1-i)))
            elif (x[i] == 'D') or (x[i] == 'd'):
                sum = sum + (13 * (16**(len(x)-1-i)))
            elif (x[i] == 'E') or (x[i] == 'e'):
                sum = sum + (14 * (16**(len(x)-1-i)))
            elif (x[i] == 'F') or (x[i] == 'f'):
                sum = sum + (15 * (16**(len(x)-1-i)))
        
        return (sum)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("RSA Encrypt-Decrypt")

    main = MainScreen()
    
    widget = QStackedWidget()
    widget.addWidget(main)
    widget.setMinimumHeight(701)
    widget.setMinimumWidth(480)

    widget.show()
    
    sys.exit(app.exec_())