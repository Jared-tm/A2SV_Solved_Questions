class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = Counter()
        for cpdomain in cpdomains:
            count_str, domain = cpdomain.split()
            count = int(count_str)
            fragments = domain.split('.')
            
            for i in range(len(fragments)):
                subdomain = ".".join(fragments[i:])
                counts[subdomain] += count

        return [f"{cnt} {dom}" for dom, cnt in counts.items()]
        