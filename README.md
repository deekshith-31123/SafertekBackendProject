# Django File Management Project

This Django project provides functionalities for file management, including creating, modifying, deleting, and retrieving files.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
   

2. Install the required dependencies:
      pip install django
   

3. Run the Django development server:
      python manage.py runserver
   

4. Access the application in your web browser at http://localhost:8000/.

## Project Structure

- create_file(request): Endpoint for creating a new file in the 'media' directory.
- get_files(request): Endpoint to retrieve a list of files in the 'media' directory.
- get_file(request, filename): Endpoint to get the content of a specific file.
- upload_file(request): View for rendering the file upload form.
- modify_file_view(request, filename): View for modifying the content of a file.
- file_modified(request): View for rendering the file modified confirmation page.
- delete_file(request, filename): Endpoint for deleting a file.

## Usage

1. Upload a File:
   - Access the upload file form at http://localhost:8000/upload_file/.
   - Provide a filename and content to upload a new file.

2. Modify a File:
   - Access the modify file form at http://localhost:8000/modify_file/<filename>/.
   - Enter new content and submit to modify an existing file.

3. Delete a File:
   - Use the endpoint http://localhost:8000/delete_file/<filename>/ to delete a file.

4. View Files:
   - Use the endpoint http://localhost:8000/get_files/ to get a list of available files.
   - Use the endpoint http://localhost:8000/get_file/<filename>/ to view the content of a specific file.
