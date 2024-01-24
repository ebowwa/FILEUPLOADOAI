import sys
import subprocess
import api_key_manager
import upload_openai

def main():
    # Check if the user wants to set an API key
    if len(sys.argv) >= 2 and sys.argv[1] == '--set-api-key':
        if len(sys.argv) != 3:
            print("Usage: python main.py --set-api-key <API_KEY>")
            return
        api_key_manager.set_api_key(sys.argv[2])
        print("API key set successfully.")
        return

    # Regular file upload functionality
    if len(sys.argv) != 2:
        # Check Python version and adjust the usage message accordingly
        try:
            python_version = subprocess.check_output(['python', '--version'])
            version_message = "python3" if "Python 3" in str(python_version) else "python"
        except subprocess.CalledProcessError:
            # In case the above check fails, default to 'python3'
            version_message = "python3"

        print(f"Usage: {version_message} main.py <file_path>")
        return

    file_path = sys.argv[1]
    try:
        api_key = api_key_manager.get_api_key()
        result = upload_openai.upload_file_to_openai(file_path, api_key)
        if result:
            print("File uploaded successfully. Response:", result)
        else:
            print("File upload failed.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()