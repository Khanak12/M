x={'Khanak':6,'is':6,'learning':6,'python':2}
searching=6
frequency=0
for key in x:
    if x[key]==searching:
        frequency=frequency+1
        
print("The number of times that 6 occured is", frequency)