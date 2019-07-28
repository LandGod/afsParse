import re  # Regular expression library, possibly not needed.
import csv  # CSV Parsing Library
import urllib.parse as parseURL # For formatting data when constructing the url. Will use urllib.parse.quote()


# Example of output format:
# <div>
#     <h3>
#         Title
#     </h3>
#     <p>
#         Category* <br>
#         Location* <br> 
#         Start Date <br> 
#         Start Time – End Time
#      </p>
#      <p>
#         Description
#      </p>
#      <p>
#         <a href="https://fostercaretraining.org/registration/?course_email=aevans@afs4kids.org&amp;course_title=HTMLCOMLIANTFORMATTEDTITLE&amp;course_date=STARTDATE&amp;course_location=LOCATION">
#             Register
#         </a>
#     </p>
# </div>


# Open csv file called test.csv and create a dictionary of data based off of the given field names
# Note that each Field name entry will include all cells up and down from the title, inclusive of the title, until the end of the document, so 
# we must take care to ignore data we don't need
# TODO: Handle grabbing a file not called test.csv
with open('test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['Category*','Title','Description', 'CEUs', 'Start Date', 'End Date', 'Start Time', 'End Time', 'Location*', 'Sponsoring Agency*'])

    for row in reader:
        # Check for blank/title row, and ignore any such
        if row['Title'] == '' or row['Title'] == 'Title':
            continue

        title = row['Title']
        category = row['Category*'].strip()
        location = row['Location*'].strip()
        date = row['Start Date'].strip()
        startTime = row['Start Time'].strip()
        endTime = row['End Time'].strip()
        description = row['Description'].strip()

        parsedTitle = parseURL.quote(title)
        link = 'https://fostercaretraining.org/registration/?course_email=aevans@afs4kids.org&course_title={parsedTitle}&course_date={date}&course_location={location}'.format(parsedTitle=parsedTitle, date=date, location=location)

        print("""<h3>\n\t{title}\n</h3>\n<p>\n\t{category}<br>\n\t{location}<br>\n\t{date}<br>\n\t{startTime}-{endTime}\n</p>\n<p>\n\t{description}\n</p>\n<p>\n\t<a href=\"{link}\">\n\t\tRegister\n\t</a>\n</p>""".format(title=title, category=category, location=location, date=date, startTime=startTime, endTime=endTime, description=description, parsedTitle=parsedTitle, link=link))
        
        print('\n-------------------------------------------------\n')



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