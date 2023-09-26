# -*- coding: utf-8 -*-
"""Prak2E1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XcaoN-vHsmUewwCu4qO76nyfrdoqT-7L
"""

print('@   @ @@@@ @@@@ @ @@@ @@@@')
print('@ @ @ @  @ @  @ @ @   @  @')
print('@   @ @  @ @  @ @ @   @@@@')
print('@   @ @@@@ @  @ @ @@@ @  @')

import math

def hitung_a(b, c):
    return math.sqrt(c*2 - b*2)

def hitung_b(a, c):
    return math.sqrt(c*2 - a*2)

def hitung_c(a, b):
    return math.sqrt(a*2 + b*2)

def main():
    print("Menghitung Pytagoras")
    print("a.) menghitung sisi a")
    print("b.) menghitung sisi b")
    print("c.) menghitung sisi c")

    opsi = str(input("masukan opsi : "))

    #menghitung sisi a
    if opsi == "a":
        b = float(input("Masukan sisi b : "))
        c = float(input("Masukan sisi c : "))
        while c < b:
            print("Nilai c harus lebih besar atau sama dengan nilai b.")
            c = float(input("Masukkan nilai sisi c: "))
        sisi_a = hitung_a(b, c)
        print(f"Sisi a = {sisi_a}")
    #mengitung sisi b
    elif opsi == "b":
        a = float(input("masukan sisi a : "))
        c = float(input("masukan sisi c : "))
        while c < a:
            print("Nilai c harus lebih besar atau sama dengan nilai a.")
            c = float(input("Masukkan nilai sisi c: "))
        sisi_b = hitung_b(a, c)
        print(f"Sisi b = {sisi_b}")
    #menghitung sisi c
    elif opsi == "c":
        a = float(input("masukan sisi a : "))
        b = float(input("masukan sisi b : "))
        sisi_c =  hitung_c(a, b)
        print("sisi c = ", sisi_c)
    else:
        print("opsi tidak valid.")

if __name__ == "__main__":
    main()

print('@   @ @@@@ @@@@ @ @@@ @@@@')
print('@ @ @ @  @ @  @ @ @   @  @')
print('@   @ @  @ @  @ @ @   @@@@')
print('@   @ @@@@ @  @ @ @@@ @  @')

import math

def hitung_a(b, c):
    return math.sqrt(c*2 - b*2)

def hitung_b(a, c):
    return math.sqrt(c*2 - a*2)

def hitung_c(a, b):
    return math.sqrt(a*2 + b*2)

def main():
    print("Menghitung Pytagoras")
    print("a.) menghitung sisi a")
    print("b.) menghitung sisi b")
    print("c.) menghitung sisi c")

    opsi = str(input("masukan opsi : "))

    #menghitung sisi a
    if opsi == "a":
        b = float(input("Masukan sisi b : "))
        c = float(input("Masukan sisi c : "))
        while c < b:
            print("Nilai c harus lebih besar atau sama dengan nilai b.")
            c = float(input("Masukkan nilai sisi c: "))
        sisi_a = hitung_a(b, c)
        print(f"Sisi a = {sisi_a}")
    #mengitung sisi b
    elif opsi == "b":
        a = float(input("masukan sisi a : "))
        c = float(input("masukan sisi c : "))
        while c < a:
            print("Nilai c harus lebih besar atau sama dengan nilai a.")
            c = float(input("Masukkan nilai sisi c: "))
        sisi_b = hitung_b(a, c)
        print(f"Sisi b = {sisi_b}")
    #menghitung sisi c
    elif opsi == "c":
        a = float(input("masukan sisi a : "))
        b = float(input("masukan sisi b : "))
        sisi_c =  hitung_c(a, b)
        print("sisi c = ", sisi_c)
    else:
        print("opsi tidak valid.")

if __name__ == "__main__":
    main()

print('@   @ @@@@ @@@@ @ @@@ @@@@')
print('@ @ @ @  @ @  @ @ @   @  @')
print('@   @ @  @ @  @ @ @   @@@@')
print('@   @ @@@@ @  @ @ @@@ @  @')

print("\n \n")


angkaPertama = int(input("masukan angka pertama : "))
angkaKedua = int(input("masukan angka kedua : "))
angkaKetiga = int(input("masukan angka ketiga : "))

hasil = max(angkaPertama, angkaKedua, angkaKetiga)
print("angka terbesar adalah ", hasil)