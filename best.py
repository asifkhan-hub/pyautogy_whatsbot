import pyautogui
import time

def send_messages_one_by_one():
    try:
        custom_delay = float(input('Enter the delay between messages (in seconds): '))

        # Read message content from a file
        with open('data.txt', 'r') as file:
            messages = file.readlines()

        if not messages:
            print('Error: The data.txt file is empty.')
            return

        # Ensure the user has time to focus on the input field
        print('Please focus on the input field...')
        time.sleep(5)

        for message in messages:
            message = message.strip()
            pyautogui.write(message)
            pyautogui.press('enter')
            time.sleep(custom_delay)

        print('All messages sent successfully.')

    except ValueError:
        print('Error: Please enter a valid delay value.')
    except FileNotFoundError:
        print('Error: The data.txt file was not found.')
    except KeyboardInterrupt:
        print('\nScript terminated by the user.')

if __name__ == "__main__":
    send_messages_one_by_one()
