def vacation():
    print("Welcome to our Vacation Destination Decision Maker!\n")
    climate = input("Preferred climate (cold/warm/moderate): ").lower()
    budget = input("Budget (low/medium/high): ").lower()
    activity = input("Activity (adventure/relaxation/culture/wildlife): ").lower()
    duration = input("Trip duration (short/medium/long): ").lower()

    if climate == "cold" and activity == "adventure" and budget in ("medium", "high"):
        destination = "Switzerland"
    elif climate == "warm" and activity == "relaxation" and budget in ("low", "medium"):
        destination = "Goa, India"
    elif climate == "moderate" and activity == "culture" and budget == "medium":
        destination = "Kyoto, Japan"
    elif climate == "warm" and activity == "wildlife" and budget in ("medium", "high"):
        destination = "Kenya Safari"
    elif climate == "cold" and activity == "culture" and budget == "low":
        destination = "Nepal"
    elif climate == "moderate" and activity == "adventure" and budget == "medium":
        destination = "New Zealand"
    elif climate == "warm" and activity == "adventure" and duration == "long":
        destination = "Thailand"
    elif climate == "moderate" and activity == "relaxation":
        destination = "Bali, Indonesia"
    else:
        destination = "Staycation or Explore Local Spots"
    print(f"\nSuggested destination: {destination}")
vacation()
