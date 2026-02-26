class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # Split the path by slashes to isolate directory names and commands
        parts = path.split('/')
        
        for part in parts:
            if part == '..':
                # Go up one directory if possible by popping the stack
                if stack:
                    stack.pop()
            elif part and part != '.':
                # Push valid directory names onto the stack
                # 'part' implicitly checks for empty strings caused by consecutive slashes
                stack.append(part)
                
        # Reconstruct and return the canonical path
        return '/' + '/'.join(stack)
