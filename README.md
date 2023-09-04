# Social Media API with Django REST Framework and JWT Authentication

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This is a RESTful API designed for building social media applications using Django REST Framework and JWT (JSON Web Token) authentication. It provides the essential endpoints and features needed to create a social media platform.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [User Authentication](#user-authentication)
  - [User Management](#user-management)
  - [Posts](#posts)
  - [Comments](#comments)
  - [Likes](#likes)
  - [Following/Followers](#followingfollowers)
- [Sample Requests](#sample-requests)
- [Contributing](#contributing)

## Features

- User registration and authentication with JWT tokens.
- User profile management, including profile picture and bio.
- Create, read, update, and delete posts.
- Comment on posts and manage your own comments.
- Like posts and view the list of users who liked a post.
- Follow and unfollow other users to build a personalized feed.

## Prerequisites

Before you start using the API, ensure you have the following prerequisites:

- Python 3.x
- Django 3.x
- Django REST Framework
- Other dependencies listed in the `requirements.txt` file.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/bhrayhaw/socialmediapi.git
   ```

2. Navigate to the project directory
   ```bash
   cd DRF
   ```
3. Install the required dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser to access the admin panel
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server
   ```bash
   python manage.py runserver
   ```
   The API will be available at http://localhost:8000/api/

## Usage

### User Authentication

- Use JWT tokens for user authentication. Obtain a token by logging in through the /api/user/login/ endpoint and include it in the Authorization header of your requests.

### User Management

- Create, read, update, and delete user profiles
- Change user profile picture and update bio

### Posts

- Create, read, update, and delete posts
- View posts created by other users
- Like and Unlike posts

### Comments

- Add comments to posts
- View and manage your comments
- Delete comments

### Likes

- Like and unlike posts
- View the list of users who liked your post

### Following/Followers

- Follow and Unfollow users
- View the list of followers
- View the list of those you are following

## Sample Request

You can navigate to the client_test directory in the root directory to test the api

```bash
cd DRF/client_test
```

## API Endpoints

- User Registration: `/api/user/register/` (POST)
- User Login: `/api/user/login/` (POST)
- User Profile: `/api/user/profile/` (GET, PUT, DELETE)
- Post List/Create: `/api/posts/` (GET, POST)
- Post Detail: `/api/posts/{post_id}/` (GET, PUT, DELETE)
- Comment List/Create: `/api/posts/{post_id}/comments/` (GET, POST)
- Comment Detail: `/api/posts/{post_id}/comments/{comment_id}/` (GET, PUT, DELETE)

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests to help improve this project.
