# Penjelasan Tentang password generator
This is a Python script that generates passwords based on specified criteria. It uses the *argparse* module to handle command line arguments, and *secrets* and *random* modules to generate random password strings.

## How to use
- Contoh Pertama: 
```bash
python.exe password-generator.py -n 2 -l 3 -u 1 -s 1 -t 10 -a 2 -o passwords.txt
```
- Contoh Kedua: 
```bash
python.exe .\password-generator.py -n 3 -l 2 -u 4 -s 5 -t 12 -a 4 -o hasil-passwordku.txt
```

agparse untuk menunjukan tata cara penggunaan program ini di terminal

## Perbedaan git dan github
git adalah alat yang digunakan unutk menegelola perubahan kode sumber kita, 
github adalah platform di mana repositori Git dapat di-host dan kolaborasi dengan orang lain bisa dilakukan

## Tutorial Git

- Sebelum kita tracking :

  1. ```$ git init ```
  2. ```$ git add . ```
  3. ```$ git commit -m "catatan kamu" ```

- Setelah kita Modified : 

  0. ini untuk lihat status yg sudah dirubah  ```$ git status```
  1. ```$ git add . ```
  2. ```$ git commit -m "catatan setelah dirubah" ```