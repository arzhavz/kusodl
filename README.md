# kusodl
Kusonime downloader dengan desain GUI, intinya gitu.
<p><strong>Info aja, proyek ini aku perluas dan aku kembangin. Tapi di repo lain, cek aja langsung di </strong><a href="https://github.com/arzhavz/stdl">https://github.com/arzhavz/stdl</a></p>

## Instalasi
Install-nya gampang cuy
### HP
Untuk install di HP, download termux dulu di <a href="https://f-droid.org/id/packages/com.termux">sini</a>.
<p>Kalau udah, paste perintah di bawah ya buat update environment termux-nya.</p>

```sh
pkg update -y && pkg upgrade -y
```

<p>Setelah itu, download pkg yang diperlukan yaitu GIT dan Python pake perintah di bawah.</p>

```sh
pkg i git python -y
```

<p>Langkah terakhir, download repo ini ke termux dan install library yang diperlukan.</p>

```sh
git clone https://github.com/hitori21/kusodl && cd kusodl && python -m pip install -r requirements.txt -U
```

<p>Jalankan program dengan mengetik <code>python main.py</code></p>

### Windows
Untuk instalasi di Windows, download <a href="https://cmder.app/">cmder</a> dan <a href="https://python.org">Python</a> dulu. Setelah diinstall, buka cmder-nya.

<p>Pertama, langsung paste aja perintah di bawah.</p>

```sh
git clone https://github.com/hitori21/kusodl && cd kusodl && py -m pip install -r requirements.txt -U
```

<p>Untuk menjalankan program, buka cmd atau powershell. Caranya klik <code>windows + r</code>.</p>
<p>Kalau ngga, buka folder repo yang udah didownload dan klik kanan lalu pilih 'buka di terminal' (Windows 11)</p>
<p>Setelah itu ketik <code>py main.py</code></p>
