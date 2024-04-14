import socket
import whois
import dns.resolver
import requests

def print_banner():
    """
    Function to print the banner with ASCII art.
    """
    print("""
  _____             _           _     _             
 |  __ \           | |         | |   (_)            
 | |__) |___   ___ | |__   __ _| |__  _ _ __   __ _ 
 |  _  // _ \ / _ \| '_ \ / _` | '_ \| | '_ \ / _` |
 | | \ \ (_) | (_) | |_) | (_| | | | | | | | | (_| |
 |_|  \_\___/ \___/|_.__/ \__, |_| |_|_|_| |_|\__, |
                            __/ |              __/ |
                           |___/              |___/  
    Website Analysis Tool - Developed by Fahad Hossain
    GitHub: https://github.com/hasanfahad23
    LinkedIn: https://www.linkedin.com/in/fahad-hossain-bb3637278/
    """)

def get_ip_address(website):
    """
    Function to retrieve the IP address of a given website.
    """
    try:
        ip_address = socket.gethostbyname(website)
        print(f"The IP address of {website} is: {ip_address}")
        return ip_address
    except socket.gaierror as e:
        print(f"Error: Unable to resolve the website's IP address. {e}")

def show_whois_report(website):
    """
    Function to display the WHOIS report of a website.
    """
    try:
        w = whois.whois(website)
        whois_report = w.text
        print("WHOIS Report:")
        print(whois_report)
        return whois_report
    except whois.parser.PywhoisError as e:
        print(f"Error: Unable to fetch WHOIS information. {e}")

def find_technologies(website):
    """
    Function to find the technologies used by a website.
    """
    try:
        req = requests.get("https://builtwith.com/"+website)
        if req.status_code == 200:
            technologies_used = req.text.split("Tech Spend")[1].split("</")[0].split(">")[1].replace("<br/>", ", ")
            print("Technologies used by", website, ":")
            print(technologies_used)
            return technologies_used
        else:
            print("Error: Unable to fetch technology information.")
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch technology information. {e}")

def find_dns_info(website):
    """
    Function to find DNS information of a website.
    """
    try:
        print("DNS information for", website, ":")
        dns_records = dns.resolver.resolve(website, 'A')
        dns_info = []
        for record in dns_records:
            print("A Record:", record)
            dns_info.append(f"A Record: {record}")
        return dns_info
    except dns.resolver.NoAnswer as e:
        print(f"Error: No DNS information found. {e}")

def find_subdomains(website):
    """
    Function to find subdomains of a website.
    """
    try:
        print("Subdomains of", website, ":")
        dns_records = dns.resolver.resolve(website, 'CNAME')
        subdomains = []
        for record in dns_records:
            print("CNAME Record:", record)
            subdomains.append(f"CNAME Record: {record}")
        return subdomains
    except dns.resolver.NoAnswer as e:
        print(f"Error: No subdomains found. {e}")

def generate_report(website, ip_address, whois_report, technologies_used, dns_info, subdomains):
    """
    Function to generate a report and save it to a text file.
    """
    with open(f"{website}_report.txt", "w") as file:
        file.write("Website Analysis Report\n")
        file.write("=======================\n")
        file.write(f"Website URL: {website}\n")
        file.write(f"IP Address: {ip_address}\n")
        file.write("\n")
        file.write("WHOIS Report:\n")
        file.write(f"{whois_report}\n")
        file.write("\n")
        file.write("Technologies Used:\n")
        file.write(f"{technologies_used}\n")
        file.write("\n")
        file.write("DNS Information:\n")
        for record in dns_info:
            file.write(f"{record}\n")
        file.write("\n")
        file.write("Subdomains:\n")
        for subdomain in subdomains:
            file.write(f"{subdomain}\n")
    print("Report generated successfully!")

if __name__ == "__main__":
    print_banner()

    website = input("Enter the website URL: ")

    ip_address = get_ip_address(website)

    choice = input("Do you want to show WHOIS report? (yes/no): ")
    if choice.lower() == 'yes':
        whois_report = show_whois_report(website)

    choice = input("Do you want to find technologies used? (yes/no): ")
    if choice.lower() == 'yes':
        technologies_used = find_technologies(website)

    choice = input("Do you want to find DNS information? (yes/no): ")
    if choice.lower() == 'yes':
        dns_info = find_dns_info(website)

    choice = input("Do you want to find subdomains? (yes/no): ")
    if choice.lower() == 'yes':
        subdomains = find_subdomains(website)

    choice = input("Do you want to generate a report? (yes/no): ")
    if choice.lower() == 'yes':
        generate_report(website, ip_address, whois_report, technologies_used, dns_info, subdomains)
