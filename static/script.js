// Fungsi modular untuk menangani modal
const setupModal = (modalSelector, overlaySelector, closeSelector) => {
  const modal = document.querySelector(modalSelector);
  const overlay = document.querySelector(overlaySelector);
  const btnCloseModal = document.querySelector(closeSelector);

  const closeModal = () => {
    modal.classList.add("hidden");
    overlay.classList.add("hidden");
  };

  const openModal = () => {
    modal.classList.remove("hidden");
    overlay.classList.remove("hidden");
  };

  btnCloseModal.addEventListener("click", closeModal);
  overlay.addEventListener("click", closeModal);

  return { openModal, closeModal };
};

const button_click = (angkaSelector, hasilSelector, modalPeladen, modalClient) => {
  const inputPengguna = document.querySelector(angkaSelector);
  const nilaiInput = document.querySelectorAll(hasilSelector);

  const interactivate = () => {
    const regex = /(-?\d+((\.|\,)\d+)?)\s?(km|hm|dam|m|dm|cm|mm)\b/;
    const match = inputPengguna.value.trim().match(regex);

    if (match) {
      // Mengirim permintaan ke server menggunakan fetch()
      fetch("/greet", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `nilai=${encodeURIComponent(match[1])}&satuan=${encodeURIComponent(match[4])}`})
        .then((response) => response.json())
        .then((data) => {
          const dataEntry = {
            0: data.greeting.km,
            1: data.greeting.hm,
            2: data.greeting.dam,
            3: data.greeting.m,
            4: data.greeting.dm,
            5: data.greeting.cm,
            6: data.greeting.mm,
          };

          nilaiInput.forEach((n, item) => { n.value = dataEntry[item] + " " + n.classList[0]; });
        })
        .catch((error) => { modalPeladen.openModal(); });
    } else { modalClient.openModal(); }}
  return { interactivate }
}

document.addEventListener("DOMContentLoaded", () => {

  // Setup modal peladen dan klien
  const modalPeladen = setupModal(".modal.peladen", ".overlay.peladen", ".close-modal.peladen");
  const modalClient = setupModal(".modal", ".overlay", ".close-modal");
  const button_c = button_click(".angka", ".result", modalPeladen, modalClient);

  // ambil tombol tekan berdasarkan kelas
  const tombolMeter = document.querySelector(".tombol");
  tombolMeter.addEventListener("click", () => {
    button_c.interactivate()
  });
});
