from typing import Union, Dict

class TabelSatuanMeter:
    """Membuat tabel konversi untuk satuan meter"""
    def __init__(self, angka: Union[float, int], satuan: str):
        self.angka = angka
        self.satuan = satuan
        self.data = {
            "km": 1,
            "hm": pow(10, 1),
            "dam": pow(10, 2),
            "m": pow(10, 3),
            "dm": pow(10, 4),
            "cm": pow(10, 5),
            "mm": pow(10, 6)
        }

    def tabel_new(self) -> Dict[str, str]:
        """menghasilkan tabel baru"""
        convert_to_km = self.data.get(self.satuan)
        return {k: str(v * convert_to_km * self.angka) for k, v in self.data.items()}
    
if __name__=="__main__":  
    tt = TabelSatuanMeter(1.25, "cm").tabel_new()
    print(tt)
