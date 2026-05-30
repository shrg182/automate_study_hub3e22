# ATBS 3e Chapter Topics


## Chapter 0: INTRODUCTION

- Who Is This Book For?
- Coding Conventions Used in This Book
- What Is Programming?
- What Is Python?
- Common Myths About Programming
  - Programmers Don’t Need to Know Much Math
  - You Are Not Too Old to Learn Programming
  - AI Won’t Replace Programmers
- About This Book
- Downloading and Installing Python
- Downloading and Installing Mu
- Starting Mu
- Starting IDLE
- The Interactive Shell
- How to Find Help
- Asking Smart Programming Questions
- New to the Third Edition
- Summary

## Chapter 1: 1 PYTHON BASICS

- 1 PYTHON BASICS
  - Entering Expressions into the Interactive Shell
  - The Integer, Floating-Point, and String Data Types
  - String Concatenation and Replication
  - Storing Values in Variables
    - Assignment Statements
    - Variable Names
  - Your First Program
  - Dissecting the Program
    - Comments
    - The print() Function
    - The input() Function
    - The Greeting Message
    - The len() Function
    - The str(), int(), and float() Functions
    - The type() Function
    - The round() and abs() Functions
  - How Computers Store Data with Binary Numbers
  - Summary
  - Practice Questions

## Chapter 2: 2 IF-ELSE AND FLOW CONTROL

- 2 IF-ELSE AND FLOW CONTROL
  - Boolean Values
  - Comparison Operators
  - Boolean Operators
  - Mixing Boolean and Comparison Operators
  - Components of Flow Control
    - Conditions
    - Blocks of Code
    - Program Execution
  - Flow Control Statements
    - if
    - else
    - elif
  - A Short Program: Opposite Day
  - A Short Program: Dishonest Capacity Calculator
  - Summary
  - Practice Questions

## Chapter 3: 3 LOOPS

- 3 LOOPS
  - while Loop Statements
    - An Annoying while Loop
    - break Statements
    - continue Statements
  - for Loops and the range() Function
    - An Equivalent while Loop
    - Arguments to range()
  - Importing Modules
  - Ending a Program Early with sys.exit()
  - A Short Program: Guess the Number
  - A Short Program: Rock, Paper, Scissors
  - Summary
  - Practice Questions

## Chapter 4: 4 FUNCTIONS

- 4 FUNCTIONS
  - Creating Functions
  - Arguments and Parameters
  - Return Values and return Statements
  - The None Value
  - Named Parameters
  - The Call Stack
  - Local and Global Scopes
    - Scope Rules
      - Code That Is in the Global Scope Can’t Use Local Variables
      - Code That Is in a Local Scope Can’t Use Variables in Other Local Scopes
      - Code That Is in a Local Scope Can Use Global Variables
      - Local and Global Variables Can Have the Same Name
    - The global Statement
    - Scope Identification
  - Exception Handling
  - A Short Program: Zigzag
  - A Short Program: Spike
  - Summary
  - Practice Questions
  - Practice Programs
    - The Collatz Sequence
    - Input Validation

## Chapter 5: 5 DEBUGGING

- 5 DEBUGGING
  - Raising Exceptions
  - Assertions
  - Logging
    - The logging Module
    - Logfiles
    - A Poor Practice: Debugging with print()
    - Logging Levels
    - Disabled Logging
  - Mu’s Debugger
    - Debugging an Addition Program
    - Setting Breakpoints
  - Summary
  - Practice Questions
  - Practice Program: Debugging Coin Toss

## Chapter 6: 6 LISTS

- 6 LISTS
  - The List Data Type
    - Indexes
    - Negative Indexes
    - Slices
    - The len() Function
    - Value Updates
    - Concatenation and Replication
    - del Statements
  - Working with Lists
    - for Loops and Lists
    - The in and not in Operators
    - The Multiple Assignment Trick
    - List Item Enumeration
    - Random Selection and Ordering
  - Augmented Assignment Operators
  - Methods
    - Finding Values
    - Adding Values
    - Removing Values
    - Sorting Values
    - Reversing Values
  - Short-Circuiting Boolean Operators
  - A Short Program: Magic 8 Ball with a List
  - Sequence Data Types
    - Mutable and Immutable Data Types
    - The Tuple Data Type
    - List and Tuple Type Conversion
  - References
    - Arguments
    - The copy() and deepcopy() Functions
  - A Short Program: The Matrix Screensaver
  - Summary
  - Practice Questions
  - Practice Programs
    - Comma Code
    - Coin Flip Streaks

## Chapter 7: 7 DICTIONARIES AND STRUCTURING DATA

