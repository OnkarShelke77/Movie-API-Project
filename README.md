# Movie-API-Project
Step-by-step summary of how I completed the project, along with a short description 
for each step: -

Step 1: Installation and Setup.
-Installed Python and ensured it's in my system path.
-Created a special workspace for the project.
-Installed Flask and necessary packages.

Step 2: Setting Up the Database
- Used SQLite for data Storage
- Made Flask connect to this database.
- Created a model class, "Movie," to define the structure of the database.
- 
Step 3: Writing the Code for the Movie Website.
- Made a list of things the website should do.
- Wrote the actual code to make those things happen in ‘app.py’ python file.
- Made sure the website can add, edit, delete, and show movies.
- Added helpful notes in the code to make it easy to understand.
- 
Step 4: API Endpoints
- Defined API endpoints for listing, adding, editing, and removing movies.
- Implemented routes for each endpoint using Flask.
- Utilized SQL Alchemy for database operations in the API endpoints.
- 
Step 5: - User Access Levels.
- Implemented user access levels: admin and user.
- Admins have privileges to add, edit, or remove movies.
- Users can only view movie listings.
- 
Step 6: Search Functionality.
- Implemented a search feature allowing users to find movies based on criteria.
- Used query parameters in the "/movies" endpoint for flexible searching.
- 
Step 7: Testing.
- Wrote unit tests using pytest to ensure API functionality.
- Tested each API endpoint for correct behavior.
- Verified that search functionality returns expected results.
Step 8: Deployment
- Ensured the app runs smoothly in a production environment.
- Kept the app running securely and efficiently.
In summary, I completed the project by setting up the development environment, designing 
the database, implementing API endpoints, managing user access, adding search 
functionality, documenting the code, conducting testing, and, if necessary, deploying the app 
for production use.
