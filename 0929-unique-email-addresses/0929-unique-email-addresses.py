class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            idx = email.index('@')
            local = ""
            domain = email[idx+1:]
            for e in email[:idx]:
                if e == '+':
                    break
                elif e == '.':
                    continue
                else:
                    local += e
            address = local + '@' + domain
            # print(address)
            email_set.add(address)
        return len(email_set)