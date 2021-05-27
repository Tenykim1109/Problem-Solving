class Solution:
    from copy import deepcopy
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        ans = 0
        langDict = {}
        notConnected = set([])   
        
        for friend1, friend2 in friendships:
            if not set(languages[friend1-1]) & set(languages[friend2-1]):
                notConnected.add(friend1)
                notConnected.add(friend2)

        for friend in notConnected:
            for lang in languages[friend - 1]:
                if lang not in langDict.keys():
                    langDict[lang] = [friend]
                else:
                    langDict[lang].append(friend)

        for item in langDict.values():
            if len(item) > ans:
                ans = len(item)
        
        return len(notConnected) - ans