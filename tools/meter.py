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
        self.negatif = {
            "km": 1,
            "hm": pow(10, -1),
            "dam": pow(10, -2),
            "m": pow(10, -3),
            "dm": pow(10, -4),
            "cm": pow(10, -5),
            "mm": pow(10, -6)
        }
        self.positif = {
            "km": 1,
            "hm": pow(10, 1),
            "dam": pow(10, 2),
            "m": pow(10, 3),
            "dm": pow(10, 4),
            "cm": pow(10, 5),
            "mm": pow(10, 6)
        }
    
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
        return {k: format_scientific(v * n_tabel * self.validation_string()) 
                for k, v in self.data_tabel.positif.items()
            }

if __name__=="__main__":
    tt = TabelSatuanMeter("2.5", "cm").tabel_new()
    print(tt)
