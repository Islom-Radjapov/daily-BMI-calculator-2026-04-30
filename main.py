```python
#!/usr/bin/env python3
"""
BMI Calculator Application
This script calculates Body Mass Index (BMI) and provides health feedback.
BMI = weight (kg) / (height (m) ** 2)
"""

def get_user_input():
    """
    Get weight and height from the user with error handling.
    Returns a tuple of (weight, height) or None if input is invalid.
    """
    while True:
        try:
            # Prompt user for weight in kilograms
            weight_input = input("\nEnter your weight in kilograms (kg): ")
            weight = float(weight_input)
            
            # Validate weight is positive
            if weight <= 0:
                print("Error: Weight must be a positive number.")
                continue
            
            # Prompt user for height in meters
            height_input = input("Enter your height in meters (m): ")
            height = float(height_input)
            
            # Validate height is positive
            if height <= 0:
                print("Error: Height must be a positive number.")
                continue
            
            # Return valid inputs
            return weight, height
        
        except ValueError:
            # Handle non-numeric input
            print("Error: Please enter valid numeric values.")
        except KeyboardInterrupt:
            # Handle user pressing Ctrl+C
            print("\n\nProgram interrupted by user.")
            return None


def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: weight (kg) / (height (m) ** 2)
    
    Args:
        weight: Weight in kilograms (float)
        height: Height in meters (float)
    
    Returns:
        bmi: Body Mass Index value (float)
    """
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        print("Error: Height cannot be zero.")
        return None


def get_bmi_category(bmi):
    """
    Determine BMI category and health status based on WHO standards.
    
    Args:
        bmi: Body Mass Index value (float)
    
    Returns:
        A tuple of (category, health_status)
    """
    if bmi < 18.5:
        category = "Underweight"
        health_status = "You may need to gain weight. Consult a healthcare provider."
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        health_status = "Great! You have a healthy weight."
    elif 25 <= bmi < 30:
        category = "Overweight"
        health_status = "You may want to consider lifestyle changes. Consult a doctor."
    else:  # bmi >= 30
        category = "Obese"
        health_status = "Please consult a healthcare professional for guidance."
    
    return category, health_status


def display_results(weight, height, bmi):
    """
    Display the BMI calculation results and health feedback to the user.
    
    Args:
        weight: Weight in kilograms (float)
        height: Height in meters (float)
        bmi: Body Mass Index value (float)
    """
    category, health_status = get_bmi_category(bmi)
    
    # Create a formatted output
    print("\n" + "=" * 50)
    print("BMI CALCULATION RESULTS")
    print("=" * 50)
    print(f"Weight:       {weight:.1f} kg")
    print(f"Height:       {height:.2f} m")
    print(f"BMI:          {bmi:.1f}")
    print(f"Category:     {category}")
    print(f"Status:       {health_status}")
    print("=" * 50)


def main():
    """
    Main function to run the BMI calculator application.
    """
    print("\n" + "=" * 50)
    print("WELCOME TO THE BMI CALCULATOR")
    print("=" * 50)
    print("This calculator determines your Body Mass Index (BMI)")
    print("based on your weight and height.")
    
    while True:
        # Get user input
        user_data = get_user_input()
        
        # Check if user cancelled the input
        if user_data is None:
            break
        
        weight, height = user_data
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Check if calculation was successful
        if bmi is None:
            continue
        
        # Display results
        display_results(weight, height, bmi)
        
        # Ask if user wants to calculate again
        print("\nWould you like to calculate another BMI?")
        try:
            another = input("Enter 'yes' or 'no': ").lower().strip()
            if another not in ['yes', 'y']:
                print("\nThank you for using the BMI Calculator. Stay healthy!")
                break
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break


# Entry point of the script
if __name__ == "__main__":
    main()
```