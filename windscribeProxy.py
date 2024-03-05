import subprocess
import random
from retry import retry

"""

# Installation Process

    windscribe - https://windscribe.com/

    commands - sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key FDC247B7

    echo 'deb https://repo.windscribe.com/ubuntu bionic main' | sudo tee /etc/apt/sources.list.d/windscribe-repo.list

    sudo apt-get update

    sudo apt-get install windscribe-cli

    windscribe login/ windscribe status/windscribe connect/windscribe disconnect/windscribe locations/windscribe connect 'shortName'/windscribe logout/windscribe --help

"""
def getCountry():
    countries = [
                    "US-C",
                    "US-C",
                    "US",
                    "US",
                    "US",
                    "US",
                    "US",
                    "US",
                    "US-W",
                    "US-W",
                    "CA",
                    "CA",
                    "CA",
                    "CA-W",
                    "CA-W",
                    "FR",
                    "FR",
                    "DE",
                    "DE",
                    "NL",
                    "NL",
                    "NL",
                    "NO",
                    "RO",
                    "CH",
                    "CH",
                    "GB",
                    "GB",
                    "TR",
                    "HK"
                ]
    return random.choice(countries)
@retry(tries=6)
def windscribeLogin():
    username = "vmtech"
    password = "Power@1234"
    command = "windscribe login"

    # Combine username and password with newline separator
    input_string = f"{username}\n{password}"

    # Execute the command
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Pass username and password to the command
    stdout, stderr = process.communicate(input=input_string.encode())
@retry(tries=6)
def windscribeConnect():
    print("Connecting to new proxy server...")
    country = getCountry()
    connection = subprocess.run(f"windscribe connect {country}", shell=True, capture_output=True, text=True)
    return connection.stdout.split("Your IP changed from")[-1].split("to")[-1].split("\n")[0]

@retry(tries=6)
def windscribeStatus():
    result = subprocess.run("windscribe status", shell=True, capture_output=True, text=True)
    if "DISCONNECTED" in result.stdout.splitlines():
        return False
    else:
        return True






