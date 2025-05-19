# Alumni Management System

## Overview
The Alumni Management System is designed to connect alumni with their alma mater and fellow graduates. It provides a platform for networking, collaboration, and staying updated on university events and initiatives. This project includes a backend built with Flask and SQLite3, and a frontend consisting of HTML and CSS files.

## Structure

```
.
├── db
│   ├── alumni_dms.db
│   └── schema.sql
├── static
│   ├── css
│   │   └── main.css
│   ├── images
│   └── videos
├── templates
│   ├── about.html
│   ├── contact.html
│   ├── events.html
│   └── index.html
├── app.py
├── requirements.txt
└── README.md

```

## Backend
- **schema.sql**: Contains SQL commands to create the database and tables for the Alumni Management System, including alumni, events, event registrations, donations, feedback, and job postings tables with necessary foreign key relationships.
- **app.py**: The main application file that handles backend logic, connects to the SQLite3 database, executes queries, and serves data to the frontend. It includes routes for alumni, events, registrations, donations, feedback, and job postings.
- **requirements.txt**: Lists the Python dependencies required for the project, such as Flask for the web framework and SQLite3 for database interaction.

## Frontend

- **index.html**: HTML structure for the homepage (basically sign up page).
- **events.html**: HTML structure for the Events page, listing upcoming events and their details.
- **about.html**: HTML structure for the About page, providing information about the system and its mission.
- **contact.html**: HTML structure for the Contact page, including contact details for the Alumni Management System.
- **events.html**: HTML structure for the Events page, listing upcoming events and their details.
- **website.css**: CSS styles for the frontend pages, ensuring a consistent and modern design across the website.

## Setup Instructions

1. Clone the repository to your local machine.

2. Navigate to the `backend` directory and create a virtual environment:
   ```bash
   python3 -m venv myenv
   ```

3. Activate the virtual environment:
   - On Windows:
      ```
      myenv\Scripts\activate
      ```
   - On macOS/Linux:
     ```
     source myenv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Start the Flask application:
   ```
   python3 app.py
   ```

6. Open your web browser and navigate to `http://localhost:5000` to access the Alumni Management System.
