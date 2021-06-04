user = input("How would you like your month's Ordred?: Alphabetical, Calender, or Days?: ")
Alpha = ("April, August, December, Febuary, January, July, June, March, May, November, October, September")
if user == ('Alphabetical'):
    print(Alpha)
Beta = ("January, Febuary, March, April, May, June, July, August, September, October, November, December")
if user == ('Calender'):
    print(Beta)
Delta = ("January - 31, Febuary - 28, March - 31, April - 30, May - 31, June - 30, July - 31, August - 31, September - 30, October - 31, November - 30, December - 31,")
if user == ('Days'):
    print(Delta)
