class Solution:
    def maskPII(self, s: str) -> str:
        s = s.strip()
        # Email case
        if "@" in s:
            name, domain = s.split("@", 1)
            name = name.lower()
            domain = domain.lower()
            # first letter, five stars, last letter
            return name[0] + "*****" + name[-1] + "@" + domain

        # Phone number case
        digits = re.sub(r"\D", "", s)  # remove non-digits
        local = "***-***-" + digits[-4:]
        country_len = len(digits) - 10
        if country_len == 0:
            return local
        return "+" + ("*" * country_len) + "-" + local
