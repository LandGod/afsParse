import re  # Regular expression library, possibly not needed.
import csv  # CSV Parsing Library
import urllib.parse as parseURL # For formatting data when constructing the url. Will use urllib.parse.quote()
import sys  # So I can grab command line arguments for the file name.

try:
    import pyperclip  # For outputting data to the clipboard 
except(ModuleNotFoundError):
    import subprocess
    def install(package):
        subprocess.call([sys.executable, "-m", "pip", "install", package])
    print('Installing Pyperclip... Please wait...')
    install('pyperclip')
    import pyperclip


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
if filename[-4:] != '.csv':
    raise TypeError('Incorrect file type! Filetype must be: .csv')

# Open csv file called test.csv and create a dictionary of data based off of the given field names
# Note that each Field name entry will include all cells up and down from the title, inclusive of the title, until the end of the document, so 
# we must take care to ignore data we don't need
with open(filename, newline='') as csvfile:

    # Generate csv dictionary for each row based on supplied column headings. Returns iterable full of dictionaries. 
    reader = csv.DictReader(csvfile, fieldnames=['Category*','Title','Description', 'CEUs', 'Start Date', 'End Date', 'Start Time', 'End Time', 'Location*', 'Sponsoring Agency*'])


    allResults =''

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
        # We'll also throw in a line break between each set of event html tags so they can be easily distinguished from eachother
        print("""<h3>\n\t{title}\n</h3>\n<p>\n\t{category}<br>\n\t{location}<br>\n\t{date}<br>\n\t{startTime} - {endTime}\n</p>\n<p>\n\t{description}\n</p>\n<p>\n\t<a href=\"{link}\">Register</a>\n</p>""".format(title=title, category=category, location=location, date=date, startTime=startTime, endTime=endTime, description=description, parsedTitle=parsedTitle, link=link))
        print('\n-------------------------------------------------\n')

        # We'll also add the same thing to our allResults string so that we can output everything to the clipboard at once.
        # Not that for this, we're swapping all of our \n characters for \r\n, so that if this gets pasted into notepad the newlines are actually recognized.
        # That wasn't necessary for the terminal output as \n should be recognized there.
        allResults += """<h3>\r\n\t{title}\r\n</h3>\r\n<p>\r\n\t{category}<br>\r\n\t{location}<br>\r\n\t{date}<br>\r\n\t{startTime} - {endTime}\r\n</p>\r\n<p>\r\n\t{description}\r\n</p>\r\n<p>\r\n\t<a href=\"{link}\">Register</a>\r\n</p>""".format(title=title, category=category, location=location, date=date, startTime=startTime, endTime=endTime, description=description, parsedTitle=parsedTitle, link=link)
        allResults += '\r\n-------------------------------------------------\r\n'
        
    
    # Once we're done, copy all data to the clipboard using pyperclip
    pyperclip.copy(allResults)