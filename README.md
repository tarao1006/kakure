# 勤務時間計算くん

![python](https://img.shields.io/badge/python-3.7+-blue.svg)
![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)

# Introduction
Please add me as a LINE friend via blow QRcode or button. This bot surely help with boring calculation using manpower and a calculator at the end of the month.

&nbsp;&nbsp; [<img height="36" border="0" alt="友だち追加" src="https://scdn.line-apps.com/n/line_add_friends/btn/ja.png">](https://line.me/R/ti/p/%40cek5889j)

[<img height="150" border="0" alt="QRcode" src="code.png">](http://qr-official.line.me/L/EXQCPCz-w9.png)



# Demo
This demo gif shows so slow reply, but actually this bot reply more quickly than this gif shows.

 <img height="600" alt="demo" src="usage.gif">


# Usage
This bot accept below three formats. You can show a half hour as "xx:30" or "xx.5".This bot will not accept fill-width characters (zenkaku) forms. When you send designated forms, it immediately returns the amount of how long you worked before 22'o clock, and after 22'o clock. If your message contains the information of your hourly wage, it also returns your monthly wages.

## ex.1

The first line indicates the hourly wage. The second line shows the days you did not eat the staff meals. And from the third line, they show your work time. Please hyphenate the time when you started working and the end time.
1. 950
2. 2
3. 17-22.5
4. 18-23:30


## ex.2

If you omit the days you did not eat the staff meals, this bot regards you ate them every time you worked.
1. 950
2. 17-22.5
3. 18-23:30

## ex.3
You can input only work time. In this case, this bot will not calculate and return your wages.
1. 17-22.5
2. 18-23:30
