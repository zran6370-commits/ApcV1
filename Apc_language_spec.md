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
const PI = 3.14;
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
  $daftar_angka = [1, 2, 3, 4, 5];
  let nama_nama = ["Alice", "Bob", "Charlie"];
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

Mendukung operator aritmatika (`+`, `-`, `*`, `/`, `%`), perbandingan (`==`, `!=`, `<`, `>`, `<=`, `>=`), dan logika (`&&`, `||`, `!`).

### 3.5. Struktur Kontrol

- **If-Else If-Else**:
  ```apc
  if ($usia > 18) {
    echo "Dewasa";
  } else if ($usia > 12) {
    echo "Remaja";
  } else {
    echo "Anak-anak";
  }
  ```
- **For Loop**:
  ```apc
  for ($i = 0; $i < 5; $i++) {
    echo $i;
  }
  
  for $item in $daftar_angka {
    echo $item;
  }
  ```
- **While Loop**:
  ```apc
  $hitung = 0;
  while ($hitung < 3) {
    echo $hitung;
    $hitung++;
  }
  ```

### 3.6. Fungsi

Fungsi dideklarasikan menggunakan kata kunci `func` (seperti JavaScript).

```apc
func sapa($nama) {
  return "Halo, " . $nama . "!";
}

echo sapa("Apc");
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
  $konfigurasi = json_parse('{"debug": true, "port": 8080}');
  echo $konfigurasi.debug;
  ```

## 5. Contoh Program Sederhana

```apc
# Program Apc pertama saya

$nama_pengguna = "Pengguna Apc";
let waktu_sekarang = new Date(); # Asumsi ada objek Date bawaan

func tampilkan_salam($nama) {
  if ($nama == "") {
    return "Halo, tamu!";
  } else {
    return `Selamat datang, ${$nama}!`;
  }
}

$pesan_salam = tampilkan_salam($nama_pengguna);

echo $pesan_salam;
echo "Waktu saat ini: " . waktu_sekarang.toLocaleString();

$data_produk = [
  {
    "id": 1,
    "nama": "Buku",
    "harga": 50000
  },
  {
    "id": 2,
    "nama": "Pulpen",
    "harga": 5000
  }
];

for $produk in $data_produk {
  echo `Produk: ${$produk.nama}, Harga: Rp ${$produk.harga}`;
}
```

## 6. Referensi

[1] Python Documentation: [https://docs.python.org/](https://docs.python.org/)
[2] PHP Documentation: [https://www.php.net/docs.php](https://www.php.net/docs.php)
[3] JavaScript (MDN Web Docs): [https://developer.mozilla.org/en-US/docs/Web/JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[4] JSON (json.org): [https://www.json.org/json-en.html](https://www.json.org/json-en.html)
