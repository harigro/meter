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
          data_entrys = {
            0: data.greeting.km,
            1: data.greeting.hm,
            2: data.greeting.dam,
            3: data.greeting.m,
            4: data.greeting.dm,
            5: data.greeting.cm,
            6: data.greeting.mm
          }
          nilai_input.forEach((n, item) => {
            n.value = data_entrys[item] + " " + n.classList[0];
          });
        })
        .catch((error) => {
          // Menampilkan error jika terjadi kesalahan
          alert("Terjadi kesalahan di peladen");
        });
    } else {
      buat_modal()
    }
  });
});
