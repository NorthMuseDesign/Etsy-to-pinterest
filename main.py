
import os
import requests


def main():
    api_key = os.getenv("ETSY_API_KEY")
    shared_secret = os.getenv("ETSY_SHARED_SECRET")

    if not api_key or not shared_secret:
        print("Missing Etsy API credentials in GitHub Secrets.")
        raise SystemExit(1)

    print("Etsy credentials found.")
    print("Ready to configure Etsy API access.")


if __name__ == "__main__":
    main()
