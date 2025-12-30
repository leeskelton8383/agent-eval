def assert_tool_used(trace, tool_name: str) -> bool:
    return any(step.tool == tool_name for step in trace.steps)

def assert_correct_final_answer(trace) -> bool:
    return trace.final_answer.strip().lower() == trace.expected_answer.strip().lower()

def assert_trace_follows_plan(trace) -> bool:
    if not trace.plan:
        return True  # no plan to compare to
    actions = [step.action for step in trace.steps]
    return actions[:len(trace.plan)] == trace.plan
