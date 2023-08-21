# Django Profile Management System

This project is a simple web application built using the Django framework for managing user profiles. It allows users to create, view, update, and delete profiles. The project includes functionalities such as uploading profile images, searching for profiles, and editing profile details.

## Features

- **Create Profile**: Users can create a new profile by providing their name, email, age, image, address, phone number, date of birth, gender, and religion. They can optionally upload a profile image.

- **View Profiles**: Users can view a list of all profiles stored in the database. They can also search for specific profiles by name.

- **View Profile Details**: Users can click on a profile to view its details, including all the information provided during profile creation.

- **Update Profile**: Users can edit and update profile information. They can modify all the details provided during profile creation, including uploading a new profile image.

- **Delete Profile**: Users can delete a profile. If a profile had an uploaded image, the image file is also removed from the server.

## Project Structure

- `models.py`: Defines the `Profile` model with fields for various profile attributes such as name, email, age, image, address, phone number, date of birth, gender, and religion.

- `views.py`: Contains view functions for different actions:
  - `create`: Handles profile creation based on user input, including uploading an image if provided.
  - `home`: Displays a list of profiles or search results if a search query is provided.
  - `SEE_PROF`: Displays detailed information about a specific profile.
  - `update`: Allows users to edit and update profile details, including uploading a new image.
  - `delete`: Handles the deletion of a profile and its associated image file (if applicable).

- `templates/`: Contains HTML templates for rendering different pages:
  - `create.html`: Form for creating a new profile.
  - `home.html`: Displays a list of profiles or search results.
  - `seeProfile.html`: Displays detailed information about a profile.
  - `update.html`: Form for updating profile details.

## Usage

1. Install the required dependencies using `pip install -r requirements.txt`.

2. Set up the Django project and database configurations.

3. Run migrations using `python manage.py makemigrations` and `python manage.py migrate`.

4. Start the development server using `python manage.py runserver`.

5. Access the application through a web browser at `http://127.0.0.1:8000/`.

## Notes

- The project assumes that the default profile image is named `def.png`.
- Profile images are stored in the `media` directory.
- Remember to secure your Django project in production environments.

## Contributing

Contributions to this project are welcome. Feel free to fork the repository, make improvements, and submit pull requests.


---

