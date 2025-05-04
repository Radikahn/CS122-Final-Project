import unittest
from app.user_accounts import UserAccounts as user


class TestUserObjects(unittest.TestCase):

    def test_user_create(self):
        user_object = user()

        user_object.username = "Tom"
        
        self.assertEqual(user_object.username, "Tom")


    def test_user_username_Change(self):
        user_object = user()

        user_object.username = "Tom"

        user_object.username = "Fred"

        self.assertEqual(user_object.username, "Fred")


    def test_add_attributes(self):
        
        user_object = user()

        user_object.username = "Tom"
        user_object.yearly_income = 120000
        user_object.account_type = "Savings"
        user_object.monthly_spending = 3200

        test_attributes = [user_object.username, user_object.yearly_income, user_object.account_type, user_object.monthly_spending]

        planned_attributres = ["Tom", 120000, "Savings", 3200]

        self.assertTrue(planned_attributres, test_attributes)


if __name__ == '__main__':
    unittest.main()
