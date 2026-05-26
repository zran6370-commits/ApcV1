# Apc Language

Apc adalah bahasa pemrograman eksperimental yang dirancang untuk menggabungkan fitur-fitur dari Python, PHP, JSON, dan JavaScript. Tujuannya adalah untuk menyediakan bahasa yang serbaguna dan mudah digunakan untuk berbagai aplikasi, mulai dari skrip sederhana hingga pengembangan web.

## Fitur Utama

- **Sintaksis Intuitif**: Mengadopsi sintaksis yang bersih dan mudah dibaca.
- **Tipe Data Dinamis**: Mendukung tipe data dinamis dan struktur fleksibel.
- **Integrasi JSON**: Dukungan bawaan untuk struktur data bergaya JSON.
- **Berorientasi Web**: Dirancang dengan mempertimbangkan pengembangan web.

## Instalasi

Untuk menjalankan interpreter Apc, Anda hanya perlu Python 3 terinstal di sistem Anda.

```bash
git clone https://github.com/zran6370-commits/ApcV1.git
cd ApcV1
python3 apc_interpreter.py <nama_file_apc>
```

## Penggunaan

Untuk menjalankan program Apc, gunakan interpreter `apc_interpreter.py`:

```bash
python3 apc_interpreter.py examples/hello.apc
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
let versi = 0.1;

echo `Selamat datang di ${$nama} versi ${versi}!`;
```

### Kondisional

`examples/conditionals.apc`:

```apc
$nilai = 75;

if ($nilai >= 90) {
  echo "Nilai A";
} else if ($nilai >= 80) {
  echo "Nilai B";
} else if ($nilai >= 70) {
  echo "Nilai C";
} else {
  echo "Nilai D";
}
```

### Loop

`examples/loops.apc`:

```apc
for ($i = 0; $i < 3; $i++) {
  echo `Iterasi ke: ${$i}`;
}

$buah = ["Apel", "Jeruk", "Mangga"];
for $item in $buah {
  echo `Saya suka ${$item}`;
}
```

### Fungsi

`examples/functions.apc`:

```apc
func tambah($a, $b) {
  return $a + $b;
}

$hasil = tambah(5, 3);
echo `Hasil penambahan: ${$hasil}`;
```

### Data JSON

`examples/json_data.apc`:

```apc
$pengguna = {
  "nama": "Budi",
  "usia": 30,
  "aktif": true
};

echo `Nama: ${$pengguna.nama}`;
echo `Usia: ${$pengguna.usia}`;

$data_json_string = json_encode($pengguna);
echo $data_json_string;
```

## Kontribusi

Kami menyambut kontribusi! Silakan ajukan *pull request* atau buka *issue* jika Anda menemukan *bug* atau memiliki saran fitur.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.
