# Tugas Sistem Deteksi Intrusi

## Christian Andrew 05311840000017

Tugas sistem deteksi intrusi ini saya menggunakan machine learning untuk melakukan deteksi terhadap wajah orang yang akan masuk ke dalam ruangan saya dan bisa membedakan mana wajah yang terdaftar dan mana yang tidak terdaftar. Setelah bisa membedakan mana yang wajah dikenal dan mana yang tidak, maka akan mengirimkan pesan ke whatsapp bahwa ada orang yang masuk ke dalam ruangan saya.

## Requirement
1. Opencv
2. Numpy
3. Pyautogui

Pyautogui digunakan untuk mengirimkan pesan kepada whatsapp bahwa ada orang yang masuk ke dalam ruangan beserta image yang di capture.

## Cara Kerja

Pertama kita perlu melakukan training terhadap machine learning kita dengan cara mengambil sebanyak 20 sample wajah kita yang akan kemudian di train menjadi file berekstensi yml. Setelah itu kita langsung melakukan pengecekan apakah yang di deteksi oleh camera adalah wajah yang di kenali atau tidak. Baik itu dikenali atau tidak maka akan langsung mengirim foto dari wajah orang tersebut ke whatsapp.

## Output Program

Disini ada foto hasil run program
