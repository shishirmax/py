import csv
with open('eggs.csv', 'w') as csvfile:
    #spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter = csv.writer(csvfile,delimiter = '|',lineterminator='\n')
    #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['IUserId','User','IPersonId','FirstName','MiddleName','LastName','Email','RowNumber'])
    #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    spamwriter.writerow(['IUserId','User','IPersonId','FirstName','MiddleName','LastName','Email','RowNumber'])
    spamwriter.writerow(['IUserId','User','IPersonId','FirstName','MiddleName','LastName','Email','RowNumber'])
