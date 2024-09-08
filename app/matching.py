from typing import List, Tuple

class Employee:
    def __init__(self, name: str, email: str, department: str):
        self.name = name
        self.email = email
        self.department = department

def match_employees(employees: List[Employee]) -> List[Tuple[Employee, ...]]:
    matches = []
    unmatched = employees.copy()
    
    while len(unmatched) > 1:
        employee = unmatched.pop(0)
        for i, potential_match in enumerate(unmatched):
            if employee.department != potential_match.department:
                matches.append((employee, potential_match))
                unmatched.pop(i)
                break
        else:
            unmatched.append(employee)
    
    # Handle remaining unmatched employees
    if len(unmatched) == 3:
        matches.append(tuple(unmatched))
    elif len(unmatched) == 2:
        matches.append(tuple(unmatched))
    elif len(unmatched) == 1:
        # Add to an existing pair if possible
        for i, match in enumerate(matches):
            if all(unmatched[0].department != m.department for m in match):
                matches[i] = match + (unmatched[0],)
                break
        else:
            # If no suitable pair found, create a new pair with same department
            matches.append((unmatched[0], employees[0]))
    
    return matches
