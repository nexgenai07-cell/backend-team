# Django Backend Integration Task

## Overview
This project is a backend-focused Django application developed as part of a backend integration assessment.
The project demonstrates integration with multiple third-party services including Cloudinary, EmailJS, Google Gemini AI, Stripe, and PostgreSQL. All functionality is managed through Django Admin without any frontend implementation.
---
## Features
### User Management
- Create users through Django Admin
- Store user information including:
  - Name
  - Email
  - Profile Image
---
### Cloudinary Integration
- Cloudinary configured as media storage
- Profile images uploaded through Django Admin
- Images stored on Cloudinary
- Cloudinary URLs generated automatically
---
### Email Integration (EmailJS)
- Welcome email sent automatically when a new user is created
- EmailJS service integration
- Error handling and logging implemented
---
### Gemini AI Integration
#### AIRequest Model
Stores:
- Prompt
- Response
- Created At
#### Functionality
- Automatically sends prompt to Gemini AI
- Stores generated response in database
- Handles API failures gracefully
---
### Stripe Payment Integration
#### Payment Model
Stores:
- User
- Amount
- Stripe Payment Intent ID
- Status
- Created At
#### Functionality
- Stripe Test Mode enabled
- Payment Intent created automatically
- Payment status stored in database
- Error handling implemented
---
### PostgreSQL Database
- PostgreSQL used as primary database
- Django migrations applied successfully
- All project data stored in PostgreSQL
---
## Tech Stack
| Technology | Purpose |
|------------|----------|
| Django 5.2 | Backend Framework |
| PostgreSQL | Database |
| Cloudinary | Media Storage |
| EmailJS | Email Service |
| Google Gemini AI | AI Response Generation |
| Stripe | Payment Processing |
| Python Decouple | Environment Variables |
---

## Project Structure

```text
backend_task/
│
├── backend_task/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── users/
│   ├── models.py
│   ├── admin.py
│   ├── signals.py
│   ├── apps.py
│   ├── gemini_service.py
│   └── migrations/
│
├── .env
├── requirements.txt
├── README.md
└── manage.py
```
---

## Environment Variables

Create a `.env` file in the project root.

```env
# Cloudinary
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Gemini
GEMINI_API_KEY=your_gemini_api_key

# EmailJS
EMAILJS_SERVICE_ID=your_service_id
EMAILJS_TEMPLATE_ID=your_template_id
EMAILJS_PUBLIC_KEY=your_public_key
EMAILJS_PRIVATE_KEY=your_private_key

# Stripe
STRIPE_SECRET_KEY=your_stripe_secret_key
```
---

## Installation

### 1. Clone Repository

```bash
git clone <repository_url>
cd backend_task
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```
---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```
---

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

---

### 7. Run Server

```bash
python manage.py runserver
```

---

## Admin Access

Open:

```text
http://127.0.0.1:8000/admin/
```
Login using the superuser credentials.
---
## Testing Summary
### User Module
✔ User creation through Django Admin
### Cloudinary
✔ Profile image uploaded successfully
✔ Image stored on Cloudinary
### EmailJS
✔ Welcome email triggered on user creation
### Gemini AI
✔ Prompt processed successfully
✔ Response stored automatically
### Stripe
✔ Payment Intent generated successfully
✔ Stripe Payment ID stored in database
### PostgreSQL
✔ Database tables created successfully
✔ Data persisted correctly
---
## Error Handling Implemented
### EmailJS
- API failure handling
- Logging support
### Gemini
- API exception handling
- Graceful response fallback
### Stripe
- Payment Intent failure handling
- Status management
---
## Assumptions
- Stripe is configured in Test Mode.
- Cloudinary account is active.
- Gemini API key has access to supported Gemini models.
- EmailJS service and template are configured correctly.

---

## Known Limitations

- No frontend implementation included.
- Payments are created in Stripe Test Mode only.
- Email delivery depends on EmailJS configuration.

---
