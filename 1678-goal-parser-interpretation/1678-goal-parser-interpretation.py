class Solution:
    def interpret(self, command: str) -> str:
        s= command.replace('()','o')
        return s.replace('(al)','al')