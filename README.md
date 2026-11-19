# Casing NeX-IOGas — v1

Kotak elektronik terpisah dari jalur gas, dengan LCD 16×2 (I2C) di muka depan.
Dibuat di SolidCraft dengan parameter `in_w`, `in_h`, `in_d`, `wall`, `fil_r`
untuk amplop dan dinding. **Posisi fitur (gland, tab, baut, boss) masih angka
tetap** — kalau ukuran amplop diubah, fitur itu perlu disesuaikan; sudah diuji,
mengubah `in_w`/`in_h` saja membuat boss sudut lepas.

Interior sengaja **polos** (tanpa pocket/standoff modul) karena layout elektronik
masih dibahas. Modul bisa ditempel busa double-tape atau dibuatkan bracket
terpisah setelah layout final.

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
| Eksterior | 140.0 × 88.0 × 50.0 |
| Dengan tab dinding | tinggi total 98.0 |
| Dinding / plat | 2.0 |
| Sudut luar | R4 |

Kedua bagian muat print bed 180 × 180 × 180:

- **Tray** 140.0 × 98.0 × 48.0 — cetak dengan bukaan menghadap ke atas
  (dinding belakang di bed). Tanpa support.
- **FrontPlate** 140.0 × 88.0 × 15.0, sudut R4 sama dengan tray — cetak dengan
  muka dalam di bawah (boss LCD menghadap ke atas). Tanpa support. Jendela dan
  tulisan tercetak mulus di permukaan atas.

## Isi kotak

| Modul | Dudukan |
|---|---|
| LCD 16×2 + backpack I2C (80 × 36) | 4 boss Ø7 × 13.5 di plat, pilot M2.5 |
| ESP32 / relay / step-down | belum ada — interior polos, menunggu layout final |

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

PETG, 0.2 mm, 3 perimeter, 25% infill. Volume solid **91.0 cm³** (± 117 g massa
solid); dengan dinding 2.0 mm hasil cetak biasanya **75–85 g** untuk keduanya.
Paling hemat: 2 perimeter + 15% infill — cukup untuk kotak elektronik indoor.

## Catatan / yang perlu dicek saat review

1. **Ruang di bawah LCD.** Backpack LCD memakan ± 24.5 mm dari muka plat
   (boss 13.5 + backpack ≤ 11), sisa ± 21.5 mm ke dinding belakang. Modul yang
   ditaruh tepat di belakang jendela LCD harus lebih pendek dari itu; relay 1ch
   (± 20.6 mm termasuk PCB) masih masuk, tapi tipis.
2. **Tebal backpack LCD** diasumsikan ≤ 11 mm. Kalau lebih, boss LCD
   ditambah dan ruang di belakangnya berkurang.
3. **Interior polos** — belum ada dudukan modul. Kalau layout sudah pasti,
   bilang posisi tiap modul, saya tambahkan bracket/pocket di v2.
4. **Plat belum punya spigot/lip** — penempatan mengandalkan 4 baut M3.
   Kalau perlu, v2 bisa ditambah bibir 2 mm.
5. **Gantung dinding pakai tab**, bukan keyhole. Tab dibuat di bidang
   belakang supaya tercetak rata di bed tanpa support.
6. **USB** hanya untuk flashing; jarak ujung konektor ke dinding kiri
   ± 8.6 mm, jadi pakai kabel micro-USB yang overmold-nya ramping atau
   lepas plat sekali untuk flash pertama.
7. **Kabel I2C LCD** ikut plat saat dibuka — pakai konektor 4-pin di sisi
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