- 7 DICTIONARIES AND STRUCTURING DATA
  - The Dictionary Data Type
    - Comparing Dictionaries and Lists
    - Returning Keys and Values
    - Checking Whether a Key Exists
    - Setting Default Values
  - Model Real-World Things Using Data Structures
    - Step 1: Set Up the Program
    - Step 2: Create a Chessboard Template
    - Step 3: Print the Current Chessboard
    - Step 4: Manipulate the Chessboard
  - Nested Dictionaries and Lists
  - Summary
  - Practice Questions
  - Practice Programs
    - Chess Dictionary Validator
    - Fantasy Game Inventory
    - List-to-Dictionary Loot Conversion

## Chapter 8: 8 STRINGS AND TEXT EDITING

- 8 STRINGS AND TEXT EDITING
  - Working with Strings
    - String Literals
      - Double Quotes
      - Escape Sequences
      - Raw Strings
      - Multiline Strings
      - Multiline Comments
    - Indexes and Slices
    - The in and not in Operators
  - F-Strings
  - F-String Alternatives: %s and format()
  - Useful String Methods
    - Changing the Case
    - Checking String Characteristics
    - Checking the Start or End of a String
    - Joining and Splitting Strings
    - Justifying and Centering Text
    - Removing Whitespace
  - Numeric Code Points of Characters
  - Copying and Pasting Strings
    - Step 1: Copy and Paste from the Clipboard
    - Step 2: Separate the Lines of Text
    - Step 3: Join the Modified Lines
  - A Short Program: Pig Latin
  - Summary
  - Practice Questions
  - Practice Program: Table Printer

## Chapter 9: 9 TEXT PATTERN MATCHING WITH REGULAR EXPRESSIONS

- 9 TEXT PATTERN MATCHING WITH REGULAR EXPRESSIONS
  - Finding Text Patterns Without Regular Expressions
  - Finding Text Patterns with Regular Expressions
  - The Syntax of Regular Expressions
    - Grouping with Parentheses
    - Using Escape Characters
    - Matching Characters from Alternate Groups
    - Returning All Matches
  - Qualifier Syntax: What Characters to Match
    - Using Character Classes and Negative Character Classes
    - Using Shorthand Character Classes
    - Matching Everything with the Dot Character
    - Being Careful What You Match For
  - Quantifier Syntax: How Many Qualifiers to Match
    - Matching an Optional Pattern
    - Matching Zero or More Qualifiers
    - Matching One or More Qualifiers
    - Matching a Specific Number of Qualifiers
  - Greedy and Non-greedy Matching
    - Matching Everything
    - Matching Newline Characters
  - Matching at the Start and End of a String
  - Case-Insensitive Matching
  - Substituting Strings
  - Managing Complex Regexes with Verbose Mode
  - Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
    - Step 1: Create a Regex for Phone Numbers
    - Step 2: Create a Regex for Email Addresses
    - Step 3: Find All Matches in the Clipboard Text
    - Step 4: Join the Matches into a String
    - Ideas for Similar Programs
  - Humre: A Module for Human-Readable Regexes
  - Summary
  - Practice Questions
  - Practice Programs
    - Strong Password Detection
    - Regex Version of the strip() Method

## Chapter 10: 10 READING AND WRITING FILES

- 10 READING AND WRITING FILES
  - Files and Filepaths
    - Standardizing Path Separators
    - Joining Paths
    - Accessing the Current Working Directory
    - Accessing the Home Directory
    - Specifying Absolute vs. Relative Paths
    - Creating New Folders
    - Handling Absolute and Relative Paths
    - Getting the Parts of a Filepath
    - Finding File Sizes and Timestamps
    - Finding Files Using Glob Patterns
    - Checking Path Validity
  - The File Reading and Writing Process
    - Opening Files
    - Reading the Contents of Files
    - Writing to Files
    - Using with Statements
  - Saving Variables with the shelve Module
    - Step 1: Store the Quiz Data in a Dictionary
    - Step 2: Create the Quiz File
    - Step 3: Create the Answer Options
    - Step 4: Write the Content to the Files
  - Summary
  - Practice Questions
  - Practice Programs
    - Mad Libs
    - Regex Search

## Chapter 11: 11 ORGANIZING FILES

