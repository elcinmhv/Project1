{% extends 'base.html' %}
{% load static %}

{% block title %}Registration Form{% endblock %}

{% block content %}
<style>
    body {
        background-image: url('{% static 'background.jpg' %}');
        background-size: cover;
        font-family: Arial, sans-serif;
        color: #333;
    }

    .container {
        padding-top: 50px;
    }

    .registration-form {
        background-color: rgba(255, 255, 255, 0.8);
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }

    h2 {
        text-align: center;
        margin-bottom: 20px;
        color: #333;
    }

    .form-group {
        margin-bottom: 20px;
    }

    label {
        font-weight: bold;
        display: block;
    }

    input[type="text"], input[type="email"], input[type="password"] {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .btn-success {
        background-color: #28a745;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }

    .btn-success:hover {
        background-color: #218838;
    }
</style>

<div class="container">
    <div class="row">
        <div class="col-md-6 offset-md-3">
            <div class="registration-form" style="margin-bottom: 40px;">
                <h2>Registration Form</h2>
                <form method="post" action="" enctype="multipart/form-data">
                    {% csrf_token %}
                    {{ error }}
                    <div class="form-group">
                        <label for="username">Username:</label>
                        {{ form.username }}
                    </div>
                    <div class="form-group">
                        <label for="first_name">First Name:</label>
                        {{ form.first_name }}
                    </div>
                    <div class "form-group">
                        <label for="last_name">Last Name:</label>
                        {{ form.last_name }}
                    </div>
                    <div class="form-group">
                        <label for="email">Email:</label>
                        {{ form.email }}
                    </div>
                    <div class="form-group">
                        <label for="password">Password:</label>
                        {{ form.password }}
                    </div>
                    <div class="form-group">
                        <label for="confirm_password">Confirm Password:</label>
                        <input type="password" name="confirm_password" id="confirm_password">
                    </div>
                    <button class="btn btn-success">Register</button>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}