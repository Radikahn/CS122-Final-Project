import unittest
from data_management import orm_data


class TestOrmFunction(unittest.TestCase):

    def setUp(self):
        # orm setup
        self.engine = orm_data.create_engine('sqlite:///user_account_data.db')
        
        self.Session = orm_data.sessionmaker(bind=self.engine)
        
        self.session = self.Session()
        
        user_data = orm_data.UserData(username = "Tom", account_type = "Savings", yearly_income = 130000, monthly_spending = 3200) 

        self.session.add(user_data)

        self.session.commit()


    
    def test_table_add(self):
        
        user_data = orm_data.UserData(username = "Michael", account_type = "Savings", yearly_income = 130000, monthly_spending = 3200) 

        self.session.add(user_data)

        self.session.commit()

        user_instance = self.session.query(orm_data.UserData.username).filter_by(username = "Michael").all()

        self.assertEqual(user_instance, "Michael")


    def test_table_update(self):
        
        update_income = orm_data.update(orm_data.UserData).where(
                orm_data.UserData.username == 'Tom').values(yearly_income=190000)
    
        self.session.execute(update_income)
    
        user_instance = self.session.query(orm_data.UserData.yearly_income).filter_by(username = 'Tom').all()

        self.assertEqual(user_instance,190000)


    def test_table_query(self):
        
        user_instance = self.session.query(orm_data.UserData.username).filter_by(username = 'Tom').all()

        self.assertEqual(user_instance, "Tom")



if __name__ == '__main__':
    unittest.main()

