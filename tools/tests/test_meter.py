import unittest
from ..meter import TabelSatuanMeter, ValidateString, DataTabel

class TestDataTabel(unittest.TestCase):

    def test_kunci_tabel_meter(self):
        tabel = DataTabel().positif
        kunci = [k for k in tabel.keys()]
        data = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
        self.assertEqual(kunci, data)


    def test_tabel_positif(self):
        tabel = DataTabel().positif
        positif = {
            "km": 1,
            "hm": pow(10, 1),
            "dam": pow(10, 2),
            "m": pow(10, 3),
            "dm": pow(10, 4),
            "cm": pow(10, 5),
            "mm": pow(10, 6)
        }
        self.assertEqual(tabel, positif)

    def test_tabel_positif(self):
        tabel = DataTabel().negatif
        negatif = {
            "km": 1,
            "hm": pow(10, -1),
            "dam": pow(10, -2),
            "m": pow(10, -3),
            "dm": pow(10, -4),
            "cm": pow(10, -5),
            "mm": pow(10, -6)
        }
        self.assertEqual(tabel, negatif)

class TestTabelSatuanMeter(unittest.TestCase):
    {'km': '1.2E1', 'hm': '1.2E2', 'dam': '1.2E3', 'm': '1.2E4', 'dm': '1.2E5', 'cm': '1.2E6', 'mm': '1.2E7'}

    def test_konversi_hm(self):
        tt = TabelSatuanMeter("120", "hm").tabel_new()
        expected = {
            'km': '1.2E1', 'hm': '1.2E2', 'dam': '1.2E3', 
            'm': '1.2E4', 'dm': '1.2E5', 'cm': '1.2E6', 'mm': '1.2E7'
        }
        self.assertEqual(tt, expected)

    def test_konversi_dm(self):
        tt = TabelSatuanMeter("12", "dm").tabel_new()
        expected = {
            'km': '1.2E-3', 'hm': '1.2E-2', 'dam': '1.2E-1', 
            'm': '1.2E0', 'dm': '1.2E1', 'cm': '1.2E2', 'mm': '1.2E3'
        }
        self.assertEqual(tt, expected)

    def test_konversi_cm(self):
        tt = TabelSatuanMeter("2.5", "cm").tabel_new()
        expected = {
            'km': '2.5E-5', 'hm': '2.5E-4', 'dam': '2.5E-3', 
            'm': '2.5E-2', 'dm': '2.5E-1', 'cm': '2.5E0', 'mm': '2.5E1'
        }
        self.assertEqual(tt, expected)

    def test_satuan_tidak_valid(self):
        with self.assertRaises(TypeError):
            TabelSatuanMeter("3.5", "invalid").tabel_new()

class TestValidateString(unittest.TestCase):

    def test_validasi_string_int(self):
        data = ValidateString("12").is_int()
        self.assertEqual(True, data)

    def test_validasi_string_float(self):
        data = ValidateString("1.2").is_float()
        self.assertEqual(True, data)

    def test_validasi_string_int_adalah_False(self):
        data = ValidateString("1.2").is_int()
        self.assertEqual(False, data)

    def test_validasi_string_float_adalah_False(self):
        data = ValidateString("12").is_float()
        self.assertEqual(False, data)

if __name__ == "__main__":
    unittest.main()
