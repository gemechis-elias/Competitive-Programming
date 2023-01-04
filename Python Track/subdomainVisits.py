class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = collections.Counter()
        for cd in cpdomains:
            visits, domain_ = cd.split()
            count[domain_] += int(visits)
            for i in range(len(domain_)):
                if domain_[i] == '.':
                    count[domain_[i + 1:]] += int(visits)
        return ["%d %s" % (count[domain], domain) for domain in count]
