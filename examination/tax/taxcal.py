import tax


def calculate_tax():
    salary = float(input('请输入月收入:'))
    salary_tax = tax.tax(salary)
    income_tax = 0.0
    if salary_tax <= 1500:
        income_tax = salary_tax * 0.03
    elif 1500 < salary_tax <= 4500:
        income_tax = salary_tax * 0.1 - 105
    elif 4500 < salary_tax <= 9000:
        income_tax = salary_tax * 0.2 - 555
    elif 9000 < salary_tax <= 35000:
        income_tax = salary_tax * 0.25 - 1005
    elif 35000 < salary_tax <= 55000:
        income_tax = salary_tax * 0.3 - 2002
    elif 55000 < salary_tax <= 80000:
        income_tax = salary_tax * 0.35 - 5505
    elif salary_tax > 80000:
        income_tax = salary_tax * 0.45 - 13505

    print('应纳个人所得税税额为: %.2f' % income_tax)


if __name__ == '__main__':
    calculate_tax()
