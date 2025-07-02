def analyze_diffs(events):
    total_commits = len(events)
    lines_added = sum(e['additions'] for e in events)
    lines_deleted = sum(e['deletions'] for e in events)
    return {
        "total_commits": total_commits,
        "lines_added": lines_added,
        "lines_deleted": lines_deleted
    }