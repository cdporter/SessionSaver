from pathlib import Path
import json

class Session(Path):
    def __init__(self, session_id: int, apps: List[App], base_path: str = None):
        self.session_id = session_id
        self.apps = apps
        if base_path:
            super().__init__(base_path)
    def save(self):
        session_data = {
            'session_id': self.session_id,
            'apps': [app.to_dict() for app in self.apps]
        }
        with open(self / f'session_{self.session_id}.json', 'w') as f:
            json.dump(session_data, f, indent=4)
    def load(self):
        with open(self / f'session_{self.session_id}.json', 'r') as f:
            session_data = json.load(f)
            self.session_id = session_data['session_id']
            self.apps = [App.from_dict(app_data) for app_data in session_data['apps']]
    def delete(self):
        session_file = self / f'session_{self.session_id}.json'
        if session_file.exists():
            session_file.unlink()
    