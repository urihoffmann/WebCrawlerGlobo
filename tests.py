from main import app
import unittest

class AppTestCase(unittest.TestCase):

    def test_root(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_auth_allowed(self):
        tester = app.test_client(self)
        response = tester.post(
            '/feed',
            data=dict(username="editoraglobo", password="challenge"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_auth_not_allowed(self):
        tester = app.test_client(self)
        response = tester.post(
            '/feed',
            data=dict(username="abc", password="def"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 401)



if __name__ == '__main__':
    unittest.main()
