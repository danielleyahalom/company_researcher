from typing import Literal
from ..format_classes import ResearchState

def route_based_on_cluster(state: ResearchState) -> Literal["curate", "manual_cluster_selection"]:
    if state.get('chosen_cluster'):
        return "curate"
    return "manual_cluster_selection"

def route_after_manual_selection(state: ResearchState) -> Literal["curate", "cluster"]:
    if state.get('chosen_cluster'):
        return "curate"
    return "cluster"

def should_continue_research(state: ResearchState) -> Literal["research", "generate_report"]:
    # Minimum threshold for documents
    min_doc_count = 2  # Adjust this as needed 
    # Check document count
    if len(state["documents"]) < min_doc_count:
        return "research"
    return "generate_report"

# Define the conditional edge function based on report grade
def route_based_on_evaluation(state: ResearchState) -> Literal["research", "publish"]:
    evaluation = state.get("eval")
    
    # If the report has critical gaps, route to research for additional questions; otherwise, proceed to format
    return "research" if evaluation.grade == 1 else "publish"
