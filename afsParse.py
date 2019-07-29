import re  # Regular expression library, possibly not needed.
import csv  # CSV Parsing Library
import urllib.parse as parseURL # For formatting data when constructing the url. Will use urllib.parse.quote()
import sys  # So I can grab command line arguments for the file name.

# For optional gui file explorer
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# Output should look like this:
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

# Imports a file name from the command line if the user has supplied one.
# If the user has not supplied one, prompt the user
try:
    filename = sys.argv[1]
except(IndexError):
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

# Check file type
if filename[-4:] == '.csv':
    fileType = False
elif filename[-4:] == '.xls':
    fileType = True
elif filename[-5:] == '.xlsx':
    fileType = True
else:
    raise TypeError('Incorrect file type! Filetype must be: csv, xls, or xlsx')

# Open csv file called test.csv and create a dictionary of data based off of the given field names
# Note that each Field name entry will include all cells up and down from the title, inclusive of the title, until the end of the document, so 
# we must take care to ignore data we don't need
with open(filename, newline='') as csvfile:

    # If excel file supply the optional dialect argument and set it to 'excel' else, for csv file, no argument to dialect
    if fileType:
        reader = csv.DictReader(csvfile, fieldnames=['Category*','Title','Description', 'CEUs', 'Start Date', 'End Date', 'Start Time', 'End Time', 'Location*', 'Sponsoring Agency*'], dialect='excel')
    else:
        reader = csv.DictReader(csvfile, fieldnames=['Category*','Title','Description', 'CEUs', 'Start Date', 'End Date', 'Start Time', 'End Time', 'Location*', 'Sponsoring Agency*'])


    for row in reader:
        # Check for blank/title row, and ignore any such
        if row['Title'] == '' or row['Title'] == 'Title':
            continue
        # For useable rows, put each piece of relevent info into variables
        print(row['Title'])
        title = row['Title']
        category = row['Category*'].strip()
        location = row['Location*'].strip()
        date = row['Start Date'].strip()
        startTime = row['Start Time'].strip()
        endTime = row['End Time'].strip()
        description = row['Description'].strip()

        # Using the other variables, create the form fill linke using urllib to parse the title and then dropping everything into place
        parsedTitle = parseURL.quote(title)
        link = 'https://fostercaretraining.org/registration/?course_email=aevans@afs4kids.org&course_title={parsedTitle}&course_date={date}&course_location={location}'.format(parsedTitle=parsedTitle, date=date, location=location)

        # Finally, create a bunch of html tags with the relevent data dropped in. I've also added lots of newline and tab characters.
        # While not actually necessary to the needs of the end user, I think they will non the less appreciate actually being able to read the output 
        print("""<h3>\n\t{title}\n</h3>\n<p>\n\t{category}<br>\n\t{location}<br>\n\t{date}<br>\n\t{startTime}-{endTime}\n</p>\n<p>\n\t{description}\n</p>\n<p>\n\t<a href=\"{link}\">\n\t\tRegister\n\t</a>\n</p>""".format(title=title, category=category, location=location, date=date, startTime=startTime, endTime=endTime, description=description, parsedTitle=parsedTitle, link=link))
        
        # Finally, we'll add some spacing and a line break in the terminal to seperate each chunck of copy/paste text
        print('\n-------------------------------------------------\n')