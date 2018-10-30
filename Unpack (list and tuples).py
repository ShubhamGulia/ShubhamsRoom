def drop_grades(grades):
    first, *middle, last = grades
    # If we want to take average of number excluding first and last
    avg = sum(middle) / len(middle)
    print(avg)
    print(middle)


drop_grades([80,60,50,40,10])