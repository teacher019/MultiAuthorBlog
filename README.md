# Multi-Author Blogging Platform

A backend-focused **Multi-Author Blogging Platform** built with **Python and Django**.

The platform allows visitors to browse published blog posts, registered readers to comment and like posts, and approved authors to create, edit, and manage their own blog posts. Site administrators can manage users, authors, posts, categories, tags, comments, and other platform data through the Django Admin panel.

---

## Features

### User Authentication & Roles

* User registration / Sign up
* User login
* Secure logout
* Django's built-in authentication system
* Passwords securely hashed by Django
* Every registered user starts as a Reader
* Admin can promote a Reader to Author
* Approved Authors can create, edit, and delete their own posts
* Authors cannot edit or delete another author's posts
* Separate Django Admin / Superuser access

### Category & Tag Management

* Category model for blog posts
* Each post belongs to one category
* Tag model with Many-to-Many relationship
* Posts can have multiple tags
* Categories and tags can be managed through Django Admin

### Blog Posts

Each post supports:

* Title
* Automatically generated unique slug
* Content
* Featured image
* Category
* Multiple tags
* Author
* Draft / Published status
* View count
* Created date
* Updated date

Authors can:

* Create posts
* Edit their own posts
* Delete their own posts
* Save posts as Draft
* Publish posts

Draft posts are not displayed publicly.

### Homepage & Post Listing

* Published posts displayed on the homepage
* Newest posts displayed first
* Pagination
* Featured images
* Post title
* Author
* Category
* Short content excerpt
* Category filtering
* Tag filtering
* Case-insensitive search by title or content

### Post Detail

Each published post has a detail page containing:

* Full post content
* Featured image
* Author
* Category
* Tags
* Published date
* Total view count
* Total like count
* Comments

The post view count is incremented when the detail page is opened.

### Comment System

* Only authenticated users can submit comments
* Anonymous users are redirected to login
* Comments store:

  * User
  * Post
  * Comment text
  * Created date
* Comments are displayed on the post detail page
* Users can delete their own comments
* Authors can moderate comments on their posts
* Site administrators can delete any comment

### Like System

* Only authenticated users can like posts
* A user cannot like the same post more than once
* Like / Unlike toggle functionality
* Total like count displayed on post detail pages

### Author Dashboard

Approved authors have access to a personal dashboard showing:

* Total posts
* Published posts
* Draft posts
* Total views
* Their own posts
* Post status
* Category
* View count
* Create post link
* Edit post link
* Delete post link

Authors can only manage their own posts.

### Author Public Profile

The platform supports an author profile page where visitors can view an author's published posts.

### Django Admin

The administrator can manage:

* Users
* Author profiles
* Categories
* Tags
* Posts
* Comments
* Likes

The administrator can also promote or revoke Author status through the administration interface.

---

## Technology Stack

* **Python 3**
* **Django**
* **SQLite**
* **HTML5**
* **Django Templates**
* **Pillow** for image handling
* **python-dotenv** for environment configuration

---

## Project Structure

```text
MultiAuthorBlog/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── author_dashboard.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── post_confirm_delete.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       └── signup.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── posts/
│   └── design01.jpg
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Requirements

Before running the project, make sure the following are installed:

* Python 3.x
* pip
* Git
* A web browser

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/teacher019/MultiAuthorBlog.git
```

Move into the project directory:

```bash
cd MultiAuthorBlog
```

---

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell execution policy prevents activation, you can also use:

```powershell
venv\Scripts\activate
```

---

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## Environment Configuration

The project uses environment variables for configuration.

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

A `.env.example` file is included in the repository to show the required environment variables.

### Important

Do **not** commit your real `.env` file to GitHub.

The `.env` file should remain private.

---

## Database Setup

Run Django migrations:

```powershell
python manage.py migrate
```

Create a superuser for Django Admin:

```powershell
python manage.py createsuperuser
```

Follow the prompts to enter:

* Username
* Email address
* Password

---

## Run the Development Server

Start the Django development server:

```powershell
python manage.py runserver
```

Open the website in your browser:

```text
http://127.0.0.1:8000/
```

---

## Django Admin

Open:

```text
http://127.0.0.1:8000/admin/
```

Log in using the superuser account created with:

```powershell
python manage.py createsuperuser
```

From the Admin panel, the site administrator can manage users, authors, posts, categories, tags, comments, and likes.

