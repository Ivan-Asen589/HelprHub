# HelprHub

**Connecting Hearts, Changing Lives**

HelprHub is a web platform that connects people with disabilities who need help with daily tasks to volunteers who want to make a difference. Receivers post requests for assistance, and helpers sign up to volunteer — building community one act of kindness at a time.

---

## Features

- **Dual-role system** — users register as either a *Helper* (volunteer) or *Receiver* (help-seeker)
- **Help request posts** — receivers create requests with title, description, date, time range, and location
- **Volunteer matching** — helpers browse available requests and sign up; one helper per request
- **Role-based dashboards** — separate dashboards for helpers (upcoming & past volunteering) and receivers (manage their posts)
- **Filtering** — helpers can filter requests by name, city, date, and availability
- **User profiles** — profile picture, bio, phone number, location, password change, account deletion
- **Email-based login** — authentication uses email instead of username

---

## Tech Stack

| Layer      | Technology                          |
|------------|-------------------------------------|
| Backend    | Django 6.0.3 (Python)               |
| Database   | SQLite3 (dev) / configurable        |
| Frontend   | Django Templates, HTML5, CSS3       |
| Icons      | Font Awesome 6                      |
| Phone      | django-phonenumber-field            |
| Production | Gunicorn + WhiteNoise               |
| Hosting    | Railway.app                         |

---

## Project Structure

```
HelprHub/
├── Backend/
│   ├── Backend/          # Django project config (settings, urls, main views)
│   ├── users/            # User model, auth, profile management
│   ├── posts/            # Help request posts (CRUD, filtering, volunteering)
│   ├── interactions/     # (In development)
│   ├── static/           # CSS stylesheets
│   └── templates/        # HTML templates
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/your-org/helprhub.git
cd helprhub/Backend

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## Usage

1. **Sign up** — choose your role (Helper or Receiver)
2. **Receivers** — go to your dashboard and create a help request with date, time, and location
3. **Helpers** — browse the request board, filter by city or date, and sign up for a task
4. **Track** — both roles have dashboards showing upcoming and past activity

---

## Live Demo

[https://helprhub-production.up.railway.app/](https://helprhub-production.up.railway.app/)

---

## Team

Built for **HackTUES 12** by team Tuhla.
