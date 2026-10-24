
import os
import requests


def main():
    keystring = os.getenv("ETSY_API_KEY")
    shared_secret = os.getenv("ETSY_SHARED_SECRET")
    shop_name = "NorthMuseDesigns"

    if not keystring or not shared_secret:
        raise SystemExit("Etsy API credentials are missing.")

    headers = {
        "x-api-key": f"{keystring}:{shared_secret}"
    }

    response = requests.get(
        "https://openapi.etsy.com/v3/application/shops",
        headers=headers,
        params={"shop_name": shop_name, "limit": 10},
        timeout=30,
    )

    if not response.ok:
        print("Etsy shop search failed:", response.status_code)
        print(response.text[:1000])
        raise SystemExit(1)

    shops = response.json().get("results", [])
    shop = next(
        (s for s in shops
         if s.get("shop_name", "").lower() == shop_name.lower()),
        None,
    )

    if not shop:
        print("Shop not found. Check the Etsy shop name.")
        return

    shop_id = shop["shop_id"]
    print("Shop found:", shop["shop_name"])
    print("Fetching active listings...")

    response = requests.get(
        f"https://openapi.etsy.com/v3/application/shops/{shop_id}/listings/active",
        headers=headers,
        params={"limit": 25},
        timeout=30,
    )

    if not response.ok:
        print("Listing request failed:", response.status_code)
        print(response.text[:1000])
        raise SystemExit(1)

    listings = response.json().get("results", [])
    print(f"Found {len(listings)} active listings.")

    for listing in listings:
        print("-", listing.get("title", "Untitled"))
        print(" ", listing.get("url", ""))


if __name__ == "__main__":
    main()
