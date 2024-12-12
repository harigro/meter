import unittest
from ..meter import TabelSatuanMeter

class TestTabelSatuanMeter(unittest.TestCase):

    def test_kunci_tabel_meter(self):
        tt = TabelSatuanMeter(2.5, "m").data
        kunci = [k for k in tt.keys()]
        data = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
        self.assertEqual(kunci, data)

    def test_konversi_m(self):
        tt = TabelSatuanMeter(2.5, "m").tabel_new()
        expected = {
            'km': '2500.0',
            'hm': '25000.0',
            'dam': '250000.0',
            'm': '2500000.0',
            'dm': '25000000.0',
            'cm': '250000000.0',
            'mm': '2500000000.0'
        }
        self.assertEqual(tt, expected)

    def test_satuan_tidak_valid(self):
        with self.assertRaises(TypeError):
            TabelSatuanMeter(3.5, "invalid").tabel_new()

if __name__ == "__main__":
    unittest.main()