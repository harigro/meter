document.addEventListener("DOMContentLoaded", () => {
  // ambil kelas modal
  const modal = document.querySelector(".modal");
  const overlay = document.querySelector(".overlay");
  const btnCloseModal = document.querySelector(".close-modal");
  const closeModal = () => {
        modal.classList.add("hidden");
        overlay.classList.add("hidden");
      };

  btnCloseModal.addEventListener("click", closeModal);
  overlay.addEventListener("click", closeModal);
  const buat_modal = () => {
    modal.classList.remove("hidden");
      overlay.classList.remove("hidden");

      
  }
  // ambil tombol tekan berdasarkan kelas
  const tombolMeter = document.querySelector(".tombol");
  tombolMeter.addEventListener("click", () => {
    const input_pengguna = document.querySelector(".angka");
    const nilai_input = document.querySelectorAll(".result");
    const regex = /(\d+)\s?(km|hm|dam|m|dm|cm|mm)\b/;
    const match = input_pengguna.value.trim().match(regex);

    if (match) {
      // Mengirim permintaan ke server menggunakan fetch()
      fetch("/greet", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `nilai=${encodeURIComponent(
          match[1]
        )}&satuan=${encodeURIComponent(match[2])}`,
      })
        .then((response) => response.json()) // Mengubah response menjadi format JSON
        .then((data) => {
          // Menampilkan hasil ke dalam input
          input_pengguna.value = data.greeting.m;
          // nilai_input.forEach((n, item) => {
          //   let nilai =
          //     parseFloat(match[1]) *
          //     konversi_ke_km(match[2].toLowerCase()) *
          //     Math.pow(10, item);
          //   n.value = cocok(nilai.toFixed(7-item-1)) + " " + n.classList[0];
          // });
        })
        .catch((error) => {
          // Menampilkan error jika terjadi kesalahan
          resultDiv.innerHTML = "<p>Terjadi kesalahan!</p>";
        });
    } else {
      buat_modal()
    }
  });
});
