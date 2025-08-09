from xml.etree import ElementTree as ET

import requests

try:
    username = "M0SNZ"
    password = ""
    callsign = "GB3RS"

    with open("hamqth.password", "r") as f:
        password = f.read().strip()

    session_url = f"https://www.hamqth.com/xml.php?u={username}&p={password}"
    session_response = requests.get(session_url)
    session_response.raise_for_status()
    session_xml = session_response.text
    namespaces = {"hamqth": "https://www.hamqth.com"}
    session_root = ET.fromstring(session_xml)
    session_elem = session_root.find(".//hamqth:session", namespaces)
    if session_elem is not None:
        error_elem = session_elem.find("hamqth:error", namespaces)
        if error_elem is not None:
            raise ValueError(f"HamQTH error: {error_elem.text}")
        session_id_elem = session_elem.find("hamqth:session_id", namespaces)
        if session_id_elem is not None:
            session_id = session_id_elem.text
        else:
            raise ValueError("Session ID not found in response")
    else:
        raise ValueError("Invalid response from HamQTH")

    lookup_url = f"https://www.hamqth.com/xml.php?id={session_id}&callsign={callsign}&prg=PycomRadioGUI"
    lookup_response = requests.get(lookup_url)
    lookup_response.raise_for_status()
    lookup_xml = lookup_response.text
    lookup_root = ET.fromstring(lookup_xml)
    search_elem = lookup_root.find(".//hamqth:search", namespaces)
    if search_elem is not None:
        data = {elem.tag.split("}")[1]: elem.text for elem in search_elem}
        print(
            {
                "call": callsign,
                "name": data.get("adr_name", data.get("nick", "")),
                "country": data.get("country", ""),
                "grid": data.get("grid", ""),
            }
        )
    else:
        raise ValueError("Callsign not found or invalid response from HamQTH")
except Exception as e:
    print(f"Error in HamQTH lookup: {e}")
