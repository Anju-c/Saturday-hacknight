
![django notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/2db31367-8f96-4e88-8a8d-a1a75936204d)


# Project Name Day_Planner
Purpose

The primary objective of this template is to facilitate the display, addition, and deletion of tasks (todos) within a user-friendly interface. This allows users to manage their tasks efficiently, ensuring a seamless experience in task management.

User Interaction

This template is designed to offer a user-friendly interface for managing tasks. It includes:

A form for adding new tasks, complete with fields for the task title, detailed description, and category selection.
Buttons for deleting existing tasks, providing users with the ability to manage their todo list effectively.
Main Features

Form for Adding Tasks:
Title Input: Users can input a title for their task, ensuring clarity and organization.
Description Textarea: A space for users to provide a detailed description of the task, offering context and clarity.
Category Selection: A dropdown list populated dynamically from the categories context variable, allowing users to categorize their tasks for better organization.
Submit Button: Users can submit the form to add a new task to the list, facilitating the addition of new tasks.
Display of Existing Tasks:
Task List: The template iterates over the todos context variable to display each task, ensuring all tasks are visible and accessible.
Task Details: For each task, it displays the title, description, and category, providing users with a comprehensive view of their tasks.
Delete Button: Each task has a delete button that, when clicked, submits a form to delete the task. A confirmation dialog is shown to prevent accidental deletions, enhancing user safety.
Security

CSRF Token: The template includes a CSRF token ({{ csrf_input }}) in both the add task form and the delete task form, as per Django's Jinja2 template backend. This is a crucial security measure to prevent cross-site request forgery attacks, ensuring the integrity and security of user data 2.
Styling and Layout

Inline Styling: The delete task form is styled with display: inline; to allow the delete button to appear next to the task details, enhancing the user interface.
Block Structure: The template uses Django's template language to define blocks ({% block content %}) and extends a base template, allowing for a consistent layout across different pages. This ensures a uniform look and feel across the application.
Additional Considerations

Dynamic Content: The template dynamically generates the category dropdown options and the list of existing tasks based on the context variables passed from the view (categories and todos). This ensures that the content is always up-to-date and relevant to the user.
User Experience: The use of a confirmation dialog for task deletion significantly improves the user experience by preventing accidental deletions, offering a safer and more intuitive interface.
Accessibility: The template utilizes semantic HTML elements (e.g., <label>, <textarea>) and includes for attributes for form controls, enhancing accessibility and ensuring that the application is usable by a wide range of users.

## Team members
1. [Mariya-saji](https://github.com/TH-Activities/saturday-hack-night-template)
2. [AshwinDen](https://github.com/TH-Activities/saturday-hack-night-template)

## How it Works ?

Base Template: The base.html template acts as a layout template, defining the overall structure of the page, including the header, footer, and navigation. It also defines blocks where specific content can be inserted.
Child Template: The provided template extends base.html and fills in the content block with the specific content for the Todo List page. This includes a form for adding tasks, a list of existing tasks, and a form for deleting tasks.
Context Variables: The view passes context variables (categories, todos) to the template. These variables are used to dynamically generate the HTML for the category dropdown and the list of tasks.
Form Submission: When the user submits the form to add a new task or delete an existing task, the form data is sent to the server. The view handles these requests, updating the database as necessary and redirecting the user back to the Todo List page.

# Libraries used
Library Name - Django 5.0.4
## How to configure


Base Template (base.html): This template serves as the foundational structure for the application, defining the layout that includes the header, footer, and navigation elements. It also establishes blocks, such as {% block content %}, where specific content can be dynamically inserted. This approach leverages Django's template inheritance feature, allowing for a consistent layout across different pages 1.

Child Template: The template for the Todo List page extends base.html, utilizing the {% extends "base.html" %} tag. This child template fills in the {% block content %} with the specific content for the Todo List page, which includes a form for adding tasks, a list of existing tasks, and a form for deleting tasks. This method of extending a base template ensures that common elements are reused, reducing redundancy and enhancing maintainability 1.

Context Variables: The view function responsible for rendering the Todo List page passes context variables (categories, todos) to the template. These variables are used within the template to dynamically generate the HTML for the category dropdown and the list of tasks. This dynamic content generation is a powerful feature of Django's template language, allowing for a more interactive and responsive user interface 2.

Form Submission: When a user submits the form to add a new task or delete an existing task, the form data is sent to the server. The view function handles these requests by processing the form data, updating the database accordingly, and then redirecting the user back to the Todo List page. This process is facilitated by Django's form handling capabilities, which include instantiating, processing, and rendering forms, as well as handling GET and POST requests 

## How to Run
Instructions for running

