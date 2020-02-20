import datetime,calendar
date=input("Dose mou mia imerominia:")
date=date.split("/")
today = datetime.date.today()
someday = datetime.date(int(date[2]), int(date[1]), int(date[0]))
diff = someday - today
days=diff.days
hours=days*24
minutes=hours*60
seconds=minutes*60
print("H hmerominia pou edoses apexei apo simera se meres:",days,"se ores",hours,"se defterolepta",seconds)
DaysOfMonth=calendar.monthrange(int(date[2]),int(date[1]))[1]
print("O sigkekrimenos minas exei",DaysOfMonth,"meres")

