from agents.data_harvester import harvest_data
from agents.diff_analyst import analyze_diffs
from agents.insight_narrator import narrate_insight

def run_flow():
    events = harvest_data()
    metrics = analyze_diffs(events)
    summary = narrate_insight(metrics)
    return summary