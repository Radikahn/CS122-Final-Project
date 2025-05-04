from tests.test_orm import TestOrmFunction
from tests.test_user_obj import TestUserObjects

orm_testing = TestOrmFunction()
orm_testing.test_table_add()
orm_testing.test_table_update()
orm_testing.test_table_query()

user_obj_testing = TestUserObjects()
user_obj_testing.test_user_create()
user_obj_testing.test_user_username_Change()
user_obj_testing.test_add_attributes()


