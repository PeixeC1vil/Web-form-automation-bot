# Web Form Automation Bot

Automation tool built with Python that reads spreadsheet data and automatically fills web forms using Selenium.

---

## Overview

This project automates repetitive form-filling tasks by reading structured data from spreadsheets and injecting it into web forms automatically.

The automation workflow:

1. Reads client data from a spreadsheet
2. Opens the target website
3. Locates form fields
4. Fills them automatically
5. Submits the form

---

## Technologies

- Python
- Selenium
- OpenPyXL

---

## Use Case

Many administrative workflows require manually copying data from spreadsheets into web forms.  
This automation eliminates repetitive work and reduces human error.

---

## Demo

![Automation Demo](demo.gif)

---

## Installation
Clone the repository:
```bash
git clone https://github.com/SEUUSUARIO/web-form-automation-bot.git
cd web-form-automation-bot

pip install -r requirements.txt

python bot.py