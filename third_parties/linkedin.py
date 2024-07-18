# module to communicate with OS
import os

# module for HTTP/HTTPS requests
import requests

# loading env variables
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from linkedIn profiles,
    Manually scrape the information from the linkedIn profile"""

    if mock:
        linkedin_profile_url = "https://www.linkedin.com/in/miho-funayama-653b391b4/"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )

        data = response.json()

        data = {
            k: v
            # data.items() to get all key and value pairs
            for k, v in data.items()
            if v not in ([], "", "", None)
            if v not in ["people_also_viewed", "certifications"]
        }
        # remove redundant field
        if data.get("groups"):
            for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")

        return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/miho-funayama-653b391b4/",
            mock=True,
        )
    )
