🌐 Awareness Campaign Hub
A Django-based web platform where users can create, explore, and join social awareness campaigns, empowering communities to participate in meaningful causes.

📖 Table of Contents

1.	Introduction
2.	Features
3.	Project Structure
4.	Installation
5.	Usage
6.	Tech Stack
7.	Methods & Architecture
8.	Dataset
9.	Key Outputs
10.	Results & Conclusion
11.	Future Improvements
12.	Troubleshooting
13.	Author

📌 Introduction

Awareness Campaign Hub is a simple yet impactful Django web application designed to promote social responsibility and community involvement.

Users can:

•	Register & log in

•	Create awareness campaigns

•	Browse ongoing initiatives

•	Join campaigns

•	Track social participation

The platform focuses on various societal issues, such as:

•	Environmental Protection
•	Mental Health
•	Hygiene & Healthcare
•	Education
•	Women Empowerment

✨ Features

•	🔐 User Authentication
        o	Register, log in, and manage sessions
•	📢 Create Awareness Campaigns
        o	Users can post new campaigns with relevant details
•	📄 Campaign Listing
        o	View all active campaigns in the community
•	🔍 Campaign Details
        o	Detailed view of each campaign
•	➕ Join Campaign
        o	Users can participate (duplicate joins prevented)
•	🎨 Responsive UI
        o	Clean Bootstrap-based interface


📁 Project Structure

AwarenessCampaignHub/
├── manage.py
├── db.sqlite3
├── campaign_app/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
└── AwarenessCampaignHub/
        ├── settings.py
        ├── urls.py
        └── wsgi.py


⚙ Installation

Follow these steps to run the project locally:

1️⃣ Clone the Repository
    git clone https://github.com/<your-username>/<repo-name>.git
    cd <repo-name>

2️⃣ Create Virtual Environment
    python -m venv env

3️⃣ Activate Environment Windows (PowerShell):
    .\env\Scripts\Activate.ps1

4️⃣ Install Requirements
    pip install -r requirements.txt

5️⃣ Apply Migrations
    python manage.py makemigrations
    python manage.py migrate

6️⃣ Start Development Server
    python manage.py runserver

7️⃣ View in Browser
    Open 👉 http://127.0.0.1:8000/


🧭 Usage

Once the server is running:

•	Visit the homepage
•	Register as a new user
•	Browse available campaigns
•	Create your own campaign
•	View campaign details
•	Join a campaign (one-time participation only)

🛠 Tech Stack

Technology	                 Purpose
Python 3	                 Core programming language
Django	                     Backend framework
SQLite3	                     Default lightweight database
HTML, CSS, Bootstrap	     UI design and styling
Git & GitHub	             Version control
Virtual Environment (venv)	 Dependency isolation


🔍 Methods & Architecture

•	Implemented Django MVT architecture
•	Created models for Campaign and Participation
•	Integrated Django Authentication for login/register/logout
•	Added CRUD functionality for campaign creation & listing
•	Enforced unique participation per user
•	Designed a modern, responsive UI using Bootstrap

📊 Dataset

No external dataset is used.
The application uses an internal SQLite database that dynamically stores:
•	User information
•	Campaign details
•	Participation records

📸 Key Outputs

✔ User Registration Page
✔ Login Page
✔ Create Campaign Page
✔ Campaign Listing Page
✔ Campaign Detail Page
✔ Join Campaign Feature


📌 Results & Conclusion

•	Successfully built a fully functional awareness campaign management system.
•	The platform is simple, intuitive, and user-friendly.
•	Increases community involvement through accessible campaign creation.
•	Encourages social contribution by centralizing awareness efforts.
This project demonstrates how a minimal system can make meaningful social impact.

🚀 Future Improvements

•	User dashboard for campaign insights
•	Comment/feedback section on campaigns
•	Campaign progress analytics
•	Social media sharing
•	Admin approval workflow
•	Email notifications

🩺 Troubleshooting

Issue	                                    Possible Fix
Virtual environment not activating	        Use PowerShell admin mode or correct activation path
ModuleNotFoundError	                        Ensure pip install -r requirements.txt completed
SQLite lock issues	                        Close other terminals/processes running the server
Static files not loading	                Run: python manage.py collectstatic (if in production)


👩‍💻 Author
Pallavi G
Developer of Awareness Campaign Hub (2025)
📧 Email: prathibhapallavi32@gmail.com
🌐 GitHub: https://github.com/PallaviG-13
