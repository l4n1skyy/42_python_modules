import json
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from ex0.space_station import SpaceStation
from ex1.alien_contact import AlienContact
from ex2.space_crew import SpaceMission

DATA = Path(__file__).parent / "generated_data"


def check(model: Any, filename: str, id_key: str) -> None:
    records = json.loads((DATA / filename).read_text())
    valid = 0
    print(f"== {filename}")
    for record in records:
        try:
            model.model_validate(record)
            valid += 1
        except ValidationError as e:
            msgs = [x["msg"].removeprefix("Value error, ") for x in e.errors()]
            print(f"   REJECTED {record[id_key]}: {msgs}")
    print(f"   {valid} valid / {len(records)} total")


check(SpaceStation, "space_stations.json", "station_id")
check(AlienContact, "alien_contacts.json", "contact_id")
check(SpaceMission, "space_missions.json", "mission_id")
check(SpaceStation, "invalid_stations.json", "station_id")
check(AlienContact, "invalid_contacts.json", "contact_id")
