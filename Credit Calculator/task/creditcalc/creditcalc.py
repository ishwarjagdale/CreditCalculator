from math import ceil, log
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-type=', '--type', type=str, help='Annuity or Differential')
parser.add_argument('-principal=', '--principal', type=int)
parser.add_argument('-periods=', '--periods', type=int)
parser.add_argument('-interest=', '--interest', type=float)
parser.add_argument('-payment=', '--payment', type=int)
args = parser.parse_args()


def y_n_m(year, month):
    if year and month > 0:
        print(f"You need {year} {'years' if year > 1 else 'year'} and {month} {'months' if year > 1 else 'month'} to "
              f"repay this credit!")
    elif year == 0:
        print(f"You need {month} {'months' if year > 1 else 'month'} to "
              f"repay this credit!")
    elif month == 0:
        print(f"You need {year} {'years' if year > 1 else 'year'} to "
              f"repay this credit!")


def count_of_months(principal, payment, interest):
    interest = interest / (12 * 100)
    n = ceil(log((payment / (payment - (interest * principal))), 1 + interest))
    year, month = n // 12, n % 12
    y_n_m(year, month)
    print(f"Overpayment = {int(payment * n - principal)}")


def annuity_payment(principal, periods, interest):
    interest = interest / (12 * 100)
    annuity = ceil((principal * interest * ((1 + interest) ** periods)) / (((1 + interest) ** periods) - 1))
    print(f"Your annuity payment = {int(annuity)}!")
    print(f"\nOverpayment = {int(annuity * periods - principal)}")


def credit(payment, periods, interest):
    interest = interest / (12 * 100)
    credit_p = payment / ((interest * ((1 + interest) ** periods)) / (((1 + interest) ** periods) - 1))
    print(f"Your credit principal = {int(credit_p)}!")
    print(f"Overpayment = {int((payment * periods) - int(credit_p))}")


def differential(principal, periods, interest):
    interest = interest / (12 * 100)
    init_sum = 0
    for i in range(1, int(periods) + 1):
        dn = ceil((principal / periods) + (interest * (principal - (principal * (i - 1) / periods))))
        init_sum += dn
        print(f"Month {i}: paid out {dn}")
    print(f"Overpayment = {int(init_sum - principal)}")


if len(sys.argv) == 5:
    if args.type == 'diff' and (args.principal and args.periods and args.interest is not None):
        differential(args.principal, args.periods, args.interest)

    elif args.type == 'annuity' and (args.payment and args.periods and args.interest is not None):
        credit(args.payment, args.periods, args.interest)

    elif args.type == 'annuity' and (args.principal and args.payment and args.interest is not None):
        count_of_months(args.principal, args.payment, args.interest)

    elif args.type == 'annuity' and (args.principal and args.periods and args.interest is not None):
        annuity_payment(args.principal, args.periods, args.interest)
    else:
        print("Incorrect parameters")
        exit()
else:
    print("Incorrect parameters")
    exit()
