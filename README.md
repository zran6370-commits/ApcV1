# Apc Language

Apc adalah bahasa pemrograman eksperimental yang dirancang untuk menggabungkan fitur-fitur dari Python, PHP, JSON, dan JavaScript. Tujuannya adalah untuk menyediakan bahasa yang serbaguna dan mudah digunakan untuk berbagai aplikasi, mulai dari skrip sederhana hingga pengembangan web.

## Fitur Utama

- **Sintaksis Intuitif**: Mengadopsi sintaksis yang bersih dan mudah dibaca.
- **Tipe Data Dinamis**: Mendukung tipe data dinamis dan struktur fleksibel.
- **Integrasi JSON**: Dukungan bawaan untuk struktur data bergaya JSON.
- **Fungsi Bawaan**: Menyediakan berbagai fungsi bawaan untuk matematika, string, sistem, dan JSON.
- **Portabilitas Lintas Platform**: Dapat dijalankan di Linux, Windows, dan macOS.

## Instalasi

Untuk menjalankan interpreter Apc, Anda hanya perlu Python 3 terinstal di sistem Anda. Kloning repositori ini:

```bash
git clone https://github.com/zran6370-commits/ApcV1.git
cd ApcV1
```

## Penggunaan

### Linux/macOS

Berikan izin eksekusi pada skrip `apc.sh` dan jalankan program Apc:

```bash
chmod +x apc.sh
./apc.sh examples/hello.apc
```

### Windows

Gunakan skrip `apc.bat` untuk menjalankan program Apc:

```cmd
apc.bat examples\hello.apc
```

## Contoh Kode

Berikut adalah beberapa contoh sederhana dari bahasa Apc.

### Hello World

`examples/hello.apc`:

```apc
# Ini adalah program Hello World pertama saya di Apc
echo "Halo, Dunia!";
```

### Variabel dan Interpolasi String

`examples/variables.apc`:

```apc
$nama = "Apc";
let versi = 0.2;

echo `Selamat datang di ${$nama} versi ${versi}!`;
```

### Fungsi Bawaan

`examples/builtins.apc`:

```apc
# Fungsi String
echo str_upper("hello apc");
echo str_lower("HELLO APC");

# Fungsi Matematika
echo math_sqrt(25);
echo math_pow(2, 5);

# Fungsi Sistem
echo `Platform OS: ${get_env("PLATFORM")}`;
echo `Waktu saat ini: ${now()}`;

# Fungsi JSON
$data_obj = {"nama": "Budi", "usia": 30};
$json_str = json_encode($data_obj);
echo `JSON string: ${$json_str}`;

$decoded_obj = json_decode($json_str);
echo `Nama dari JSON: ${$decoded_obj.nama}`; # Akses properti objek belum sepenuhnya didukung
```

## Kontribusi

Kami menyambut kontribusi! Silakan ajukan *pull request* atau buka *issue* jika Anda menemukan *bug* atau memiliki saran fitur.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.
