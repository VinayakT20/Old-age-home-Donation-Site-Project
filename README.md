# HelpAge Foundation Donation Portal

This project implements a donation portal for HelpAge Foundation, an organization dedicated to helping the elderly. The system allows users to sign up, log in, and make donations securely while providing an intuitive interface for both new and returning donors.

## Features

- User authentication (Sign up and Sign in)
- Secure payment gateway for credit and debit card transactions
- Email confirmation system for successful donations
- Q&A section for common inquiries
- Input validation for user details and payment information

## Libraries and Modules Used

- `re`: For regular expression operations, used in validating input formats
- `os`: Provides functions for interacting with the operating system
- `email.message`: For creating and handling email messages
- `ssl`: Ensures secure connections for email sending
- `smtplib`: Enables sending emails via SMTP protocol
- `email.utils`: Utilities for email handling
- `pathlib`: Object-oriented filesystem paths

## How It Works

1. Users are greeted with a welcome screen and prompted to sign up or sign in.
2. New users can create an account, while existing users can log in.
3. Donors provide their personal details and choose a payment method.
4. The payment gateway securely processes credit or debit card information.
5. Upon successful payment, a confirmation email is sent to the donor.
6. Users can access a Q&A section for additional information or support.

## Security Features

- Password confirmation during sign-up
- Input validation for email addresses, phone numbers, and payment details
- Secure email sending using SSL

This project demonstrates the implementation of a full-fledged donation system, incorporating user authentication, secure payment processing, and automated communication with donors. It serves as a practical example of integrating various Python libraries to create a functional web application for charitable purposes.
