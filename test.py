try:
    from app import app
    import unittest

except Exception as e:
    print("some Modules are missing {}".format(e))

class FlaskTest(unittest.TestCase):

    # check for response 200
    def test_index(self):
        tester = app.test_client(self)
        
        response = tester.get("/product")
        
        statuscode = response.status_code
        
        self.assertEqual(statuscode, 200)
        
    # check if content return is application / json
    
    def test_index_content(self):
        tester = app.test_client(self)
        
        response = tester.get("/product")
        
        self.assertEqual(response.content_type, "application/json")
        
    # check for Data returned
    
    def test_name_data(self):
        tester = app.test_client(self)
        
        response = tester.get("/product")
        
        self.assertTrue(b'name' in response.data)
    
    def test_description_data(self):
        tester = app.test_client(self)
        
        response = tester.get("/product")
        
        self.assertTrue(b'description' in response.data)
        
    def test_price_data(self):
        tester = app.test_client(self)
        
        response = tester.get("/product")
        
        self.assertTrue(b'price' in response.data)
        
    def test_qty_data(self):
        tester = app.test_client(self)
        
        response = tester.get("/product")
        
        self.assertTrue(b'qty' in response.data)
        
    def test_non_existing_product(self):
        # test a non existing office
        tester = app.test_client(self)
        
        response = tester.get("/product/1")
            
        self.assertEqual(response._status_code, 200)

        
    
        
         
        
