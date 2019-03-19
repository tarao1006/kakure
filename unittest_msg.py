import unittest
import msg

class msgTest(unittest.TestCase):

    def test_soutei(self):
        actual = msg.make_results('970\n0\n16-22\n18-23.5\n17-21.5')
        expected = '基本給: \t14.5\n深夜給: \t1.5\n合計: \t16.0\n\n基本給: \t¥14,065\n深夜給: \t¥1,818\n合計: \t¥15,883\n控除: \t¥600\n支給額: \t¥15,283\n(時給1: \t¥970)\n(時給2: \t¥1,212)\n\n勤務日数: \t3日'
        self.assertEqual(expected, actual)

    def test_wage(self):
        actual = msg.make_results('970')
        expected = '勤務時間を入力してください。'
        self.assertEqual(expected, actual)

    def test_wage_day(self):
        actual = msg.make_results('970\n0')
        expected = '勤務時間を入力してください。'
        self.assertEqual(expected, actual)

    def test_early(self):
        actual = msg.make_results('970\n0\n15-23')
        expected = '開始時間が16時よりも早い日があります。確認してください。\n\n基本給: \t7.0\n深夜給: \t1.0\n合計: \t8.0\n\n基本給: \t¥6,790\n深夜給: \t¥1,212\n合計: \t¥8,002\n控除: \t¥200\n支給額: \t¥7,802\n(時給1: \t¥970)\n(時給2: \t¥1,212)\n\n勤務日数: \t1日'
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
