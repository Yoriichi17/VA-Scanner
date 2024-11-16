import os
from general import create_dir, write_file
from domain_name import get_domain
from ip_address import get_ip
from nmap import get_nmap
from robots_text import get_robotext
from whois import get_whois

ROOT_DIR = 'vascanner'
create_dir(ROOT_DIR)

def gather_info(name, url):
    print("Creating project directory...")
    create_dir(ROOT_DIR)
    print("Fetching domain name...")
    
    try:
        domain_name = get_domain(url)
        print("Domain name found.")
    except Exception as e:
        domain_name = "Error fetching domain name: " + str(e)
        print(domain_name)

    print("Fetching IP address...")
    try:
        ip_address = get_ip(domain_name)
        print("IP address found.")
    except Exception as e:
        ip_address = "Error fetching IP address: " + str(e)
        print(ip_address)
    
    print("Running Nmap scan...")
    try:
        nmap_result = get_nmap("-F", ip_address)
        print("Nmap scan completed.")
    except Exception as e:
        nmap_result = "Error running Nmap scan: " + str(e)
        print(nmap_result)
    
    print("Fetching robots.txt...")
    try:
        robots_txt = get_robotext(url)
        print("robots.txt fetched.")
    except Exception as e:
        robots_txt = "Error fetching robots.txt: " + str(e)
        print(robots_txt)
    
    print("Fetching Whois information...")
    try:
        whois_info = get_whois(domain_name)
        print("Whois information fetched.")
    except Exception as e:
        whois_info = "Error fetching Whois information: " + str(e)
        print(whois_info)

    create_report(name, url, domain_name, nmap_result, robots_txt, whois_info)
    print("Report generated successfully.")

def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
    project_dir = os.path.join(ROOT_DIR, name)
    create_dir(project_dir)
    
    print("Writing report files...")
    try:
        write_file(os.path.join(project_dir, 'full_url.txt'), full_url)
        write_file(os.path.join(project_dir, 'domain_name.txt'), domain_name)
        write_file(os.path.join(project_dir, 'robots.txt'), robots_txt)
        write_file(os.path.join(project_dir, 'nmap.txt'), nmap)
        write_file(os.path.join(project_dir, 'whois.txt'), whois)
        print("Report files written successfully.")
    except Exception as e:
        print(f"Error writing report files: {e}")

# Example usage
gather_info("example_project", "https://nmap.org/")
