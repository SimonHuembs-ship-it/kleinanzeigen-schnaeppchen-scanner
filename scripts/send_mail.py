"""Verschickt email_output.html ueber Resend.

Wird von .github/workflows/send-email.yml aufgerufen, sobald ein Push die
Datei email_output.html beruehrt.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
BERLIN = timezone(timedelta(hours=2))

ABSENDER = os.environ.get("MAIL_VON", "Kleinanzeigen-Bot <kleinanzeigen-bot@simonhuembs.com>")
EMPFAENGER = os.environ.get("MAIL_AN", "kleinanzeigen-bot@simonhuembs.com")


def main() -> int:
    schluessel = os.environ.get("RESEND_API_KEY")
    if not schluessel:
        print("RESEND_API_KEY fehlt", file=sys.stderr)
        return 1

    pfad = WURZEL / "email_output.html"
    if not pfad.exists():
        print("email_output.html fehlt, nichts zu senden", file=sys.stderr)
        return 1

    inhalt = pfad.read_text(encoding="utf-8")
    heute = datetime.now(BERLIN)
    betreff = os.environ.get("MAIL_BETREFF") or f"Kleinanzeigen Schnäppchen, {heute:%d.%m.%Y}"

    anfrage = urllib.request.Request(
        "https://api.resend.com/emails",
        data=json.dumps({
            "from": ABSENDER,
            "to": [e.strip() for e in EMPFAENGER.split(",") if e.strip()],
            "subject": betreff,
            "html": inhalt,
        }).encode("utf-8"),
        headers={"Authorization": f"Bearer {schluessel}",
                 "Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(anfrage, timeout=30) as antwort:
            print("gesendet:", antwort.read().decode("utf-8"))
        return 0
    except urllib.error.HTTPError as fehler:
        print(f"Resend antwortet {fehler.code}: {fehler.read().decode('utf-8')}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
