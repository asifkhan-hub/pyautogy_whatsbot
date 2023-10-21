import pyautogui
import time

def send_messages():
    try:
        number_of_messages = int(input('Enter the number of messages to send: '))
        custom_delay = float(input('Enter the delay between messages (in seconds): '))

        # Read message content from a file
        with open('data.txt', 'r') as file:
            message_content = file.read().strip()

        # Ensure the user has time to focus on the input field
        print('Please focus on the input field...')
        time.sleep(5)

        for num in range(number_of_messages):
            pyautogui.write(message_content)
            pyautogui.press('enter')
            time.sleep(custom_delay)

        print('Script executed successfully.')

    except ValueError:
        print('Error: Please enter valid input.')
    except FileNotFoundError:
        print('Error: The data.txt file was not found.')
    except KeyboardInterrupt:
        print('\nScript terminated by the user.')

if __name__ == "__main__":
    send_messages()
