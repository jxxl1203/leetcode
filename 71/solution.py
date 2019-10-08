class Solution(object):
    def simplifyPath(self, path):
        s = ["", ""]
        for p in path.split("/"):
            if p == "":
                continue
            if p == "..":
                if s.pop() == "":
                    s.append("")
                    continue
            elif p == ".":
                continue
            else:
                s.append(p)
        res = "/".join(s)
        while res.find("//") > -1:
                res = res.replace("//", "/")
        return res


a = Solution()
print a.simplifyPath("/a//b////c/d//././/..")