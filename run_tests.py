from tests.test_orm import TestOrmFunction


orm_testing = TestOrmFunction()
orm_testing.setUp()
orm_testing.test_table_add()
orm_testing.test_table_update()
orm_testing.test_table_query()