---

## User Workflow

### Reader

A newly registered user is a Reader by default.

Readers can:

1. Register
2. Log in
3. Browse published posts
4. Search posts
5. Filter by category or tag
6. Like posts
7. Unlike posts
8. Submit comments
9. Delete their own comments

---

### Author

An administrator can promote a Reader to Author.

An approved Author can:

1. Log in
2. Open the Author Dashboard
3. Create a new post
4. Upload a featured image
5. Select a category
6. Add tags
7. Save as Draft or Published
8. Edit their own posts
9. Delete their own posts
10. View basic post analytics

Authors cannot modify another author's posts.

---

### Administrator

The site administrator uses a separate Django Superuser account.

The administrator can:

* Manage users
* Promote users to Author
* Revoke Author status
* Manage categories
* Manage tags
* Manage all posts
* Manage comments
* Moderate platform content

---

## Media & Static Files

Featured images are handled using Django's media configuration.

The project uses Django's:

```python
MEDIA_ROOT
MEDIA_URL
```

configuration for uploaded images.

During development, uploaded media is served using Django's `static()` helper.

---

## Security

The project uses Django's built-in authentication system.

Security-related practices include:

* Password hashing through Django authentication
* Environment variables for sensitive configuration
* `.env` excluded from Git
* Role-based access control
* Author ownership checks
* Protected create/edit/delete operations
* Authentication required for comments and likes

---

## Dependencies

Project dependencies are listed in:

```text
requirements.txt
```

Install them with:

```powershell
pip install -r requirements.txt
```

---

## Testing

Run Django's system check:

```powershell
python manage.py check
```

Expected result:

```text
System check identified no issues (0 silenced).
```

Check migrations:

```powershell
python manage.py makemigrations
python manage.py migrate
```

---

## Main URLs

| Page             | URL                                 |
| ---------------- | ----------------------------------- |
| Homepage         | `/`                                 |
| Signup           | `/signup/`                          |
| Login            | `/login/`                           |
| Logout           | `/logout/`                          |
| Author Dashboard | `/author/dashboard/`                |
| Create Post      | `/post/create/`                     |
| Post Detail      | `/post/<slug>/`                     |
| Add Comment      | `/post/<slug>/comment/`             |
| Like / Unlike    | `/post/<slug>/like/`                |
| Edit Post        | `/dashboard/post/<post_id>/edit/`   |
| Delete Post      | `/dashboard/post/<post_id>/delete/` |
| Django Admin     | `/admin/`                           |

---

## Assignment Requirements Checklist

| Requirement                 | Status |
| --------------------------- | ------ |
| User Registration           | ✅      |
| User Login                  | ✅      |
| Secure Logout               | ✅      |
| Secure Password Storage     | ✅      |
| Reader Role                 | ✅      |
| Approved Author System      | ✅      |
| Author Dashboard            | ✅      |
| Author Ownership Protection | ✅      |
| Category Management         | ✅      |
| Tag Management              | ✅      |
| Blog Post Model             | ✅      |
| Unique Auto-generated Slug  | ✅      |
| Featured Image              | ✅      |
| Draft / Published Status    | ✅      |
| Draft Visibility Protection | ✅      |
| Homepage                    | ✅      |
| Pagination                  | ✅      |
| Category Filtering          | ✅      |
| Tag Filtering               | ✅      |
| Search                      | ✅      |
| Post Detail Page            | ✅      |
| View Count                  | ✅      |
| Comment System              | ✅      |
| Comment Moderation          | ✅      |
| Like System                 | ✅      |
| Like / Unlike Toggle        | ✅      |
| Unique User/Post Like       | ✅      |
| Django Admin                | ✅      |
| Author Public Profile       | ✅      |
| Template-based Frontend     | ✅      |
| `requirements.txt`          | ✅      |
| `.env.example`              | ✅      |
| `.gitignore`                | ✅      |
| README Documentation        | ✅      |

---

## GitHub Repository

**Repository:**
https://github.com/teacher019/MultiAuthorBlog

---

## Local Development

Quick start:

```powershell
git clone https://github.com/teacher019/MultiAuthorBlog.git
cd MultiAuthorBlog
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then visit:

```text
http://127.0.0.1:8000/
```

---

## Author

**Abdul Khalek**

Multi-Author Blogging Platform
Built with Python and Django.

---

## License

This project was created as an educational Django assignment.
