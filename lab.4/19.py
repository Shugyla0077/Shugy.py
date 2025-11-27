from datetime import datetime

today=datetime.today()

end_of_year=datetime(today.year,12,31)

days_remaining =(end_of_year- today).days

print (f"31 желтоқсанға дейін {days_remaining} күн қалды.")






from datetime import datetime

today=datetime.today()

end _of_year=datetime(today.year,12,31 )

days_remaining=(end_of_year- today).days

print (f"31 желтоқсанға дейін{days_remaining}күн қалды.")



def cube (a,b):
    for i in range (a,b+1):
        yield i*i*i 

a=1
b=5
for num in cube (a,b):
    print(num)



