class Solution:
    def simplifyPath(self, path: str) -> str:
        ele=path.split("/")
        st=[]
        for e in ele:
            if e=="." or e == "":
                continue
            if e=="..":
                if st:
                    st.pop()
            else:
                st.append(e)
        return "/" + "/".join(st)
