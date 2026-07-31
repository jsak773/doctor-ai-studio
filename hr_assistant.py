import sqlite3
from typing import List, Dict, Any
from database import DB_PATH

class HRAssistant:
    def __init__(self):
        pass

    def get_all_staff(self) -> List[Dict[str, Any]]:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM staff WHERE status = 'ACTIVE'")
            return [dict(row) for row in cursor.fetchall()]

    def add_staff(self, name: str, role: str, phone: str, shift_timing: str) -> Dict[str, Any]:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO staff (name, role, phone, shift_timing, status)
                VALUES (?, ?, ?, ?, 'ACTIVE')
            ''', (name, role, phone, shift_timing))
            conn.commit()
            new_id = cursor.lastrowid
            return {"id": new_id, "name": name, "role": role, "phone": phone, "shift_timing": shift_timing}

if __name__ == "__main__":
    hr = HRAssistant()
    print("Staff:", hr.get_all_staff())
