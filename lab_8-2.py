# Function to generate invitations for a list of names.
def generate_party_invitations(names):
    """
    This function takes a list of names and generates invitations for a party.
    It uses a for loop to print each invitation.

    Parameters:
    - names (list): A list of names.

    Returns:
    - None
    """
    # Check if the list is empty
    if not names:
        print("No names provided. Cannot generate invitations.")
        return

    # Iterate through the list of names using a for loop
    for name in names:
        # Generate and print the invitation for each person
        invitation = f"Hi {name}, You're invited to my party on Friday!"
        print(invitation)

# Example list of names
guest_names = ["Jake", "Bob", "Charlie"]

# Call the function with the list of names
generate_party_invitations(guest_names)
