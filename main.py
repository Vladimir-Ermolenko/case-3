"""Case-study #3 Investment report
Developers:
Sharkov 40(%), Ermolenko (35%), Keda 30(%).
"""

# The program counts all the numbers connected with your deposit

# Lets the user choose the language
language = input('Ввеедите язык(Русский , English, Deutsch)').lower()
if language == 'русский':
    import locru as loc
elif language == 'english':
    import locen as loc
elif language == 'deutsch':
    import locgr as loc
else:
    import locen as loc

# Base for future numbers
basis_of_investment = []
interest_amount = []
capital = []

# Lets the user choose deposit qualities
years = int(input(loc.time))
initial_capital = float(input(loc.starting_cap))
percent = float(input(loc.interest))
investment_infusion = float(input(loc.refill))

# Needed for further calculations
basis_of_investment.append(round(initial_capital, 2))

for i in range(1, years * 12):
    basis_of_investment.append((basis_of_investment[i - 1] * (1 + (percent / 100)) + investment_infusion))

for i in range(0, (years * 12)):
    interest_amount.append(basis_of_investment[i] * (percent / 100))
    capital.append(interest_amount[i] + basis_of_investment[i])

# Intermediate operations
max_len_basis = len(str(round(basis_of_investment[years * 12 - 1]))) + 3
max_len_interest = len(str(round(interest_amount[years * 12 - 1]))) + 3
max_len_capital = len(str(round(capital[years * 12 - 1]))) + 3

if max_len_basis < 12:
    max_len_basis = 12
if max_len_interest < 10:
    max_len_interest = 10
if max_len_capital < 9:
    max_len_capital = 9

# Completes the table with the found numbers depending on the language the user chose
for year in range(1, years + 1):
    if language == 'русский':
        print(year, loc.yearn)
        print("-" * (12 + max_len_basis + max_len_interest + max_len_capital))
        print("|       |", ' ' * ((max_len_basis - 12) // 2), 'основа', ' ' * (((max_len_basis-12) // 2) + 2), '|',
              ' ' * ((max_len_interest - 12) // 2), 'сумма %', ' ' * ((max_len_interest - 9) // 2), '|',
              ' ' * (max_len_capital - 2), '|')
        print("| месяц |", ' ' * (((max_len_basis - 12) // 2)-2), 'инвестиций', ' ' * ((max_len_basis - 12) // 2),
              "|", ' ' * ((max_len_interest - 12) // 2), 'за месяц', ' ' * (((max_len_interest - 12) // 2) + 1), '|',
              ' ' * (((max_len_capital - 12) // 2) - 2), "капитал",  ' ' * (((max_len_capital - 12) // 2) + 3), "|")
        print("-" * (12 + max_len_basis + max_len_interest + max_len_capital))
    elif language == 'english':
        print(year, loc.yearn)
        print("-" * (12 + max_len_basis + max_len_interest + max_len_capital))
        print("|       |", ' ' * ((max_len_basis - 12) // 2),  "invest", ' ' * (((max_len_basis-12) // 2) + 2), "|",
              ' ' * ((max_len_interest - 12) // 2), "% sum", ' ' * (((max_len_interest - 12) // 2) + 4), '|',
              ' ' * ((max_len_capital) - 2), '|')
        print("| month |", ' ' * ((max_len_basis - 12) // 2), "base",  ' ' * (((max_len_basis - 12) // 2) + 4), "|",
              ' ' * ((max_len_interest - 12) // 2), "for month", ' ' * ((max_len_interest - 12) // 2), "|",
              ' ' * ((max_len_capital - 12) // 2),  "capital", ' ' * (((max_len_capital - 12) // 2) + 1),  "|")
        print("-" * (12 + max_len_basis + max_len_interest + max_len_capital))
    elif language == 'deutsch':
        print(year, loc.yearn)
        print("-" * (12 + max_len_basis + max_len_interest + max_len_capital))
        print("|       |",  ' ' * ((max_len_basis - 12) // 2),  "basis", ' ' * (((max_len_basis-12) // 2) + 3), "|",
              ' ' * ((max_len_interest - 12) // 2), "% menge", ' ' * (((max_len_interest - 12) // 2)+1), "|",
              ' ' * (max_len_capital - 1), '|')
        print("| monte |",  ' ' * ((max_len_basis - 12) // 2), "investition", ' ' * (((max_len_basis - 12) // 2)-3),
              "|", ' ' * ((max_len_interest - 12) // 2), "pro monte", ' ' * (((max_len_interest - 12) // 2)-1),  "|",
              ' ' * ((max_len_capital - 12) // 2),  "kapital",' ' * (((max_len_capital - 12) // 2) + 2),   "|")
        print("-" * (12 + max_len_basis + max_len_interest + max_len_capital))
    else:
        print(year, loc.yearn)
        print("-" * (12 + max_len_basis + max_len_interest + max_len_capital))
        print("|       |", ' ' * ((max_len_basis - 12) // 2), "invest", ' ' * (((max_len_basis - 12) // 2) + 2), "|",
              ' ' * ((max_len_interest - 12) // 2), "% sum", ' ' * (((max_len_interest - 12) // 2) + 4), '|',
              ' ' * (max_len_capital - 2), '|')
        print("| month |", ' ' * ((max_len_basis - 12) // 2), "base", ' ' * (((max_len_basis - 12) // 2) + 4), "|",
              ' ' * ((max_len_interest - 12) // 2), "for month", ' ' * ((max_len_interest - 12) // 2), "|",
              ' ' * ((max_len_capital - 12) // 2), "capital", ' ' * (((max_len_capital - 12) // 2) + 1), "|")
        print("-" * (12 + max_len_basis + max_len_interest + max_len_capital))
    for month in range(12):
        if (month + 1) < 10:
            print('|   ', month + 1, '   ', sep='', end='|')
        else:
            print('|  ', month + 1, '   ', sep='', end='|')
        print("{0:.2f}".format(basis_of_investment[(year * 12) + month - 12]),
              ' ' * (max_len_basis - len(str(round(basis_of_investment[(year * 12) + month - 12])))-3), sep='', end='|')
        print("{0:.2f}".format(interest_amount[(year * 12) + month - 12]),
              ' ' * (max_len_interest - len(str(round(interest_amount[(year * 12) + month - 12])))-3), sep='', end='|')
        print("{0:.2f}".format(capital[(year * 12) + month - 12]),
              ' ' * (max_len_capital - len(str(round(capital[(year * 12) + month - 12])))-3), sep='', end='|\n')
    print("-" * (12 + max_len_basis + max_len_interest + max_len_capital))

