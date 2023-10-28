document.addEventListener("DOMContentLoaded", function () {
  const namaPacar = document.getElementById("nama_pacar");
  const usiaPacar = document.getElementById("usia_pacar");
  const tombolAnimasi = document.getElementById("tombol_animasi");

  // Animasi sederhana saat tombol ditekan
  tombolAnimasi.addEventListener("click", function () {
    tombolAnimasi.style.transform = "scale(1.2)";
    setTimeout(() => {
      tombolAnimasi.style.transform = "scale(1)";
    }, 200);
  });

  // Mengganti nama pacar dan usianya
  namaPacar.textContent = "Ayunda Sari";
  usiaPacar.textContent = "19";
});