- 11 ORGANIZING FILES
  - The shutil Module
    - Copying Files and Folders
    - Moving and Renaming Files and Folders
    - Permanently Deleting Files and Folders
    - Deleting to the Recycle Bin
  - Walking a Directory Tree
  - Compressing Files with the zipfile Module
    - Creating and Adding to ZIP Files
    - Reading ZIP Files
    - Extracting from ZIP Files
    - Step 1: Figure Out the ZIP File’s Name
    - Step 2: Create the New ZIP File
    - Step 3: Walk the Directory Tree
    - Ideas for Other Programs
  - Summary
  - Practice Questions
  - Practice Programs
    - Selectively Copying
    - Deleting Unneeded Files
    - Renumbering Files
    - Converting Dates from American- to European-Style

## Chapter 12: 12 DESIGNING AND DEPLOYING COMMAND LINE PROGRAMS

- 12 DESIGNING AND DEPLOYING COMMAND LINE PROGRAMS
  - A Program by Any Other Name
  - Using the Terminal
    - The cd, pwd, dir, and ls Commands
    - The PATH Environment Variable
    - PATH Editing
      - Windows
      - macOS and Linux
    - The which and where Commands
  - Virtual Environments
  - Installing Python Packages with pip
  - Self-Aware Python Programs
  - Text-Based Program Design
    - Short Command Names
    - Command Line Arguments
    - Clipboard I/O
    - Colorful Text with Bext
    - Terminal Clearing
    - Sound and Text Notification
  - A Short Program: Snowstorm
  - Pop-up Message Boxes with PyMsgBox
  - Deploying Python Programs
    - Windows
    - macOS
    - Ubuntu Linux
  - A Short Program: Copying the Current Working Directory
    - Windows
    - macOS
    - Ubuntu Linux
  - A Short Program: Clipboard Recorder
    - Windows
    - macOS
    - Ubuntu Linux
  - Compiling Python Programs with PyInstaller
  - Summary
  - Practice Questions
  - Practice Program: Make Your Programs Deployable

## Chapter 13: 13 WEB SCRAPING

- 13 WEB SCRAPING
  - HTTP and HTTPS
    - Step 1: Figure Out the URL
    - Step 2: Handle the Command Line Arguments
    - Step 3: Retrieve the Clipboard Content
    - Ideas for Similar Programs
  - Downloading Files from the Web with the requests Module
    - Downloading Web Pages
    - Checking for Errors
    - Saving Downloaded Files to the Hard Drive
  - Accessing a Weather API
    - Requesting a Latitude and Longitude
    - Fetching the Current Weather
    - Getting a Weather Forecast
    - Exploring APIs
  - Understanding HTML
    - Exploring the Format
    - Viewing a Web Page’s Source
    - Opening Your Browser’s Developer Tools
    - Finding HTML Elements
  - Parsing HTML with Beautiful Soup
    - Creating a Beautiful Soup Object
    - Finding an Element
    - Getting Data from an Element’s Attributes
    - Step 1: Get the Search Page
    - Step 2: Find All Results
    - Step 3: Open Web Browsers for Each Result
    - Ideas for Similar Programs
    - Step 1: Design the Program
    - Step 2: Download the Web Page
    - Step 3: Find and Download the Comic Image
    - Step 4: Save the Image and Find the Previous Comic
    - Ideas for Similar Programs
  - Controlling the Browser with Selenium
    - Starting a Selenium-Controlled Browser
    - Clicking Browser Buttons
    - Finding Elements on the Page
    - Clicking Elements on the Page
    - Filling Out and Submitting Forms
    - Sending Special Keys
  - Controlling the Browser with Playwright
    - Starting a Playwright-Controlled Browser
    - Clicking Browser Buttons
    - Finding Elements on the Page
    - Clicking Elements on the Page
    - Filling Out and Submitting Forms
    - Sending Special Keys
  - Summary
  - Practice Questions
  - Practice Programs
    - Image Site Downloader
    - 2048
    - Link Verification

## Chapter 14: 14 EXCEL SPREADSHEETS

- 14 EXCEL SPREADSHEETS
  - Reading Excel Files
    - Opening a Workbook
    - Getting Sheets from the Workbook
    - Getting Cells from the Sheets
    - Converting Between Column Letters and Numbers
    - Getting Rows and Columns
    - Step 1: Read the Spreadsheet Data
    - Step 2: Populate the Data Structure
    - Step 3: Write the Results to a File
    - Ideas for Similar Programs
  - Writing Excel Documents
    - Creating and Saving Excel Files
    - Creating and Removing Sheets
    - Writing Values to Cells
    - Step 1: Set Up a Data Structure with the Updated Information
    - Step 2: Check All Rows and Update Incorrect Prices
    - Ideas for Similar Programs
  - Setting the Font Style of Cells
  - Formulas
  - Adjusting Rows and Columns
    - Setting Row Height and Column Width
    - Merging and Unmerging Cells
    - Freezing Panes
  - Charts
  - Summary
  - Practice Questions
  - Practice Programs
    - Multiplication Table Maker
    - Blank Row Inserter

