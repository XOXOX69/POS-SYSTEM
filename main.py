import csv
from gmail_service import get_gmail_service, send_email

def read_customers(filename="customers.csv"):
    """Reads customers from a CSV file."""
    customers = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append(row)
    return customers

def read_template(filename):
    """Reads an email template from a file."""
    with open(filename, "r") as file:
        template = file.read()
    return template

def main():
    """Main function to run the email automation."""
    # 1. Get the Gmail service
    service = get_gmail_service()
    if not service:
        print("Failed to connect to Gmail. Exiting.")
        return

    # 2. Read the customer list
    customers = read_customers()
    if not customers:
        print("No customers found in customers.csv. Exiting.")
        return

    # 3. Choose the email template
    print("Available templates:")
    print("1. Marketing Email (templates/marketing_email.txt)")
    print("2. Notification Email (templates/notification_email.txt)")
    
    choice = input("Which template would you like to use? (1 or 2): ")
    if choice == "1":
        template_path = "templates/marketing_email.txt"
    elif choice == "2":
        template_path = "templates/notification_email.txt"
    else:
        print("Invalid choice. Exiting.")
        return

    template = read_template(template_path)
    if not template:
        print(f"Template file {template_path} is empty. Exiting.")
        return
        
    lines = template.splitlines()
    subject = lines[0].replace("Subject: ", "")
    body_template = "\n".join(lines[1:])


    # 4. Send emails
    for customer in customers:
        body = body_template.format(name=customer["name"])
        send_email(service, customer["email"], subject, body)

    print("Email campaign finished.")

if __name__ == "__main__":
    main()
