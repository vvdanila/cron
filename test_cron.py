import unittest

import cron
 

class CronScheduler(unittest.TestCase):
 
    def test_minute_frequency_valid(self):
        self.assertEqual(cron.schedule('59', 'minutes'), '59')
        self.assertEqual(cron.schedule('1,4,5,6', 'minutes'), '1 4 5 6')
        self.assertEqual(cron.schedule('1-3', 'minutes'), '1 2 3')
        self.assertEqual(cron.schedule('1-10/2', 'minutes'), '1 3 5 7 9')

    def test_minute_frequency_invalid(self):
        with self.assertRaises(ValueError):
            cron.schedule('invalid_minute', 'minutes')

    def test_command(self):
        self.assertEqual(cron.get_command(['/bin/foo', 'bar']), '/bin/foo bar')

    def test_month_frequency_all(self):
        self.assertEqual(cron.schedule('*', 'months'), '1 2 3 4 5 6 7 8 9 10 11 12')

    def test_weekday_valid(self):
        self.assertEqual(cron.schedule('6', 'weekdays'), '6')

    def test_weekday_invalid(self):
        with self.assertRaises(AssertionError):
            cron.schedule('7', 'weekdays')
 
if __name__ == '__main__':
    unittest.main()