# Spesifikasi Bahasa Apc

## 1. Pendahuluan

Apc adalah bahasa pemrograman baru yang dirancang untuk menggabungkan kemudahan penggunaan Python, fleksibilitas web PHP, struktur data JSON, dan reaktivitas JavaScript. Tujuan utama Apc adalah menyediakan bahasa yang serbaguna untuk pengembangan web, skrip, dan aplikasi data.

## 2. Filosofi Desain

- **Sintaksis Intuitif**: Mengadopsi sintaksis yang bersih dan mudah dibaca dari Python.
- **Dinamis dan Fleksibel**: Mendukung tipe data dinamis dan struktur yang fleksibel seperti JavaScript dan PHP.
- **Integrasi Data**: Memiliki dukungan bawaan untuk struktur data bergaya JSON.
- **Berorientasi Web**: Dirancang dengan mempertimbangkan pengembangan web.

## 3. Sintaksis Dasar

### 3.1. Komentar

Komentar baris tunggal dimulai dengan `#` (seperti Python dan PHP) atau `//` (seperti JavaScript).
Komentar multi-baris diapit oleh `/*` dan `*/` (seperti JavaScript dan PHP).

```apc
# Ini adalah komentar satu baris
// Ini juga komentar satu baris
/*
Ini adalah
komentar multi-baris
*/
```

### 3.2. Variabel

Variabel dideklarasikan tanpa tipe data eksplisit dan diawali dengan `$` (seperti PHP) atau `let`/`const` (seperti JavaScript).

```apc
$nama = "Dunia";
let usia = 30;
const PI = 3.14; # const belum diimplementasikan, tapi untuk tujuan dokumentasi
```

### 3.3. Tipe Data

- **String**: Diapit oleh kutip tunggal atau ganda.
  ```apc
  $pesan = "Halo, Apc!";
  let kata = 'Selamat datang';
  ```
- **Number**: Integer dan float.
  ```apc
  $jumlah = 100;
  let harga = 99.99;
  ```
- **Boolean**: `true` atau `false`.
  ```apc
  $aktif = true;
  let selesai = false;
  ```
- **Array/List**: Koleksi terindeks (seperti Python list atau JavaScript array).
  ```apc
  $daftar_angka = [1, 2, 3, 4, 5]; # Belum sepenuhnya didukung di interpreter dasar
  let nama_nama = ["Alice", "Bob", "Charlie"]; # Belum sepenuhnya didukung di interpreter dasar
  ```
- **Object/Dictionary/Map**: Koleksi pasangan kunci-nilai (seperti JavaScript object, Python dictionary, atau JSON object).
  ```apc
  $pengguna = {
    "nama": "Budi",
    "usia": 25,
    "kota": "Jakarta"
  };
  let produk = {
    id: 101,
    nama: "Laptop",
    harga: 1200.00
  };
  ```
- **Null**: `null`.
  ```apc
  $data_kosong = null;
  ```

### 3.4. Operator

Mendukung operator aritmatika (`+`, `-`, `*`, `/`, `%`), perbandingan (`==`, `!=`, `<`, `>`, `<=`, `>=`), dan logika (`&&`, `||`, `!`). (Implementasi dasar saat ini hanya mendukung `+` untuk string dan angka).

### 3.5. Struktur Kontrol

- **If-Else If-Else**:
  ```apc
  if ($usia > 18) { # Belum sepenuhnya didukung di interpreter dasar
    echo "Dewasa";
  } else if ($usia > 12) {
    echo "Remaja";
  } else {
    echo "Anak-anak";
  }
  ```
- **For Loop**:
  ```apc
  for ($i = 0; $i < 5; $i++) { # Belum sepenuhnya didukung di interpreter dasar
    echo $i;
  }
  
  for $item in $daftar_angka { # Belum sepenuhnya didukung di interpreter dasar
    echo $item;
  }
  ```
- **While Loop**:
  ```apc
  $hitung = 0;
  while ($hitung < 3) { # Belum sepenuhnya didukung di interpreter dasar
    echo $hitung;
    $hitung++;
  }
  ```

### 3.6. Fungsi

Fungsi dideklarasikan menggunakan kata kunci `func` (seperti JavaScript). (Deklarasi fungsi belum sepenuhnya didukung, tetapi pemanggilan fungsi bawaan sudah).

