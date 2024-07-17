# module to communicate with OS
import os
# module for HTTP/HTTPS requests
import requests
# loading env variables
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: boolean = False):
    """scrape information from linkedin profiles,
    Manually scrape the information from the linkedin profile"""

    if mock:
        linkedin_profile_url = "https://www.linkedin.com/in/miho-funayama-653b391b4/"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/miho-funayama-653b391b4/"
        )
    )