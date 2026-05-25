import sys

while True:
    current_drivers = input(
        "Would you like to start this program with the current Formula 1 2025 drivers?  "
    ).strip().lower()
    if current_drivers == "no":
        print("Please edit the drivers.txt with the drivers you wish to use.")
        print("Exiting program. Run again when ready.")
        sys.exit()
    elif current_drivers == "yes":
        print("Great, loading current F1 drivers as of November 2025")
        break
    else:
        print("Invalid input! Please type 'yes' or 'no'")

drivers = []
drivers_file = "drivers.txt"

try:
    with open(drivers_file) as file:
        for lineno, line in enumerate(file, start=1):
            if not line.strip():
                continue

            parts = line.strip().split(",")
            if len(parts) != 4:
                raise ValueError(f"Line {lineno}: expected 4 comma-separated fields, got {len(parts)}: {line.strip()}")
            driver, team, country, driver_number = parts
            
            driver = driver.strip()
            if not driver:
                raise ValueError(f"Line {lineno}: Driver name cannot be empty")
            if driver.isdigit():
                raise ValueError(f"Line {lineno}: Driver name cannot be a number: {driver}")
            if len(driver) < 2:
                raise ValueError(f"Line {lineno}: Driver name seems too short: {driver}")

            team = team.strip()
            if not team:
                raise ValueError(f"Line {lineno}: Team name cannot be empty")
            if team.isdigit():
                raise ValueError(f"Line {lineno}: Team name cannot be a number: {team}")

            country = country.strip().upper()
            if not country:
                raise ValueError(f"Line {lineno}: Country code cannot be empty")
            if country.isdigit():
                raise ValueError(f"Line {lineno}: Country code cannot be a number: {country}")
            if len(country) != 3 or not country.isalpha():
                raise ValueError(f"Line {lineno}: Invalid country code: {country} Must be three letters.")
            
            driver_number = driver_number.strip()
            if not driver_number:
                raise ValueError(f"Line {lineno}: Driver number cannot be empty")
            if not driver_number.isdigit() or not (1 <= int(driver_number) <= 99):
                raise ValueError(f"Line {lineno}: Driver number must be a number between 1 and 99: {driver_number}")


            drivers.append({
                "Driver": driver,
                "Team": team,
                "Nationality": country,
                "Driver_Number": driver_number
            })

except FileNotFoundError:
    print("Error: drivers.txt file not found.")
    sys.exit()
except Exception as e:
    print(f"Error handling drivers.txt:{e}")
    sys.exit()

def lap_time():
    while True:
        lap = input("Enter lap time (MM:SS.sss) or NT for no time set:  ").strip()
        if lap.upper() == "NT":
            return None
        try:
            minutes, seconds = lap.split(":")
            minutes = int(minutes)
            seconds = float(seconds)
            if minutes < 0 or seconds < 0 or seconds >= 60:
                raise ValueError
            return minutes, seconds
        except ValueError:
            print("Invalid format. Please use MM:SS.sss e.g., 01:30.231")

def convert_to_seconds(minutes, seconds):
    if minutes is None:
        return None
    return minutes * 60 + seconds

def format_lap_time(time):
    if time is None:
        return "No Time Set"
    minutes = int(time // 60)
    seconds = time % 60
    return f"{minutes}:{seconds:06.3f}"

def run_session(drivers, session_name, cutoff):
    print(f"\n--- {session_name} ---")
    results = []
    for driver in drivers:
        print(f"Enter lap time for driver {driver['Driver_Number']} - {driver['Driver']} ({driver['Team']}):")
        lap = lap_time()
        if lap is None:
            total_time = None
        else:
            minutes, seconds = lap
            total_time = convert_to_seconds(minutes, seconds)
        results.append((driver["Driver"], total_time))

    results.sort(key=lambda x: (x[1] is None, x[1] if x[1] is not None else 0))

    print(f"\nResults for {session_name}:")
    for i, (driver, time) in enumerate(results):
        print(f"{i+1}. {driver} - {format_lap_time(time)}")
    return [d for d, _ in results[:cutoff]]

q2_drivers = run_session(drivers, "Qualifying 1", 15)
q3_drivers = run_session([d for d in drivers if d["Driver"] in q2_drivers], "Qualifying 2", 10)
q3_results = run_session([d for d in drivers if d["Driver"] in q3_drivers], "Qualifying 3", 10)

