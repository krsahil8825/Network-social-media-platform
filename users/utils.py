import requests
import validators


def is_image_url(url: str) -> bool:
    # Validate URL format
    if not validators.url(url):
        return False

    try:
        # Send HEAD request to avoid downloading full content
        response = requests.head(url, allow_redirects=True, timeout=5)

        # Read content type header
        content_type = response.headers.get("Content-Type", "").lower()

        # Check if it's an image
        return content_type.startswith("image/")
    except requests.RequestException:
        # Network/connection error
        return False
