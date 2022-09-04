# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:47:09 2019

@author: G_MAHESA99
"""

def cari(buku, entry):
    
    key = ('judul', 'harga', 'pengarang', 'kutipan')
    filtered = [i for i in buku if any(str(i[index]) == entry for index in key)]
    
    def tampil():
        print(filtered)
    return tampil

buku = [
    {'judul': 'F.U. Money', 'harga' : 400000, 'pengarang': 'Lu', 'kutipan' : 'The hell man'},
    {'judul': 'Nat Geo', 'harga' : 400000, 'pengarang': 'will iam', 'kutipan' : 'Ya begitulah'},
    {'judul': 'Nat People', 'harga' : 300000, 'pengarang': 'budi', 'kutipan' : 'contoh kutipan'},
    {'judul': 'Doraemon', 'harga' : 470000, 'pengarang': 'amin', 'kutipan' : 'ya ya ya aku sayang sekali'},
    {'judul': 'Joker', 'harga' : 480000, 'pengarang': 'Tak tau', 'kutipan' : 'Orang baik tersakiti'},
    {'judul': 'Batman', 'harga' : 250000, 'pengarang': 'Meme', 'kutipan' : 'Iam batman'},
    {'judul': 'Jawaban UN 2020', 'harga' : 350000, 'pengarang': 'Pencury', 'kutipan' : 'Dijamin lulus'},
]

entry = input("Input salah satu (atau semua) \nJudul/Harga/Pengarang/Kutipan : ")
fungsiku = cari(buku, entry)
fungsiku()