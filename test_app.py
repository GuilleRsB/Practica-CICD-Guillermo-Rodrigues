import unittest
from app.app import app, dias_vividos


class TestDiasVividos(unittest.TestCase):

    # Prueba de la función 'dias_vividos' con diferentes casos
    def test_dias_vividos(self):
        self.assertEqual(dias_vividos(10), 3650)  # Caso normal
        self.assertEqual(dias_vividos(0), 0)  # Caso límite: edad mínima
        self.assertEqual(dias_vividos(-5), 0)  # Caso límite: valores negativos
        self.assertEqual(dias_vividos(100), 36500)  # Caso extremo

    # Configuración antes de cada prueba
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    # Prueba para GET en la página principal
    def test_index_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Calcula los d\xc3\xadas vividos',
            response.data
        )

    # Prueba para POST válido en la página principal
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

    # Prueba para POST inválido (edad no numérica)
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

    # Prueba para POST con edad vacía
    def test_index_post_empty_age(self):
        response = self.client.post(
            '/',
            data={'nombre': 'Guillermo', 'edad': ''}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Error: La edad debe ser un n\xc3\xbamero entero.',
            response.data
        )

    # Prueba para POST con edad en un valor extremo (150 años)
    def test_index_post_large_age(self):
        response = self.client.post(
            '/',
            data={'nombre': 'Guillermo', 'edad': '150'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Guillermo, has vivido aproximadamente',
            response.data
        )


if __name__ == '__main__':
    unittest.main()