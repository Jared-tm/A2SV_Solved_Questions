"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        """
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
        emp_map = {emp.id: emp for emp in employees}
        
        def dfs(current_id):
            employee = emp_map[current_id]
            total_importance = employee.importance

            for sub_id in employee.subordinates:
                total_importance += dfs(sub_id)
                
            return total_importance
        
        return dfs(id)