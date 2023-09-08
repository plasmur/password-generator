from argparse import ArgumentParser
import secrets
import random
import string

# Persiapan Argument Parser
parser = ArgumentParser(
    prog="Password Generator",
    description="MenghasiIkan password dengan menggunakan alat ini.",
)

# Menambahkan argumen ke dalam parser
parser.add_argument(
    "-n", "--angka", default=0, help="Jumlah digit dalam password", type=int
)

parser.add_argument(
    "-l", "--huruf-kecil", default=0, help="Jumlah huruf kecil dalam password", type=int
)
parser.add_argument(
    "-u", "--huruf-besar", default=0, help="Jumlah huruf besar dalam password", type=int
)
parser.add_argument(
    "-s",
    "--karakter-khusus",
    default=0,
    help="Jumlah karakter khusus dalam password",
    type=int,
)

# Menambahkan argumen total panjang password
parser.add_argument(
    "-t",
    "--total-panjang",
    default=0,
    help="panjang total password. Jika diisi, akan mengabaikan -n, -i, -u, dan -s, "
    "serta menghasilkan password yang benar-benar acak dengan panjang yang ditentukan",
    type=int,
)

# Jumlah password harus berupa bilangan, jadi kita periksa apakah bertipe int.
parser.add_argument("-a", "--jumlah", default=1, type=int)
parser.add_argument("-o", "--file-output")
parser.add_argument(
    "-c" "--contoh pengunaannya",
    help="--python.exe .\password-generator.py -n 3 -l 2 -u 4 -s 5 -t 12 -a 4 -o hasil-passwordku.txt",
)

# Parsing argumen dari baris perintah.
args = parser.parse_args()

# variabel untuk simpan daftar password
passwords = []

# melakukan perulangan sebanayk jumlah password.
for _ in range(args.jumlah):
    if args.total_panjang:
        # menghasilkan password acak dengan panjang total_panjang
        passwords.append(
            "".join(
                [
                    secrets.choice(
                        string.digits + string.ascii_letters + string.punctuation
                    )
                    for _ in range(args.total_panjang)
                ]
            )
        )

    else:
        password = []
        # jika /berapa angka yang harus dimasukan dalam password
        for _ in range(args.angka):
            password.append(secrets.choice(string.digits))

        # jika / beberapa banyak huruf besar yang harus dimasukan dalam password
        for _ in range(args.huruf_besar):
            password.append(secrets.choice(string.ascii_uppercase))

        # jika / beberapa banyak huruf kecil yang harus dimasukan dalam password
        for _ in range(args.huruf_kecil):
            password.append(secrets.choice(string.ascii_lowercase))

        # jika / beberapa banyak karakter khusus yang harus dimasukan dalam password
        for _ in range(args.karakter_khusus):
            password.append(secrets.choice(string.punctuation))

        # mengacak daftar berisi semua huruf, angka, dan simbol yang mungkin.
        random.shuffle(password)

        # mengambil huruf huruf pada string hingga mencapai panjang argument dan menggabungkannya
        password = "".join(password)

        # menambahkan password ini ke daftar password keseluruhan.
        password.append(password)

# menyimpan password ke file .txt
if args.file_output:
    with open(args.file_output, "w") as f:
        f.write("\n".join(passwords))

# menampilkan password di layar
print("\n".join(passwords))
