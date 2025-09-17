class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        total_views = defaultdict(int)
        best_videos = {}

        for c, vid, v in zip(creators, ids, views):
            total_views[c] += v

            if c not in best_videos:
                best_videos[c] = (v, vid)
            else:
                curr_views, curr_vid = best_videos[c]
                if v > curr_views or (v == curr_views and vid < curr_vid):
                    best_videos[c] = (v, vid)

        max_views = max(total_views.values())

        results = []
        for c in total_views:
            if total_views[c] == max_views:
                results.append([c, best_videos[c][1]])
        
        return results
