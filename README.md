Website Recon Tool 🌐

The Website Recon Tool is a comprehensive reconnaissance tool designed for security analysts and penetration testers to gather valuable information about target websites.

## Features
- **IP Address Lookup**: Quickly find the IP address of a website.
- **WHOIS Report**: Retrieve WHOIS information for the target domain.
- **Technology Detection**: Identify technologies used on the website.
- **DNS Information**: Fetch DNS records associated with the domain.
- **Subdomain Enumeration**: Discover subdomains of the target domain.
- **Report Generation**: Generate a comprehensive report of the gathered information.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/hasanfahad23/Website-Recon-Tool.git
   ```
2. Navigate to the project directory:
   ```
   cd Website-Recon-Tool
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the script and follow the prompts to perform various reconnaissance tasks.

```bash
./website_recon.py
```

## Options
- **-t, --target**: Specify the target website.
- **-w, --whois**: Generate a WHOIS report.
- **-t, --tech**: Perform technology detection.
- **-d, --dns**: Retrieve DNS information.
- **-s, --subdomains**: Enumerate subdomains.
- **-r, --report**: Generate a report.

Example:
```bash
./website_recon.py -t example.com -w -t -d -s -r
```

## Developer
- **Fahad Hossain**
  - GitHub: [hasanfahad23](https://github.com/hasanfahad23)
  - LinkedIn: [Fahad Hossain](https://www.linkedin.com/in/fahad-hossain-bb3637278/)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
