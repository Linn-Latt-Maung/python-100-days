def add_setting(settings_dict, setting_tuple):
    # Unpack the tuple and convert key and value to lowercase
    key, value = setting_tuple
    key = str(key).lower()
    value = str(value).lower()
    
    # Check if the key already exists in the dictionary
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    # Add the new setting and return success message
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict, setting_tuple):
    # Unpack and convert to lowercase
    key, value = setting_tuple
    key = str(key).lower()
    value = str(value).lower()
    
    # Check if the key exists to perform update
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings_dict, key):
    # Convert key to lowercase
    key = str(key).lower()
    
    # Remove the key if it exists
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"

def view_settings(settings_dict):
    # Check if the dictionary is empty
    if not settings_dict:
        return "No settings available."
    
    # Initialize the return string with the header and a newline
    result = "Current User Settings:\n"
    
    # Iterate through the dictionary
    for key, value in settings_dict.items():
        # Add the capitalized key, the value, and a newline
        result += f"{key.capitalize()}: {value}\n"
        
    return result

# Requirement 9: Create a dictionary named test_settings for testing
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

# Example of how it would look when called:
print(view_settings(test_settings))
