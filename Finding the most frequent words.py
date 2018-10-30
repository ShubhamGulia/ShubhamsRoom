from collections import Counter

text ="The internet is an essential employment resource for many of today’s job seekers, according to a new survey " \
     "by Pew Research Center. A majority of U.S. adults (54%) have gone online to look for job information, 45% have" \
    "applied for a job online, and job-seeking Americans are just as likely to have turned to the internet during their" \
    "most recent employment search as to their personal or professional networks. Yet even as the internet has taken on" \
    "a central role in how people find and apply for work, a minority of Americans would find it difficult to engage in many" \
    "digital job seeking behaviors – such as creating a professional resume, searching job listings online, or following up via " \
    "email with potential employers. And while many of today’s job seekers are enlisting their smartphones to browse jobs or" \
    "communicate with potential employers, others are using their mobile devices for far more complex and challenging tasks, from " \
    "writing a resume to filling out an online job application."

words= text.split()

counter= Counter(words)
top_five= counter.most_common(5)
print(top_five)