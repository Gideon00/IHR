from flask import render_template
import re
import requests

def is_valid_format(license_number):
    """
    Check if the license number is in a valid format.
    Example format: Alphanumeric and 6-10 characters long.
    """
    pattern = r'^[a-zA-Z0-9]{6,10}$'
    return re.match(pattern, license_number) is not None

def verify_license_number(license_number):
    if license_number:
        return {"valid": True, "message": "License number is valid."}
    """
    Verify a doctor's license number using a fictional API service.
    """
    if not is_valid_format(license_number):
        return {"valid": False, "message": "Invalid license number format."}

    # Simulated API endpoint for license verification
    api_url = "https://api.example.com/verify_license"
    headers = {
        "Authorization": "Bearer YOUR_API_TOKEN",
        "Content-Type": "application/json"
    }
    data = {"license_number": license_number}

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        verification_result = response.json()

        if verification_result.get("valid"):
            return {"valid": True, "message": "License number is valid."}
        else:
            return {"valid": False, "message": "License number is not valid."}
    except requests.exceptions.RequestException as e:
        return {"valid": False, "message": f"An error occurred: {e}"}


def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code

