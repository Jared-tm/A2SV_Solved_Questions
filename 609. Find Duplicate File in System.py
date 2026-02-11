class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
    
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            
            for file in parts[1:]:
                name, content = file.split("(")
                content = content[:-1] 
                full_path = f"{directory}/{name}"
                hashmap[content].append(full_path)
                
        return [group for group in hashmap.values() if len(group) > 1]
            