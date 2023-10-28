<?php
    $nama = $_POST['nama'];
    $fajar = isset($_POST['fajar']) ? $_POST['fajar'] : 'Tidak Absen';
    $terbit = isset($_POST['terbit']) ? $_POST['terbit'] : 'Tidak Absen';
    $dzuhur = isset($_POST['dzuhur']) ? $_POST['dzuhur'] : 'Tidak Absen';
    $ashar = isset($_POST['ashar']) ? $_POST['ashar'] : 'Tidak Absen';
    $maghrib = isset($_POST['maghrib']) ? $_POST['maghrib'] : 'Tidak Absen';
    $isya = isset($_POST['isya']) ? $_POST['isya'] : 'Tidak Absen';

    // Simpan data absen dalam file teks
    $data = "Nama: $nama\n";
    $data .= "Fajar: $fajar\n";
    $data .= "Terbit: $terbit\n";
    $data .= "Dzuhur: $dzuhur\n";
    $data .= "Ashar: $ashar\n";
    $data .= "Maghrib: $maghrib\n";
    $data .= "Isya: $isya\n\n";

    $file = fopen('data_absen.txt', 'a'); // Mode 'a' untuk menambahkan data ke file
    fwrite($file, $data);
    fclose($file);

    // Kirim respon ke AJAX
    echo 'Absen berhasil dikirim';
?>
