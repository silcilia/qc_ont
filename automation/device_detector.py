
import re

from automation.browser import open_device_gui


VENDOR_KEYWORDS = {
    "Huawei": ["huawei"],
    "ZTE": ["zte"],
    "FiberHome": ["fiberhome", "fiber home"],
}


def detect_vendor(text):
    text = text.lower()

    for vendor, keywords in VENDOR_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            return vendor

    return "Unknown"


def detect_model(text):
    patterns = [
        r"\bHG\d{4,}[A-Z0-9-]*\b",
        r"\bEG\d{4,}[A-Z0-9-]*\b",
        r"\bZX[A-Z0-9-]{3,}\b",
        r"\bAN\d{3,}[A-Z0-9-]*\b",
        r"\bG-\d{4,}[A-Z0-9-]*\b",
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(0)

    return "Unknown"


def detect_firmware(text):
    patterns = [
        r"(?:firmware|software version|software)\s*[:=]\s*([A-Za-z0-9._-]+)",
        r"(?:version|ver)\s*[:=]\s*([A-Za-z0-9._-]+)",
    ]

    for pattern in patterns:
        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(1)

    return "Unknown"


def run_detection(ip_address):
    gui_data = open_device_gui(ip_address)

    if "error" in gui_data:
        return gui_data

    # Gabungkan informasi halaman untuk dianalisis
    combined_text = (
        gui_data.get("title", "") + "\n" +
        gui_data.get("page_text", "") + "\n" +
        str(gui_data.get("inputs", []))
    )

    result = {
        "ip_address": ip_address,
        "vendor": detect_vendor(combined_text),
        "model": detect_model(combined_text),
        "firmware": detect_firmware(combined_text),
        "page_title": gui_data.get("title"),
        "http_status": gui_data.get("http_status"),
        "inputs": gui_data.get("inputs"),
        "buttons": gui_data.get("buttons"),
    }

    return result
