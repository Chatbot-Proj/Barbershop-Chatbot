import json
from typing import Any, Text, Dict, List
from pathlib import Path
from prettytable import PrettyTable

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAvailableAppointments(Action):
    def name(self) -> Text:
        return "action_available_appointments"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Load the JSON file with the available appointments
        file_path = str(Path(__file__).parent / "sample_data/available_times.json")
        with open(file_path) as f:
            data = json.load(f)

        # Extract the appointment data from the JSON file
        appointments = data["appointments"]

        # Create a table with the appointment data
        table = PrettyTable()
        table.field_names = ["Date", "Time", "Length", "Barber Name", "Location"]

        for appointment in appointments:
            table.add_row(
                [
                    appointment["date"],
                    appointment["time"],
                    appointment["length"],
                    appointment["barber_name"],
                    appointment["location"]["address"],
                ]
            )

        # Send the table back to the user
        dispatcher.utter_message(text=f"Here are the available appointment times:\n\n{table}")

        return []
