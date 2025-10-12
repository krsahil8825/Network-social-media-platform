import requests
import validators


def is_image_url(url: str) -> bool:
    if not validators.url(url):
        return False

    try:
        response = requests.head(url, allow_redirects=True, timeout=5)

        content_type = response.headers.get("Content-Type", "").lower()

        return content_type.startswith("image/")
    except requests.RequestException:
        return False