import os
import sys

def display_targets(networks, security_type):
    print("Select a target: \n")
    try:
        rows, columns = os.popen('stty size', 'r').read().split()
        columns = int(columns)
        for i in range(len(networks)):
            # Ensure all components are strings
            num = str(i + 1)
            ssid = str(networks[i])
            security = str(security_type[i])  # Convert to string to avoid OC_PythonLong
            # Compute width with string concatenation
            display_text = f"{num}. {ssid}{security}"
            width = len(display_text) + 2
            spacer = " "

            if columns >= 100:
                calc = int((columns - width) * 0.75)
            else:
                calc = columns - width

            for index in range(calc):
                spacer += "."
                if index == calc - 1:
                    spacer += " "

            print(f"{num}. {ssid}{spacer}{security}")
    except Exception as e:
        print(f"Error displaying targets: {e}")
        sys.exit(-1)

def prompt_for_target_choice(max):
    while True:
        try:
            selected = int(input("\nEnter number of target: "))
            if(selected >= 1 and selected <= max):
                return selected - 1
        except Exception as e:
            pass

        print("Invalid choice: Please pick a number between 1 and " + str(max))