```apc
func sapa($nama) {
  return "Halo, " . $nama . "!";
}

# echo sapa("Apc"); # Pemanggilan fungsi kustom belum didukung
```

## 4. Fitur Unik

- **Templating String**: Dukungan untuk interpolasi string yang kuat (seperti JavaScript template literals).
  ```apc
  $nama = "Apc";
  $pesan = `Selamat datang, ${$nama}!`;
  echo $pesan;
  ```
- **Integrasi JSON Native**: Objek JSON dapat dibuat dan diakses secara langsung.
  ```apc
  $konfigurasi = json_decode("{\"debug\": true, \"port\": 8080}");
  echo $konfigurasi.debug; # Akses properti objek belum sepenuhnya didukung
  ```

## 5. Fungsi Bawaan (Built-in Functions)

Apc menyediakan beberapa fungsi bawaan untuk mempermudah pengembangan:

| Fungsi         | Deskripsi                                        | Contoh Penggunaan                               |
|----------------|--------------------------------------------------|-------------------------------------------------|
| `print(args...)` | Mencetak argumen ke konsol. Mirip Python.        | `print("Hello");` `print($var, "world");`      |
| `echo(args...)`  | Mencetak argumen ke konsol. Mirip PHP.           | `echo "Hello";` `echo $var, "world";`         |
| `len(string/array)` | Mengembalikan panjang string atau array.         | `len("Apc");` `len($myArray);`                 |
| `str_upper(string)` | Mengubah string menjadi huruf kapital.           | `str_upper("hello");`                          |
| `str_lower(string)` | Mengubah string menjadi huruf kecil.             | `str_lower("WORLD");`                          |
| `math_sqrt(number)` | Mengembalikan akar kuadrat dari sebuah angka.    | `math_sqrt(16);`                                |
| `math_pow(base, exp)` | Mengembalikan hasil pangkat.                     | `math_pow(2, 3);`                               |
| `math_abs(number)` | Mengembalikan nilai absolut dari sebuah angka.   | `math_abs(-5);`                                 |
| `now()`          | Mengembalikan tanggal dan waktu saat ini.        | `now();`                                        |
| `json_encode(data)` | Mengubah data Apc (objek/array) menjadi string JSON. | `json_encode($myObject);`                       |
| `json_decode(string)` | Mengubah string JSON menjadi data Apc.           | `json_decode("{\"key\":\"value\"}");`       |
| `get_env(key)`   | Mengambil nilai variabel lingkungan.              | `get_env("PATH");`                             |
| `exit(code)`     | Menghentikan eksekusi program dengan kode keluar. | `exit(0);`                                      |

## 6. Contoh Program Sederhana

```apc
# Program Apc pertama saya

$nama_pengguna = "Pengguna Apc";
let waktu_sekarang = now();

# func tampilkan_salam($nama) { # Deklarasi fungsi kustom belum didukung
#   if ($nama == "") {
#     return "Halo, tamu!";
#   } else {
#     return `Selamat datang, ${$nama}!`;
#   }
# }

# $pesan_salam = tampilkan_salam($nama_pengguna); # Pemanggilan fungsi kustom belum didukung

echo `Selamat datang, ${$nama_pengguna}!`;
echo "Waktu saat ini: " . waktu_sekarang;

$data_produk = {
  "produk1": {"id": 1, "nama": "Buku", "harga": 50000},
  "produk2": {"id": 2, "nama": "Pulpen", "harga": 5000}
};

# for $produk in $data_produk { # Loop belum sepenuhnya didukung
#   echo `Produk: ${$produk.nama}, Harga: Rp ${$produk.harga}`;
# }

$json_string = json_encode($data_produk);
echo `Data produk dalam JSON: ${$json_string}`;

$platform_os = get_env("PLATFORM");
echo `Sistem Operasi: ${$platform_os}`;

$random_num = math_pow(2, 4);
echo `2 pangkat 4 adalah: ${$random_num}`;
```

## 7. Referensi

[1] Python Documentation: [https://docs.python.org/](https://docs.python.org/)
[2] PHP Documentation: [https://www.php.net/docs.php](https://www.php.net/docs.php)
[3] JavaScript (MDN Web Docs): [https://developer.mozilla.org/en-US/docs/Web/JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[4] JSON (json.org): [https://www.json.org/json-en.html](https://www.json.org/json-en.html)
