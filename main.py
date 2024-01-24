import sys
import subprocess

# Import the 'upload_openai' module (assuming it's in the same directory)
import upload_openai

def main():
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
    result = upload_openai.upload_file_to_openai(file_path)
    if result:
        print("File uploaded successfully. Response:", result)
    else:
        print("File upload failed.")

if __name__ == "__main__":
    main()