## Chapter 15: 15 GOOGLE SHEETS

- 15 GOOGLE SHEETS
  - Installing and Setting Up EZSheets
    - Creating a New Google Cloud Project
    - Enabling the Sheets and Drive APIs
    - Configuring the OAuth Consent Screen
    - Creating Credentials
    - Logging In with the Credentials File
    - Revoking the Credentials File
  - Spreadsheet Objects
    - Creating, Uploading, and Listing Spreadsheets
    - Accessing Spreadsheet Attributes
    - Downloading and Uploading Spreadsheets
    - Deleting Spreadsheets
  - Sheet Objects
    - Reading and Writing Data
      - Addressing Columns and Rows
      - Reading and Writing Entire Columns and Rows
    - Creating, Moving, and Deleting Sheets
    - Copying Sheets
  - Google Forms
    - Step 1: Audit the Fake Blockchain
    - Step 2: Make Transactions
  - Working with Google Sheets Quotas
  - Summary
  - Practice Questions
  - Practice Programs
    - Downloading Google Forms Data
    - Converting Spreadsheets to Other Formats
    - Finding Mistakes in a Spreadsheet

## Chapter 16: 16 SQLITE DATABASES

- 16 SQLITE DATABASES
  - Spreadsheets vs. Databases
  - SQLite vs. Other SQL Databases
  - Creating Databases and Tables
    - Connecting to Databases
    - Creating Tables
    - Defining Data Types
    - Listing Tables and Columns
  - CRUD Database Operations
    - Inserting Data into the Database
      - Transactions
      - SQL Injection Attacks
    - Reading Data from the Database
      - Looping over Query Results
      - Filtering Retrieved Data
      - Ordering the Results
      - Limiting the Number of Results
      - Creating Indexes for Faster Data Reading
    - Updating Data in the Database
    - Deleting Data from the Database
  - Rolling Back Transactions
  - Backing Up Databases
  - Altering and Dropping Tables
  - Joining Multiple Tables with Foreign Keys
  - In-Memory Databases and Backups
  - Copying Databases
  - SQLite Apps
  - Summary
  - Practice Questions
  - Practice Programs
    - Cat Vaccination Checker
    - Meal Ingredients Database

## Chapter 17: 17 PDF AND WORD DOCUMENTS

- 17 PDF AND WORD DOCUMENTS
  - PDF Documents
    - Extracting Text
    - Post-Processing with AI
    - Extracting Images
    - Creating PDFs from Other Pages
      - Rotating Pages
      - Inserting Blank Pages
      - Adding Watermarks and Overlays
      - Encrypting and Decrypting PDFs
    - Step 1: Find All PDF Files
    - Step 2: Open Each PDF
    - Step 3: Save the Results
    - Ideas for Similar Programs
  - Word Documents
    - Reading Word Documents
    - Getting the Full Text from a .docx File
    - Styling Paragraph and Run Objects
    - Applying Run Attributes
    - Writing Word Documents
    - Adding Headings
    - Adding Line and Page Breaks
    - Adding Pictures
  - Summary
  - Practice Questions
  - Practice Programs
    - PDF Paranoia
    - Custom Invitations
    - PDF Password Breaker

## Chapter 18: 18 CSV, JSON, AND XML FILES

- 18 CSV, JSON, AND XML FILES
  - The CSV Format
    - Reading CSV Files
    - Accessing Data in a for Loop
    - Writing CSV Files
    - Using Tabs Instead of Commas
    - Handling Header Rows
    - Step 1: Loop Through Each File
    - Step 2: Read the File
    - Step 3: Write the New CSV File
    - Ideas for Similar Programs
  - Versatile Plaintext Formats
    - JSON
      - Reading JSON Data
      - Writing JSON Data
    - XML
      - Reading XML Files
      - Writing XML Files
  - Summary
  - Practice Questions
  - Practice Program: Excel-to-CSV Converter

## Chapter 19: 19 KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS

- 19 KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS
  - The time Module
    - Returning the Epoch Timestamp
    - Pausing Programs
    - Step 1: Set Up the Program to Track Times
    - Step 2: Track and Print Lap Times
    - Ideas for Similar Programs
  - The datetime Module
    - Representing Duration
    - Pausing Until a Specific Date
    - Converting datetime Objects into Strings
    - Converting Strings into datetime Objects
  - Launching Other Programs from Python
    - Passing Command Line Arguments to Processes
    - Receiving Output Text from Launched Commands
    - Running Task Scheduler, launchd, and cron
    - Opening Files with Default Applications
    - Step 1: Count Down
    - Step 2: Play the Sound File
    - Ideas for Similar Programs
  - Summary
  - Practice Questions
  - Practice Programs
    - Prettified Stopwatch
    - Friday the 13th Finder

