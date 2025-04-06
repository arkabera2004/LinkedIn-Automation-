import subprocess
import sys

def run_script(script_name, input_text=None):
    """Runs a Python script and waits for it to complete, providing input if needed."""
    print(f"Running {script_name}...\n")

    try:
        # If input_text is provided, pass it to the script
        result = subprocess.run(
            [sys.executable, script_name], 
            input=input_text,  # Pass input to the script
            text=True, 
            capture_output=True,
            timeout=300  # Prevent infinite execution (5 minutes timeout)
        )

        # Print output and errors
        print(result.stdout)
        if result.stderr:
            print(f"Error in {script_name}:\n{result.stderr}")

    except subprocess.TimeoutExpired:
        print(f"{script_name} timed out. Terminating execution.\n")

    print(f"{script_name} completed.\n")

def main():
    """Runs all three scripts sequentially."""
    scripts = [
        ("news_browser_to_text.py", "Artificial Intelligence\n"),  # Provide input text here
        ("refrramer.py", None),  # No input needed
        ("upload.py", None)  # No input needed
    ]

    for script, input_text in scripts:
        run_script(script, input_text)
        
        # Break the loop if upload.py is running infinitely
        if script == "upload.py":
            print("Forcing termination of upload.py after execution to prevent infinite loop.")
            break

if __name__ == "__main__":
    main()
