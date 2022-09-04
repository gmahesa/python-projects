# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:33:15 2019

@author: galang_mahesa
"""

mahasiswa = [
    {'nama' : 'galang', 'ipk' : 3, 'sem': 2},
    {'nama' : 'aji', 'ipk' : 4, 'sem': 5},
    {'nama' : 'mahesa', 'ipk' : 2, 'sem': 2},
    {'nama' : 'galang aji', 'ipk' : 3, 'sem': 6},
    {'nama' : 'aji mahesa', 'ipk' : 1, 'sem': 7}
]

print(mahasiswa)
print("--------------------------------------")
    
mahasiswa.insert(5, {'nama' : 'galang mahesa', 'ipk' : 3, 'sem': 3})
new = {'nama' : 'galang mahesa', 'ipk' : 3, 'sem': 3}
mahasiswa [4] = new
mahasiswa.append({'nama' : 'galang mahesa', 'ipk' : 3, 'sem': 3})

print(mahasiswa)
print("--------------------------------------")

def cari(mahasiswa, kriteria):
    return mahasiswa ['nama'] in kriteria['nama']\
    and mahasiswa ['ipk'] in kriteria['ipk']\
    and mahasiswa ['sem'] in kriteria['sem']

def tampil(key,value):
    if value == True:
        print(key,value)
        
kriteria = {'nama': 'galang','ipk':list(range(1,5)), 'sem': list(range(2,8))}
x = list(map(cari,mahasiswa, [kriteria]*len(mahasiswa)))

list(map(tampil,mahasiswa,x));