import unittest
import pytest

from app import app
from app import SiteUtils

class AppTestCase(unittest.TestCase):
    # Test funkcji home
    def test_home(self):
        # Tworzę tets clienta
        tester=app.test_client(self)
        # Wywołuję metodę GET na endpoincie '/'
        # To, co nam zwróci metoda GET, zapiszemy do zmiennej "response"
        response=tester.get('/')
        # Sprawdzam, czy zapytanie się powiodło
        # (a powiodło się, gdy status code jest równy 200)
        assert response.status_code == 200
        # Sprawdzam treśc komunikatu
        assert response.get_data() == b"Witam na moim API!"

    def test_home_powitanie(self):
        tester=app.test_client(self)
        # To samo co powyżej, ale dla endpointu "/powitanie"
        response=tester.get('/powitanie')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(), b"Witam na moim API!")

    @pytest.mark.parametrize("name", ['Zenek', 'Kamil', 'Ania', 'Basia'])
    def test_hello_you(name):
        tester=app.test_client()
        response=tester.get(f"/powitanie/{name}")
        assert response.status_code == 200
        assert response.get_data().decode()== f"Witam serdecznie, {name}"

    def test_get_active_cases(self):
        utils=SiteUtils()
        cases=utils.request_active_covid_cases()
        assert cases.status_code == 200
        self.assertIsInstance(cases.content,bytes)

if __name__=="__main__":
    unittest.main(verbosity=2)
