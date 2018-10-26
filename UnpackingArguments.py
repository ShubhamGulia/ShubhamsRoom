def health_cal(age,apples,cig):
    solutions=(100-age)+(apples*2)-(cig*1)
    print(solutions)

#directly passing arguments
health_cal(27,20,0)

#shubham_data
shubham_data=[24,2,0]
#passing arguments one by one
health_cal(shubham_data[0],shubham_data[1],shubham_data[2])
#Unpacking arguments
health_cal(*shubham_data)