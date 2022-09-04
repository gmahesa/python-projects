# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 15:30:11 2019

@author: galang_mahesa
"""

buku = [
    {'judul': 'F.U. Money', 'harga' : 400000, 'pengarang': 'Lu'},
    {'judul': 'Nat Geo', 'harga' : 450000, 'pengarang': 'will iam'},
    {'judul': 'Nat People', 'harga' : 300000, 'pengarang': 'budi'},
    {'judul': 'Doraemon', 'harga' : 470000, 'pengarang': 'amin'},
    {'judul': 'Joker', 'harga' : 480000, 'pengarang': 'Tak tau'},
    {'judul': 'Batman', 'harga' : 250000, 'pengarang': 'Meme'},
    {'judul': 'Jawaban UN 2020', 'harga' : 350000, 'pengarang': 'Pencury'},
]

print(buku)
print("--------------------------------------")

def cari(buku, subsring):
    return buku ['judul'] in substring['judul']\
    and buku ['harga'] in substring['harga']\
    and buku ['pengarang'] in substring['pengarang']

def tampil(key,value):
    if value == True:
        print(key,value)
        
substring = {'judul': 'Jawaban UN 2020','harga':list(range(200000,410000)), 'pengarang': 'Pencury'}
x = list(map(cari,buku, [substring]*len(buku)))

list(map(tampil,buku,x));