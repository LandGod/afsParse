import re  # Regular expression library, possibly not needed.
import csv  # CSV Parsing Library

'''
Example of output format:
<div>
    <h3>
        Title
    </h3>
    <p>
        Category* <br>
        Location* <br> 
        Start Date <br> 
        Start Time – End Time
     </p>
     <p>
        Description
     </p>
     <p>
        <a href="https://fostercaretraining.org/registration/?course_email=aevans@afs4kids.org&amp;course_title=HTMLCOMLIANTFORMATTEDTITLE&amp;course_date=STARTDATE&amp;course_location=LOCATION">
            Register
        </a>
    </p>
</div>
'''

# Open csv file called test.csv and create a dictionary of data based off of the given field names
# Note that each Field name entry will include all cells up and down from the title, inclusive of the title, until the end of the document, so 
# we must take care to ignore data we don't need
# TODO: Handle grabbing a file not called test.csv
with open('test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['Category*','Title','Description', 'CEUs', 'Start Date', 'End Date', 'Start Time', 'End Time', 'Location*', 'Sponsoring Agency*'])




## For reference
    # for row in reader:
    #     if row['Start Date'] != '':
    #         print(row['Start Date'])



## Old parsing file I made a while ago, here for reference: 

# old_list = open('test.csv', 'r')
# new_list = open('parsedInfo.txt', 'w')


# pattern = re.compile(r"[a-z]{4,}\s")
# new_list.write('[')
# timer = 15
# for line in old_list:
#     theWord = pattern.search(line)
#     if (not theWord):
#         print('Nope')
#         print("Continuing")
#         continue
#     new_list.write("\"" + theWord.group(0).strip() + "\", ")
#     timer = timer - 1
#     if timer < 1:
#         new_list.write("\n")
#         timer = 15


# new_list.write(']')
# old_list.close()
# new_list.close()