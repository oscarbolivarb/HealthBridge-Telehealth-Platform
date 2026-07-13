import unittest

# Check if a phone number is valid 
def validate_phone(phone):
  return len(phone) == 10 and phone.isdigit()

# Check if an appointment is within clinic hours
def validate_clinic_hours(hour):
  return 8 <= hour <= 17

class TestValidation(unittest.TestCase):

  def test_valid_phone(self):
    self.assertTrue(validate_phone("1234567890"))

  def test_invalid_phone(self): 
    self.assertFalse(validate_phone("12345"))

  def test_valid_clinic_hours(self):
    self.assertTrue(validate_clinic_hours(10))

  def test_invalid_clinic_hours(self):
    self.assertFalse(validate_clinic_hours(22))

if __name__== "__main__":
  unittest.main()
