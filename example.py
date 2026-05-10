from Session import Session
from App import App
from pathlib import Path

# Create some apps
app1 = App("Visual Studio Code", [])
app2 = App("Chrome Browser", [])

# Create a session with those apps
apps = [app1, app2]
session = Session(session_id=1, apps=apps, base_path=str(Path.cwd()))

# Save the session to disk
print(f"Saving session {session.session_id}...")
session.save()
print("Session saved successfully!")

# Load the session back
print(f"Loading session {session.session_id}...")
session.load()
print(f"Loaded session with {len(session.apps)} apps")
