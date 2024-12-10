from typing import Union, Dict

data = {
    "km": 1,
    "hm": pow(10, 1),
    "dam": pow(10, 2),
    "m": pow(10, 3),
    "dm": pow(10, 4),
    "cm": pow(10, 5),
    "mm": pow(10, 6)
}

def convert_to_km(satuan: str) -> int:
    return data.get(satuan)

def data_new(angka: Union[float, int], satuan: str) -> Dict[str, str]:
    data_baru = None
    # for k, v in data.items():
    #     data_new = {k, v*convert_to_km(satuan)*angka}
    return {k: v*convert_to_km(satuan)*angka for k, v in data.items()}

print(data_new(12, "cm"))
