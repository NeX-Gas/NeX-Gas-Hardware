# Casing NeX-IOGas — v2 (cetak tanpa support)

Kotak elektronik terpisah dari jalur gas, dengan LCD 16×2 (I2C) di muka depan.
Interior sengaja polos (tanpa pocket/standoff modul) karena layout elektronik
masih dibahas.

Dibuat di SolidCraft dengan parameter `in_w`, `in_h`, `in_d`, `wall`, `fil_r`
untuk amplop dan dinding. **Posisi fitur (gland, tab, baut, boss) masih angka
tetap** — kalau ukuran amplop diubah, fitur itu perlu disesuaikan.

## File

| File | Isi |
|---|---|
| `NeX-IOGas_Casing.sc` | Desain SolidCraft (2 body: Tray, FrontPlate) |
| `NeX-IOGas_Casing.step` | STEP untuk CAD lain |
| `NeX-IOGas_Casing.3mf` | Mesh, masih di orientasi desain |
| `NeX-IOGas_Tray_print.stl` | **Tray siap cetak**, sudah diputar, Z = 0 |
| `NeX-IOGas_Lid_print.stl` | **Lid siap cetak**, sudah diputar, Z = 0 |
| `hero.png` | Render 3/4 |
| `tools/orient_for_print.py` | Skrip yang memutar STL ke pose cetak |

## Amplop

| | mm |
|---|---|
| Interior (W × H × D) | 136 × 84 × 46 |
| Eksterior | 140.0 × 88.0 × 50.0 |
| Tinggi total dengan tab | 98.0 |
| Dinding / plat | 2.0 |
| Sudut luar | R4 (tray dan plat) |

## Orientasi cetak — wajib

| Part | Pose | Footprint |
|---|---|---|
| Tray | **dinding belakang di bed, bukaan menghadap atas** | 140 × 98 × 48 |
| Lid | **muka luar di bed, boss LCD menghadap atas** | 140 × 88 × 15 |

Kedua STL `*_print.stl` **sudah** dalam pose ini (Z minimum = 0), jadi tinggal
slice. Kalau memakai `NeX-IOGas_Casing.3mf`, putar tray 90° terhadap X.

Ini bukan preferensi: kalau tray dicetak berdiri di dasarnya (pose desain),
atap interior 136 × 44 mm jadi bidang horizontal dan support memenuhi kotak.

## Verifikasi cetak

Di-slice dengan Orca untuk A1 mini, profil **0.20 Standard / PETG Basic**
(3 wall, 15% infill), **support diaktifkan** dengan ambang 30°:

| Part | Filament | Waktu | Support |
|---|---|---|---|
| Tray | 75.84 g | 2h 56m | **0.00 g** (0 tanda support) |
| Lid | 26.71 g | 1h 08m | 0.01 g (2 tanda kecil di bawah huruf) |
| **Total** | **≈ 102.6 g** | **≈ 4h 04m** | ≈ 0 |

Untuk lebih hemat: 2 perimeter + 10–15% infill.

## Lubang

| Fitur | Ukuran | Catatan |
|---|---|---|
| Jendela LCD | 66 × 17 | viewing area 64.5 × 16 |
| Gland daya | M16, **teardrop 45°** | dinding bawah, X = +25 |
| Gland sensor/solenoid | M20, **teardrop 45°** | dinding bawah, X = +52 |
| USB | 8 × 10 + atap 45° | dinding kiri, sejajar ujung ESP32 |
| Ventilasi | 6 × Ø6, **teardrop 45°** | 3 per sisi |
| Tab dinding | 2× 30 × 3, Ø4.5 | atas, X = ±45 |
| Kaki karet | 4 recess Ø10 × 0.8 | bawah |

Puncak teardrop menghadap **+Y** (arah "atas" saat dicetak), sesuai standar
lubang horizontal: sisi 45° tidak perlu support, beda dengan lengkung 90°.

## Baut

| Item | Jumlah |
|---|---|
| M3 × 12 self-tapping (plat → tray) | 4 |
| M2.5 × 10 self-tapping (LCD → plat) | 4 |
| Sekrup M4 + washer (tab ke dinding) | 2 |
| Gland M16 / M20 + mur | 1 + 1 |
| Kaki karet Ø10 | 4 |

## Yang membuatnya 0 support

1. **Boss sudut sekarang tembus** dari dinding belakang sampai rim — jadi kolom
   vertikal. Versi sebelumnya berhenti 12 mm dan ujungnya berupa bidang
   horizontal 7 × 7 mm di ketinggian 36 mm; itu yang memicu support.
2. **Lubang gland & ventilasi teardrop 45°** — puncak menghadap arah cetak.
3. **Lubang USB diberi atap 45°**, bukan ambang datar.
4. Tidak ada lagi pad/pocket modul yang membuat bidang menggantung.

## Catatan / yang perlu dicek

1. **Ruang di bawah LCD.** Backpack LCD memakan ± 24.5 mm dari muka plat
   (boss 13.5 + backpack ≤ 11), sisa ± 21.5 mm ke dinding belakang.
2. **Tebal backpack LCD** diasumsikan ≤ 11 mm. Kalau lebih, boss LCD ditambah.
3. **Deboss "NEX-IOGas"** menyisakan 0.01 g support (2 tanda) karena huruf
   dicetak menghadap bed. Kalau mau benar-benar 0.000 g, bilang — labelnya
   saya hapus atau saya ganti jadi engraving V.
4. **Plat belum punya spigot/lip** — penempatan mengandalkan 4 baut M3.
5. **Gantung dinding pakai tab**, bukan keyhole.
6. **USB** hanya untuk flashing; jarak ujung konektor ke dinding kiri ± 8.6 mm.
7. **Kabel I2C LCD** ikut plat saat dibuka — pakai konektor 4-pin di sisi ESP32.

## Elektrikal LCD (belum ada di firmware)

| LCD I2C | ESP32 |
|---|---|
| VCC | 5 V (dari step-down) |
| GND | GND |
| SDA | GPIO21 |
| SCL | GPIO22 |
