import unittest
import json
from urllib.request import urlopen

class TestApplication(unittest.TestCase):

    def test_application_health(self):
        response = urlopen("http://localhost:8000/health")
        data = json.loads(response.read())

        self.assertEqual(response.status, 200)
        self.assertEqual(data["status"], "healthy")

    def test_application_name(self):
        response = urlopen("http://localhost:8000/health")
        data = json.loads(response.read())

        self.assertEqual(
            data["application"],
            "Cloud DevOps Platform"
        )

if __name__ == "__main__":
    unittest.main()
