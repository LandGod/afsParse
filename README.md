## About
afsParse is an application written for a web marketing contractor in order to automate a specific routine task. The contractor is given a spreadsheet file, containing public event information, from which they must then copy and paste information onto an event page, using a website builder. The task is repetetive and always follows the same format. Thus, it was a perfect candidate for automation. 

** UPDATE: **
After implementing this program the client was able complete a task which previously took 20 to 30 minutes (and was very annoying) in about 5 minutes. By engineering the application to a tight specification and staying within a small scope, I was able to complete this application (including testing) in just a couple of hours. The client was happy with the low price, and the time savings allowed the program to pay for itslef in after a relatively small number of cycles. 

Note that many of the design desitions for the program were made due to the specific nature of the task. Where the circumstances different I would have liked to have made a more full-featured and comprehensive application. For example, it would have been simple enough to have the program generate html for the entire page. Unfortunatly, the necessity of using the client's website builder means that the html for each event must be inserted into the document seperately. Thus, the choice to ouput the data as seperate events. Additionally, due to project budget, no attempt was made to allow for input files of different formats, or any other sort of customization. Such things should not be necessary anyway since the information is always sent using the same template.

# Operation Instructions

### Before First Use
* In order to properly use this applicaiton, users must have some version of Python 3 installed on their machine. 
* It is also recomended that python is added to the user's PATH for easy operation of the program via command prompt. 
* It is further recomended that the user install a terminal applicaiton that allows easy copy/pasting of data, such as git BASH.

### Operation
1. Open the folder containing the afsParse.py application using the terminal of your choice. (If using git BASH, you can simply right click on the folder in the Windows Explorer and select 'Git Bash here from the dropdown menu.)
2. Type the following command: 'python afsParse.py`
3. If the csv file that you would like to use is in the same folder, you may supply the file name as an aditional argument. EG: 'python afsParse.py myfile.csv`
4. Whether or not you've supplied a file name, press enter.
5. If you did not supply a file name, you will be prompted to select the spreadsheet file you'd like to use via a file explorer GUI.
6. If the 'pyperclip' module is not installed on your machine, then the program will automatically install it before proceeding in order to allow the advanced clipboard features.
7. Results will be displayed in the terminal window where they can be copied. Additionally, all results will also be automatically coppied to your clipboard. If you prefer to copy/paste out of the terminal window, then you can just go ahead and do that. If you don't like doing that, then simply open a new, blank, text document, and click paste, which will paste in the entire output of the program (assuming you haven't coppied something else since running it).


For technical support please contact Daniel Gold - DanielJasonGold@gmail.com
