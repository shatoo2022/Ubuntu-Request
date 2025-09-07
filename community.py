import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
     
    # Get URL from user
    url = input("Please enter the image URL: ")
    
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        #  adding a header, Pretend to be a browser to avoid 403 Forbidden

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            )
        }

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes

         # Check Content-Type header
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped: URL does not contain an image (Content-Type = {content_type})")
            return
        
        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename:
            filename = "downloaded_image.jpg"
            
             # Prevent duplicate downloads
        if os.path.exists(filepath):
            print(f"⚠ Skipped duplicate: {filename} already exists in Fetched_Images")
            return
        
        # Save the image
        filepath = os.path.join("Fetched_Images", filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

        # Ask for multiple URLs at once
    urls = input("Enter one or more image URLs (separated by spaces): ").split()

    # Process each URL
    for url in urls:
        try:
            fetch_and_save_image(url)
        except Exception as e:
            print(f"✗ Failed to fetch {url}: {e}")

    print("\nConnection strengthened. Community enriched.")

def fetch_and_save_image(url):
    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        filename = "downloaded_image.jpg"
    filepath = os.path.join("Fetched_Images", filename)
    with open(filepath, 'wb') as f:
        f.write(response.content)
    print(f"✓ Successfully fetched: {filename}")
    print(f"✓ Image saved to {filepath}")

if __name__ == "__main__":
    main()