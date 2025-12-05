# FSCS.py
class FCFSAlgorithm:
    def solve(self, processes):
        top = 0
        ct, tat, wt = [], [], []
        for i, p in enumerate(processes):
            at = float(p['at'])
            bt = float(p['bt'])
            if top < at:
                top = at + bt
            else:
                top += bt
            ct.append(top)
            tat.append(top - at)
            wt.append(tat[-1] - bt)
        results = []
        for i, p in enumerate(processes):
            results.append({
                'pid': p['pid'],
                'at': p['at'],
                'bt': p['bt'],
                'ct': ct[i],
                'tat': tat[i],
                'wt': wt[i]
            })
        avg_tat = round(sum(tat)/len(processes),4)
        avg_wt = round(sum(wt)/len(processes),4)
        return {"data": results, "avgTat": avg_tat, "avgWt": avg_wt}
