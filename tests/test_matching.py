from app.matching import match_employees, Employee

def test_matching():
    employees = [
        Employee("Alice", "alice@example.com", "HR"),
        Employee("Bob", "bob@example.com", "Engineering"),
        Employee("Charlie", "charlie@example.com", "Marketing"),
        Employee("David", "david@example.com", "HR"),
    ]
    
    matches = match_employees(employees)
    
    assert len(matches) == 2
    assert all(len(match) == 2 for match in matches)
    assert all(m[0].department != m[1].department for m in matches)
