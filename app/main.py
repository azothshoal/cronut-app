from .matching import match_employees, Employee as MatchEmployee
from .database import get_session, Employee as DBEmployee
from .slack_utils import send_message

def run_cronut():
    session = get_session()
    db_employees = session.query(DBEmployee).all()
    
    employees = [MatchEmployee(e.name, e.email, e.department) for e in db_employees]
    matches = match_employees(employees)
    
    for match in matches:
        for employee in match:
            message = f"You've been matched with {', '.join(e.name for e in match if e != employee)} for Cronut this week!"
            send_message(employee.email, message)

if __name__ == "__main__":
    run_cronut()
