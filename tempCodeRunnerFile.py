    elif '+' in value:  # If there's a '+' sign, remove it and use the base value
        return int(value.replace('+', ''))
    else:  # If it's a single number, convert directly
        return int(value)