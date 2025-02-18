from typing import Union, Dict
from babel.numbers import format_scientific
import re

class ValidateString:
    def __init__(self, value: str):
        """Mendeteksi apakah parameter integer atau float"""
        self.value = value

    def is_int(self) -> bool:
        return re.fullmatch(r"-?\d+", self.value) is not None

    def is_float(self) -> bool:
        return re.fullmatch(r"-?\d+\.\d+", self.value) is not None
    
class DataTabel:
    def __init__(self):
        """Menghasilkan tabel satuan meter"""
        meter_n = [1, 1e-1, 1e-2, 1e-3,
                   1e-4, 1e-5, 1e-6] 
        meter_p = [1, 1e1, 1e2, 1e3,
                   1e4, 1e5, 1e6]
        self.negatif = dict(zip(["km", "hm", "dam", "m", "dm", "cm", "mm"], meter_n))
        self.positif = dict(zip(["km", "hm", "dam", "m", "dm", "cm", "mm"], meter_p))
    
class TabelSatuanMeter:
    """Membuat tabel konversi untuk satuan meter"""
    def __init__(self, angka: str, satuan: str):
        self.angka = angka
        self.satuan = satuan
        self.data_tabel = DataTabel()

    def validation_string(self) -> Union[int, float]:
        vv = ValidateString(self.angka)
        if vv.is_float():
            return float(self.angka)
        if vv.is_int():
            return int(self.angka)

    def tabel_new(self) -> Dict[str, str]:
        """menghasilkan tabel baru"""
        n_tabel = self.data_tabel.negatif.get(self.satuan)
        result = map(lambda item: (item[0], format_scientific(round(item[1] * n_tabel * self.validation_string(), 10))),
                     self.data_tabel.positif.items())
        return dict(result)