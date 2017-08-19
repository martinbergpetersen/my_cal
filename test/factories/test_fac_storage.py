import unittest
from src.factories.fac_storage import StorageFactory
from src.handlers.csv_handler import CSV


class TestFacStorage(unittest.TestCase):

    def test_fac_csv(self):
        factory = StorageFactory()
        result = factory.create_instance('CSV')
        self.assertEqual(type(CSV), type(result))
