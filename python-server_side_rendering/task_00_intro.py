import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files for a list of attendees
    using the provided template.
    
    Args:
        template (str): The template string with placeholders.
        attendees (list): List of dictionaries with attendee information.
    """

    # Check input types
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees must be a list of dictionaries, got {type(attendees).__name__}.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Define the placeholders expected in the template
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        invitation_text = template
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            # Replace missing or None values with "N/A"
            if value is None:
                value = "N/A"
            invitation_text = invitation_text.replace(f"{{{placeholder}}}", str(value))
        
        # Output file name
        output_filename = f"output_{idx}.txt"
        
        try:
            with open(output_filename, "w") as file:
                file.write(invitation_text)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
