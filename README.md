# Professional Email Automation

This is a Python-based email automation tool that uses the Gmail API to send marketing and notification emails to a list of customers.

## Setup

1.  **Enable the Gmail API and Create Credentials:**
    *   Follow the instructions in the [Google Cloud Console](https://console.cloud.google.com/flows/enableapi?apiid=gmail.googleapis.com) to enable the Gmail API for your project.
    *   Create an OAuth 2.0 Client ID for a **Desktop application**.
    *   Download the `credentials.json` file and place it in the same directory as the `main.py` script.

2.  **Install Dependencies:**
    *   Install the necessary Python libraries using pip:
        ```
        pip install -r requirements.txt
        ```

## Usage

1.  **Add Customers:**
    *   Open the `customers.csv` file and add your customer information. The file should have two columns: `name` and `email`.

2.  **Customize Email Templates:**
    *   The `templates` directory contains sample email templates (`marketing_email.txt` and `notification_email.txt`). You can edit these templates or add new ones to suit your needs.

3.  **Run the Application:**
    *   Execute the `main.py` script from your terminal:
        ```
        python main.py
        ```
    *   The first time you run the script, you will be prompted to authorize access to your Gmail account. Follow the on-screen instructions to complete the authorization process.
    *   After authorizing, you will be prompted to choose an email template. The script will then send the emails to all the customers in your `customers.csv` file.
