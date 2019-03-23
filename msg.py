import re

class SubmittedMessage:

    def __init__(self, submitted_message: list):
        # define type
        self.type = self.check_type(submitted_message)
        self.alert = False
        self.early_start = False
        self.late_start = False
        self.late_end = False
        self.all_income = None
        self.base_income = None
        self.base_time = None
        self.contents = None
        self.days = None
        self.dinner = None
        self.income = None
        self.night_time = None
        self.night_income = None
        self.wage = None
        self.nodinner = 0
        self.txt = ''

        # set parameters
        if self.type==0:
            self.contents = submitted_message
            self.days = len(self.contents)
            self.base_time, self.night_time = self.calculate_separete_time()
        elif self.type==1 or self.type==2:
            self.wage = int(submitted_message[0])
            self.contents = submitted_message[1:]
            if self.type==2:
                self.nodinner = int(submitted_message[1])
                self.contents = submitted_message[2:]
            self.days = len(self.contents)
            self.base_time, self.night_time = self.calculate_separete_time()
            self.base_income = int(self.wage * self.base_time)
            self.night_income = int(int(self.wage * 1.25) * self.night_time)
            self.income = self.base_income + self.night_income
            self.dinner = 200 * (self.days - self.nodinner)
            if self.dinner<0:
                self.txt += 'まかないを食べていない日数が勤務日数よりも多いです。'
                self.alert = True
            else:
                self.all_income = self.income - self.dinner
        elif self.type==3:
            self.txt += '勤務時間を入力してください。'
            self.alert = True
        elif self.type==-1:
            self.txt += '不正な入力値(数字以外の文字および - , . , : 以外の記号)が含まれているか、不正な入力形式です。'
            self.alert = True
        else:
            pass


    def check_type(self, s: list):
        '''
        help, ヘルプ, へるぷ -> 100
        数字および許可された記号以外, 不正な入力形式 -> -1
        時給, 勤務時間 -> 1
        時給, まかないを食べなかった日, 勤務時間 -> 2
        勤務時間なし -> 3
        勤務時間のみ -> 0
        '''
        if self.check_help(s):
            return 100
        if self.check_error(s):
            return -1
        if all(re.match('^\d+$',i) for i in s):
            return 3
        if self.check_int_or_not(s[0]):
            if self.check_int_or_not(s[1]):
                return 2 #s[0]がintかつs[1]がint
            else:
                return 1 #s[0]がint
        else:
            return 0

    def check_help(self, s):
        if s[0] in ['help', 'ヘルプ', 'へるぷ']:
            return 1
        else:
            return 0


    def check_error(self, s):
        if all(re.match('^\d{2}.?\d{0,2}-\d{2}.?\d{0,2}$|^\d*$', replace_time_display(t)) for t in s ):
            return 0
        else:
            return 1

    def check_int_or_not(self, s):
        try:
            int(s)
        except ValueError:
            return 0
        else:
            return 1

    def calculate_separete_time(self):
        base = night = 0
        for content in self.contents:
            s, e = map(float, replace_time_display(content).split('-'))
            if e-s<0:
                self.txt += '勤務時間の入力値が不正です。\n\n'
                self.alert = True
                return 0, 0
            if s<16:
                self.early_start = True
            if s>18:
                self.late_start = True
            if e>=24:
                self.late_end = True
            if e>22:
                night += e - 22
                base += 22 - s
            else:
                base += e - s
        return base, night


def replace_particular_symbols(s):
    return s.replace('-','').replace('.','').replace(':','')

def replace_time_display(s):
    return s.replace(':00', '.0').replace(':0', '.0').replace(':15', '.25').replace(':30', '.5').replace(':45', '.75')


def make_results(txt: str):
    result = ''
    message_list = [l.replace(' ', '') for l in list(txt.split('\n')) if l]

    s = SubmittedMessage(message_list)
    if s.alert:
        result += s.txt.strip()
    else:
        if s.type==100:
            result += '上の写真のようなメッセージを送ってください。'
        else:
            if s.early_start:
                result += '開始時間が16時よりも早い日があります。確認してください。\n\n'
            if s.late_start:
                result += '開始時間が18時よりも遅い日があります。確認してください。\n\n'
            if s.late_end:
                result += '終了時間が24時よりも遅い日があります。確認してください。\n\n'
            if s.type in [0, 1, 2]:
                result += s.txt + "基本給: \t{:.1f}\n深夜給: \t{:.1f}\n合計: \t{:.1f}\n\n".format(s.base_time, s.night_time, (s.base_time+s.night_time))
                if s.type in [1, 2]:
                    result += '基本給: \t¥{:,}\n深夜給: \t¥{:,}\n合計: \t¥{:,}\n控除: \t¥{:,}\n支給額: \t¥{:,}\n(時給1: \t¥{:,})\n(時給2: \t¥{:,})\n\n' \
                        .format(s.base_income, s.night_income, s.income, s.dinner, s.all_income, s.wage, int(s.wage*1.25))
            result += '勤務日数: \t{}日'.format(s.days)
    return result

class option:
    def __init__(self):
        self.a = None
