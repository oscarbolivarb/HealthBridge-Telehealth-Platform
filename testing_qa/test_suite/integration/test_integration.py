import unittest

# Simulate scheduling an appointment
def schedule_appointment(name):
  return f"Appointment scheduled for {name}"

# Simulate writing to the audit Log
def audit_log(message):
  return f"Audit: {message}


class TestIntegration(unittest.TestCase):

  def test_schedule_appointment(self):
    result = schedule_appointment("John Smith")
    self.assertEqual(result, "Appointment scheduled for John Smith")

  def test_audit_log(self):
    result = audit_log("Appointment created")
    self.assertEqual(result, "Audit: Appointment created")

  if __name__ == "__main__":
    unittest.main()