## Chapter 20: 20 SENDING EMAIL, TEXTS, AND PUSH NOTIFICATIONS

- 20 SENDING EMAIL, TEXTS, AND PUSH NOTIFICATIONS
  - The Gmail API
    - Enabling the API
    - Sending Mail
    - Reading Mail
    - Searching for Mail
    - Downloading Attachments
  - SMS Email Gateways
  - Push Notifications
    - Sending Notifications
    - Transmitting Metadata
    - Receiving Notifications
  - Summary
  - Practice Questions
  - Practice Programs
    - Umbrella Reminder
    - Auto Unsubscriber
    - Email-Based Computer Control

## Chapter 21: 21 MAKING GRAPHS AND MANIPULATING IMAGES

- 21 MAKING GRAPHS AND MANIPULATING IMAGES
  - Computer Image Fundamentals
    - Colors and RGBA Values
    - Coordinates and Box Tuples
  - Manipulating Images with Pillow
    - Working with the Image Data Type
    - Cropping Images
    - Pasting Images onto Other Images
    - Resizing Images
    - Rotating and Flipping Images
    - Changing Individual Pixels
    - Step 1: Open the Logo Image
    - Step 2: Loop Over All Files
    - Step 3: Resize the Images
    - Step 4: Add the Logo and Save the Changes
    - Ideas for Similar Programs
  - Drawing on Images
    - Shapes
      - Points
      - Lines
      - Rectangles
      - Ellipses
      - Polygons
      - A Drawing Example
    - Text
  - Copying and Pasting Images to the Clipboard
  - Creating Graphs with Matplotlib
    - Line Graphs and Scatter Plots
    - Bar Graphs and Pie Charts
    - Additional Components
  - Summary
  - Practice Questions
  - Practice Programs
    - Tile Maker
    - Identifying Photo Folders on the Hard Drive
    - Creating Custom Seating Cards

## Chapter 22: 22 RECOGNIZING TEXT IN IMAGES

- 22 RECOGNIZING TEXT IN IMAGES
  - Installing Tesseract and PyTesseract
    - Windows
    - macOS
    - Linux
    - PyTesseract
  - OCR Fundamentals
    - Preprocessing an Image
    - Fixing Mistakes Using Large Language Models
  - Recognizing Text in Non-English Languages
  - The NAPS2 Scanner Application
    - Installing and Setting Up NAPS2
    - Running NAPS2 from Python
    - Specifying Input
  - Summary
  - Practice Questions
  - Practice Program: Browser Text Scraper

## Chapter 23: 23 CONTROLLING THE KEYBOARD AND MOUSE

- 23 CONTROLLING THE KEYBOARD AND MOUSE
  - Setting Up Accessibility Apps on macOS
  - Staying on Track
    - Pauses and Fail-Safes
    - Logouts
  - Controlling Mouse Movement
    - Moving the Mouse
    - Getting the Current Position
  - Controlling Mouse Interaction
    - Clicking
    - Dragging
    - Scrolling
  - Planning Your Mouse Movements
  - Taking Screenshots
  - Image Recognition
  - Getting Window Information
    - Obtaining the Active Window
    - Finding Windows with Other Functions
    - Manipulating Windows
  - Controlling the Keyboard
    - Sending Key Press Strings
    - Specifying Key Names
    - Pressing and Releasing the Keyboard
    - Running Hotkey Combinations
  - Setting Up GUI Automation Scripts
  - Displaying Message Boxes
  - Summary
  - Practice Questions
  - Practice Programs
    - Looking Busy
    - Reading Text Fields with the Clipboard
    - Writing a Game-Playing Bot

## Chapter 24: 24 TEXT-TO-SPEECH AND SPEECH RECOGNITION ENGINES

- 24 TEXT-TO-SPEECH AND SPEECH RECOGNITION ENGINES
  - Text-to-Speech Engine
    - Generating Speech
    - Saving Speech Audio to WAV Files
  - Speech Recognition
  - Creating Subtitle Files
  - Downloading Videos from Websites
  - Summary
  - Practice Questions
  - Practice Programs
    - Adding Voice to Guess the Number
    - Singing “99 Bottles of Beer”
    - YouTube Transcriber

**Displayed topic items:** 649
