#!/usr/bin/env python3
import os
import json

# Define where the config will live
CONFIG_DIR = os.path.expanduser("~/.aws_automation_tools")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def load_config():
    """
    Load the existing configuration from CONFIG_FILE.
    If the file doesn't exist or is incomplete, initialize the keys.
    """
    config = {}
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
        except json.JSONDecodeError:
            print("Warning: Existing config file is invalid. Starting fresh.")

    # Ensure the necessary keys exist.
    config.setdefault("region", "")
    config.setdefault("account_ids", {})
    config.setdefault("kms_keys", {})

    return config

def save_config(config):
    """
    Save the configuration to CONFIG_FILE. Create the directory if needed.
    """
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
    print(f"Configuration saved at {CONFIG_FILE}")

def set_region(config):
    """
    Prompt for a default AWS region and store it.
    """
    region = input("Enter the default region (e.g. eu-west-1): ").strip()
    if region:
        config["region"] = region
        print(f"Default region set to: {region}")
    else:
        print("No region entered; skipping.")

def add_account(config):
    """
    Prompt for an account alias and account ID and store it.
    """
    alias = input("Enter the account alias (e.g. NONPROD): ").strip()
    if not alias:
        print("Account alias cannot be empty.")
        return
    account_id = input("Enter the account ID: ").strip()
    if account_id:
        config["account_ids"][alias] = account_id
        print(f"Added account {alias}: {account_id}")
    else:
        print("No account ID entered; skipping.")

def add_kms_key(config):
    """
    Prompt for a KMS key alias and its ARN and store it.
    """
    alias = input("Enter the KMS key alias (e.g. NONPROD): ").strip()
    if not alias:
        print("KMS key alias cannot be empty.")
        return
    kms_arn = input("Enter the KMS key ARN: ").strip()
    if kms_arn:
        config["kms_keys"][alias] = kms_arn
        print(f"Added KMS key {alias}: {kms_arn}")
    else:
        print("No KMS key ARN entered; skipping.")

def main():
    config = load_config()

    while True:
        print("\n--- AWS Automation Tools Setup ---")
        print("Choose an option to configure:")
        print("1. Set default region")
        print("2. Add an account")
        print("3. Add a KMS key")
        print("4. Quit and save")
        choice = input("Enter your choice [1-4]: ").strip()

        if choice == "1":
            set_region(config)
        elif choice == "2":
            add_account(config)
        elif choice == "3":
            add_kms_key(config)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    save_config(config)

if __name__ == "__main__":
    main()
