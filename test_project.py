import unittest
from appium import webdriver

class CalculatorTests(unittest.TestCase):

    @classmethod

    def setUpClass(self):

        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def getresults(self):
        displaytext = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = displaytext.strip("Display is " )
        displaytext = displaytext.rstrip(' ')
        displaytext = displaytext.lstrip(' ')
        return displaytext


    def test_display(self):
        self.driver.find_element_by_name("Clear").click()
        self.driver.find_element_by_name("Two").click()
        self.assertEqual(self.getresults(),"2")
        self.driver.find_element_by_name("One").click()
        self.assertEqual(self.getresults(),"21")
        self.driver.find_element_by_name("Clear").click()

    def test_addition(self):
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Plus").click()
        self.driver.find_element_by_name("Seven").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(),"8")

    def test_subtraction(self):
        self.driver.find_element_by_name("Four").click()
        self.driver.find_element_by_name("Minus").click()
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(),"3")   


    def test_combination(self):
        self.driver.find_element_by_name("Seven").click()
        self.driver.find_element_by_name("Multiply by").click()
        self.driver.find_element_by_name("Nine").click()
        self.driver.find_element_by_name("Plus").click()
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Equals").click()
        self.driver.find_element_by_name("Divide by").click()
        self.driver.find_element_by_name("Eight").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(),"8")

    def test_division(self):
        self.driver.find_element_by_name("Eight").click()
        self.driver.find_element_by_name("Eight").click()
        self.driver.find_element_by_name("Divide by").click()
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("One").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(),"8")

    def test_squared(self):
        self.driver.find_element_by_name("Two").click()
        self.driver.find_element_by_name("Square").click()
        self.assertEqual(self.getresults(),"4")
        self.driver.find_element_by_name("Square").click()
        self.assertEqual(self.getresults(),"16")      

    def test_backspace(self):
        self.driver.find_element_by_name("Five").click()
        self.driver.find_element_by_name("Seven").click()
        self.driver.find_element_by_name("Eight").click()
        self.assertEqual(self.getresults(),"578")
        self.driver.find_element_by_name("Backspace").click()
        self.assertEqual(self.getresults(),"57")
        self.driver.find_element_by_name("Backspace").click()
        self.assertEqual(self.getresults(),"5")
        self.driver.find_element_by_name("Clear").click()

    def test_decimal(self):
        self.driver.find_element_by_name("Decimal Separator").click()
        self.driver.find_element_by_name("Five").click()
        self.driver.find_element_by_name("Plus").click()
        self.driver.find_element_by_name("Decimal Separator").click()
        self.driver.find_element_by_name("Seven").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(),"1.2")
        self.driver.find_element_by_name("Minus").click()
        self.driver.find_element_by_name("Decimal Separator").click()
        self.driver.find_element_by_name("Two").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(),"1")

    def test_division_by_zero(self):
        self.driver.find_element_by_name("Five").click()
        self.driver.find_element_by_name("Divide by").click()
        self.driver.find_element_by_name("Zero").click()
        self.driver.find_element_by_name("Equals").click()
        self.assertEqual(self.getresults(),"Cannot divide by zero")

    def test_invalid_root(self):
        self.driver.find_element_by_name("Five").click()
        self.driver.find_element_by_name("Positive Negative").click()
        self.assertEqual(self.getresults(),"-5")
        self.driver.find_element_by_name("Square root").click()
        self.assertEqual(self.getresults(),"Invalid input")




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)