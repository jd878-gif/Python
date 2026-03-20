# Python

📚 Library Management System
A simple console-based Library Management System built in Python that manages two core entities — Books and Members — with support for essential data operations via an interactive menu.

📌 Features
The system supports the following operations on both Books and Members:
OperationDescription🔍 SearchLook up a book or member by their unique ID➕ InsertAdd a new book or member to the system❌ DeleteRemove an existing book or member from the system

🗂️ Entities
📖 Book
FieldTypeDescriptionisbn_nointUnique identifier for the booktitlestrTitle of the bookauthorstrAuthor's namepublisherstrPublisher's nameyears_of_publicationintYear the book was published
👤 Member
FieldTypeDescriptionmember_idintUnique identifier for the membernamestrMember's full nameageintMember's ageemailstrMember's email addressyears_of_experienceintYears of experience

⚙️ How It Works
The program runs two interactive menu loops — one for Books and one for Members.
📖 Book Menu
Hit 1 → Search Book   (by ISBN number)
Hit 2 → Insert Book   (enter details interactively)
Hit 3 → Delete Book   (by ISBN number)
Hit 4 → Exit
👤 Member Menu
Hit a → Search Member   (by Member ID)
Hit b → Insert Member   (enter details interactively)
Hit c → Delete Member   (by Member ID)
Hit d → Exit

🚀 Getting Started
Prerequisites

Python 3.x

# Navigate to the project directory
cd library-management-system
Running the Project
bashpython library.py

📁 Project Structure
library-management-system/
│
├── library.py      # Single file containing all logic for Books and Members
└── README.md       # Project documentation

All operations for both Books and Members are implemented in a single file.


🛠️ Tech Stack

Language: Python 3
Storage: In-memory (Python lists of dictionaries)


🔮 Future Improvements

Split Books and Members into separate modules/files
Add file or database persistence (e.g., JSON, SQLite)
Add input validation and error handling improvements
Build a GUI or web interface


📄 License
This project is open-source and available under the MIT License.

🙋‍♂️ Author
Jeet Dave
https://github.com/jd878-gif/
