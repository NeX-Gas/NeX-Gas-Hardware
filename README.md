# Casing NeX-IOGas — v1

Kotak elektronik terpisah dari jalur gas, dengan LCD 16×2 (I2C) di muka depan.
Dibuat di SolidCraft dengan parameter `in_w`, `in_h`, `in_d`, `wall`, `fil_r`
untuk amplop dan dinding. **Posisi fitur internal (pocket modul, gland, tab,
baut) masih angka tetap** — kalau ukuran amplop diubah, fitur itu perlu
disesuaikan; sudah diuji, mengubah `in_w`/`in_h` saja membuat boss sudut lepas.

## File

| File | Isi |
|---|---|
| `NeX-IOGas_Casing.sc` | Desain parametrik SolidCraft (2 body: Tray, FrontPlate) |
| `NeX-IOGas_Casing.step` | STEP untuk CAD lain |
| `NeX-IOGas_Casing.3mf` | Mesh untuk slicer |
| `hero.png` | Render 3/4 |

## Amplop

| | mm |
|---|---|
| Interior (W × H × D) | 136 × 84 × 46 |
| Eksterior | 140.8 × 88.8 × 50.8 |
| Dengan tab dinding | tinggi total 98.8 |
| Dinding / plat | 2.4 |
| Sudut luar | R4 |

Kedua bagian muat print bed 180 × 180 × 180:

- **Tray** 140.8 × 98.8 × 48.4 — cetak dengan bukaan menghadap ke atas
  (dinding belakang di bed). Tanpa support.
- **FrontPlate** 140.8 × 88.8 × 13.5, sudut R4 sama dengan tray — cetak dengan
  muka dalam di bawah (boss LCD menghadap ke atas). Tanpa support. Jendela dan
  tulisan tercetak mulus di permukaan atas.

## Isi kotak

| Modul | Dudukan | Posisi |
|---|---|---|
| ESP32 DevKit 38-pin (54.4 × 27.9) | pocket 55.2 × 28.6, dalam 2.4 | kiri atas |
| Modul relay 1ch (50 × 26) | pocket 49.4 × 24.6 | kiri bawah |
| Step-down LM2596 (43 × 21) | pocket 42.4 × 19.6 | kanan atas |
| LCD 16×2 + backpack I2C (80 × 36) | 4 boss Ø7 × 13.5, pilot M2.5 | plat depan |

Pocket modul dibuat 0.8 mm lebih besar dari PCB supaya longgar; board turun
masuk dari depan dan tidak bisa lepas setelah plat terpasang.

## Lubang

| Fitur | Ukuran | Catatan |
|---|---|---|
| Jendela LCD | 66 × 17 | viewing area 64.5 × 16 |
| Gland daya | Ø16.3 (M16) | dinding bawah, X = +25 |
| Gland sensor/solenoid | Ø20.3 (M20) | dinding bawah, X = +52 |
| USB | 8 × 10 | dinding kiri, sejajar ujung ESP32 |
| Ventilasi | 4 slot 3 × 20 | 2 per sisi |
| Tab dinding | 2× 30 × 3, Ø4.5 | atas, X = ±45 |
| Kaki karet | 4 recess Ø10 × 0.8 | bawah |

## Baut

| Item | Jumlah |
|---|---|
| M3 × 12 self-tapping (plat → tray) | 4 |
| M2.5 × 10 self-tapping (LCD → plat) | 4 |
| Sekrup M4 + washer (tab ke dinding) | 2 |
| Gland M16 / M20 + mur | 1 + 1 |
| Kaki karet Ø10 | 4 |

## Cetak

PETG, 0.2 mm, 3 perimeter, 25% infill. Volume solid 118.1 cm³ (± 152 g);
dengan infill 25% biasanya keluar 90–110 g untuk keduanya.

## Catatan / yang perlu dicek saat review

1. **Tinggi modul relay.** Pocket relay 2.4 mm dalam; relay duduk 4 mm dari
   dinding belakang. Modul relay 1ch umumnya 17–20 mm di atas PCB. Relai
   sengaja ditaruh di baris bawah supaya tidak bertabrakan dengan backpack
   LCD. Kalau modulmu lebih tinggi dari 22 mm, kabari — kedalaman kotak
   dinaikkan.
2. **Tebal backpack LCD** diasumsikan ≤ 11 mm. Kalau lebih, boss LCD
   ditambah.
3. **Plat belum punya spigot/lip** — penempatan mengandalkan 4 baut M3.
   Kalau perlu, v2 bisa ditambah bibir 2 mm.
4. **Gantung dinding pakai tab**, bukan keyhole. Tab dibuat di bidang
   belakang supaya tercetak rata di bed tanpa support.
5. **USB** hanya untuk flashing; jarak ujung konektor ke dinding kiri
   ± 8.6 mm, jadi pakai kabel micro-USB yang overmold-nya ramping atau
   lepas plat sekali untuk flash pertama.
6. **Kabel I2C LCD** ikut plat saat dibuka — pakai konektor 4-pin di sisi
   ESP32, bukan solder langsung.

## Elektrikal LCD (belum ada di firmware)

Firmware `NeX-Gas-Firmware.ino` belum memuat kode LCD. Pin I2C default
ESP32 masih kosong dan tidak bentrok dengan sensor:

| LCD I2C | ESP32 |
|---|---|
| VCC | 5 V (dari step-down) |
| GND | GND |
| SDA | GPIO21 |
| SCL | GPIO22 |
