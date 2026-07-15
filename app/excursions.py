"""Curated shore-excursion catalog + the agent's grounding instructions."""

EXCURSIONS = [
    ("Cozumel", "Reef Snorkel Adventure", 95, True, "water/adventure"),
    ("Cozumel", "Mayan Ruins & Beach Break", 140, True, "culture"),
    ("Cozumel", "Private Catamaran Sail", 180, False, "relaxation"),
    ("Nassau", "Blue Lagoon Dolphin Encounter", 120, True, "water"),
    ("Nassau", "Historic Nassau Food Walk", 75, False, "food"),
    ("Nassau", "Exuma Cays Speedboat & Swimming Pigs", 210, False, "adventure"),
    ("Cabo San Lucas", "Arch & Sea Lion Snorkel", 85, True, "water"),
    ("Cabo San Lucas", "Camel Ride & Taco Lunch", 130, True, "food/adventure"),
    ("Cabo San Lucas", "Sunset Sail with Tapas", 110, False, "relaxation/food"),
    ("Cabo San Lucas", "Desert ATV Off-Road", 150, False, "adventure"),
    ("Cabo San Lucas", "Whale Watching (seasonal)", 90, True, "nature"),
    ("Cabo San Lucas", "Luxury Beach Club Day Pass", 100, False, "relaxation"),
]


def catalog_text() -> str:
    lines = []
    port = None
    for p, name, price, family, kind in EXCURSIONS:
        if p != port:
            lines.append(f"\n{p}:")
            port = p
        fam = "family-friendly" if family else "adults"
        lines.append(f"- {name} (${price}, {fam}, {kind})")
    return "\n".join(lines)


def instructions() -> str:
    return (
        "You are Horizon Helper, a friendly shore-excursion concierge for the fictional "
        "Blue Horizon Cruise Line. Only recommend from the catalog below; never invent "
        "excursions or prices. If the guest hasn't said their port or interests, ask one "
        "short clarifying question first. For each suggestion give the name, a one-line "
        "reason it fits their interests/budget/group, and the price. Keep replies short, "
        "warm, and use plain punctuation.\n\nCATALOG:" + catalog_text()
    )
