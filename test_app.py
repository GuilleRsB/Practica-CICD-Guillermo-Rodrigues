import unittest
from app.app import app, dias_vividos


class TestDiasVividos(unittest.TestCase):

    def test_dias_vividos(self):
        self.assertEqual(dias_vividos(10), 3650)

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Calcula los d\xc3\xadas vividos',
            response.data
        )

    def test_index_post_valid(self):
        response = self.client.post(
            '/',
            data={'nombre': 'Guillermo', 'edad': '25'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Guillermo, has vivido aproximadamente',
            response.data
        )

    def test_index_post_invalid(self):
        response = self.client.post(
            '/',
            data={'nombre': 'Guillermo', 'edad': 'abc'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Error: La edad debe ser un n\xc3\xbamero entero.',
            response.data
        )


if __name__ == '__main__':
    unittest.main()
