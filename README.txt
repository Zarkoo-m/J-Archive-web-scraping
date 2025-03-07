
📦 Automated Web Scraping for Jeopardy Archive
End-to-End Data Extraction – Featuring Keyword-Based Search, Data Analysis & Report Generation.

-----------------------------------------------------------------------------------------------
📌 MAIN DESCRIPTION
✅ Object-Oriented Functions
🔹 Each step in script has a separate object-oriented function, ensuring modularity, code reusability, and maintainability.

✅ Modular Design
🔹 The script is modular, making it easy to maintain, structured, and flexible for  multiple scraping choices.

✅ Folder Separation
🔹 Functions and fields are well-organized in separate files, categorized into folders based on web site sections - steps for clear navigation.

-----------------------------------------------------------------------------------------------
📚 LIBRARIES & DEPENDENCIES
🔹 Built-in Python Libraries
✔️ os – File and directory operations
✔️ re – Regular expressions for text processing
✔️ time – Execution timing and delays
✔️ csv – Structured data storage and handling
✔️ collections – Data structuring and frequency analysis
✔️ datetime – Date and time manipulation
✔️ threading – Parallel execution for optimized performance

🔹 Web Scraping & Automation
✔️ BeautifulSoup – Parsing and extracting HTML content
✔️ WebDriverWait – Handling dynamic elements
✔️ EC (Expected Conditions) – Ensuring stable element interactions
✔️ By – Locating elements for automation
✔️ ActionChains – Handling advanced browser interactions

🔹 Data Storage & Reporting
✔️ Workbook – Excel file generation
✔️ ExcelChartGenerator – Automated chart creation
✔️ BarChart, Reference – Graph plotting for statistical analysis
-----------------------------------------------------------------------------------------------
⚙️ MAIN FEATURES

✅ Web Scraping & Data Extraction
🔹 Automated Scraping – Uses BeautifulSoup to parse and extract structured data from J-Archive.
🔹 Dynamic Search Processing – Extracts results based on user-provided keywords, enabling targeted data collection.
🔹 Pagination Handling – Iterates through multiple search result pages to ensure comprehensive data extraction.

✅ Repeat Mechanism
🔹 Automated Retry Logic – Implemented a custom function that attempts each step up to 3 times if the initial execution fails.
🔹 Error Resilience – Ensures the script does not terminate unexpectedly due to temporary issues like network delays, missing elements, or slow page loading.
🔹 Adaptive Recovery – If a step fails, the function waits before retrying, improving script stability and preventing unnecessary failures.
🔹 Execution Continuity – Guarantees smooth operation by handling transient errors dynamically instead of stopping execution immediately.

✅ Centralized & Decentralized Data Storage
🔹 Binary Data Storage – Saves extracted information in binary format to enhance data integrity and retrieval speed.
🔹 Structured Data Organization – Implements centralized and decentralized storage strategies to improve data access and processing efficiency.
🔹 Optimized Querying – Enables fast searching and sorting within stored datasets.

✅ Reports & Data Visualization
🔹 Excel Report Generation – Exports processed data into an Excel file, featuring structured tables and summaries.
🔹 Graphical Data Representation – Integrates bar charts into Excel reports for visual data interpretation (TOP 30 - most frequently repeated results).
🔹 HTML Report Creation – Generates clean and structured HTML reports for easy data presentation.

✅ Cache Management
🔹 Cache Clearing Before Execution – Removes temporary files and stored session data to prevent conflicts and outdated results.
🔹 Performance Optimization – Ensures that the script operates in a clean state for each execution cycle.

✅ Logging & Debugging
🔹 Event Logging System – Captures key events and errors, allowing for easy debugging and performance tracking.
🔹 Execution Monitoring – Logs each step of the script to provide visibility into data processing.
🔹 Detailed Error Tracking – Stores exception details for troubleshooting and issue resolution.

✅ Exception Handling & Stability
🔹 Try-Except Blocks – Ensures graceful error handling, preventing script crashes and allowing smooth execution.
🔹 Custom Error Messages – Provides clear debugging outputs to help identify and resolve issues efficiently.
🔹 Resilient Execution – Handles missing elements, unexpected response delays, and incorrect page structures.

✅ Data Analysis & Sorting
🔹 Keyword-Based Data Filtering – Sorts clues, answers, and categories based on frequency of occurrence.
🔹 Statistical Processing – Identifies patterns in Jeopardy game data, enabling deeper insights.
🔹 Optimized Sorting Mechanism – Sorts data efficiently to highlight the most relevant and frequently appearing terms.

✅ HTML Content Cleaning
🔹 Data Sanitization – Removes unnecessary HTML tags and artifacts to extract clean text from parsed data.
🔹 Format Optimization – Ensures extracted data is properly structured for storage, analysis, and reporting.
🔹 Error-Free Data Extraction – Cleans HTML noise to prevent issues with inconsistent or malformed content.
-----------------------------------------------------------------------------------------------
🛠  HOW IT WORKS

1️⃣ Cache Memory Clearing – Frees up system resources and ensures a fresh session start.
2️⃣ Opening the Website – Automatically loads the main page of the J-Archive site.
3️⃣ Keyword Entry – The user enters a search term.
4️⃣ Search Execution – The keyword is entered into the site's search bar, and the search is initiated.
5️⃣ Collecting Results – Automatically extracts all results where the keyword appears.
6️⃣ Selecting the Number of Results – The user chooses whether to process all results or a custom number.
7️⃣ Opening Results – Opens each result and counts how many rounds were played in the game.
8️⃣ Data Extraction – Extracts clue, answer, and category from each round of every game.
9️⃣ Data Storage – Collected data is stored in binary format for optimization and faster access.
🔟 Categorized Data Collection – All answers and clues are grouped into a list according to their categories.
1️⃣1️⃣ Data Analysis & Sorting – Performs analysis and sorting based on the most frequently appearing clues, answers, and categories.
1️⃣2️⃣ User Prompt for Continuation – The script offers the option to enter a new keyword or exit the program.
1️⃣3️⃣ Report Generation – Analyzed results are exported to Excel (with charts) and an HTML report with structured tables.


---

## 📂 **PROJECT STRUCTURE**

```plaintext
📁 j-archive
│── 📁 A_DRIVERS                                                                          
│   ├──A_1_DRIVER_SETUP.py 
│
│── 📁 B_FUNCTIONS                                                                        
│   ├── B_1_OPEN_WEB_SITE.py
│   ├── B_2_OPEN_MAIN_PAGE.py
│   ├── B_3_SEARCH_ENTRY.py
│   ├── B_4_RESULT_SCANNER.py
│   ├── B_5_SEPARATE_GAME.py
│   ├── B_6_ANALYSIS.py
│   ├── B_7_REPEAT_PROCESS.py
│
│── 📁 C_SUPPORTING_FILES                                                                
│   ├── C_1_LOGS.py
│   ├── C_2_EXCEPTION_HANDLERS.py
│   ├── C_3_CLEAR_CACHE_MEMORY.py
│   ├── C_4_REPEAT_MECHANISM.py
│
│── 📁 D_HELPERS                                                                
│   ├── D_1_USER_INPUT_1.py
│   ├── D_2_HTML_CLEARNER.py
│   ├── D_3_CONVERT_TO_BINARY.py
│   ├── D_4_USER_INPUT2_CHOICE.py
│   ├── D_5_CSV_SAVER.py
│   ├── D_6__CONVERT_TO_BINARY2.py
│   ├── D_7_EXCEL_REPORT.py
│   ├── D_8_EXCEL_CHART.py
│   ├── D_9_HTML_REPORT.py
│
│── 🖥️ Main.py        










