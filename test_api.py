import os
import sys

try:
    from openai import OpenAI
except ImportError:
    print("Please install openai first: pip install openai")
    sys.exit(1)

from getpass import getpass

print("--- OpenAI API Key Tester ---")
print("This script will check if your API key is active and has credits.")

api_key = getpass("Paste your API Key here (starts with sk-): ").strip()

client = OpenAI(api_key=api_key)

try:
    print("\nAttempting to connect to OpenAI...")
    # Try a very cheap/simple call
    response = client.models.list()
    print("\nSUCCESS! Your API key is working perfectly.")
    print(f"Found {len(list(response))} models available to you.")
    
except Exception as e:
    print("\nFAILED. The API returned an error:")
    print("-" * 40)
    print(e)
    print("-" * 40)
    if "insufficient_quota" in str(e):
        print("\nDIAGNOSIS: You have run out of credits (or haven't added any yet).")
        print("SOLUTION: Go to usage settings and add $5 credit.")
    elif "invalid_api_key" in str(e):
        print("\nDIAGNOSIS: The API key is incorrect.")
