import json
from agent_eval_core.schema import AgentTrace, Step
from agent_eval_core.assertions import *
import pandas as pd



def load_traces(path):
    with open(path) as f:
        raw_data = json.load(f)

    traces = []
    for item in raw_data:
        steps = [Step(**s) for s in item["steps"]]
        trace = AgentTrace(
            task_id=item["task_id"],
            question=item["question"],
            final_answer=item["final_answer"],
            expected_answer=item["expected_answer"],
            steps=steps,
            plan=item.get("plan"),
            expected_tools=item.get("expected_tools")
        )
        traces.append(trace)

    return traces

def evaluate(trace):
    return {
        "task_id": trace.task_id,
        "question": trace.question,
        "expected_answer": trace.expected_answer,
        "final_answer": trace.final_answer, 
        "correct_final_answer": assert_correct_final_answer(trace),
        "expected_tools_used": trace.expected_tools,
        "correct_tool_used": assert_tool_used(trace, "search"),
        "expected_plan": trace.plan,
        "trace_follows_plan": assert_trace_follows_plan(trace),
    }

if __name__ == "__main__":
    traces = load_traces("examples/example3.json")
    results = [evaluate(t) for t in traces]
    df = pd.DataFrame(results)
    df.to_csv("eval_summary.csv", index=False)

    # ----- Summary Stats -----
    summary = {
        "Total Tasks": len(df),
        "Correct Final Answers": df["correct_final_answer"].sum(),
        "Correct Final Answer %": f"{df['correct_final_answer'].mean() * 100:.1f}%",
        "Used Expected Tool": df["correct_tool_used"].sum(),
        "Used Expected Tool %": f"{df['correct_tool_used'].mean() * 100:.1f}%",
        "Followed Plan": df["trace_follows_plan"].sum(),
        "Followed Plan %": f"{df['trace_follows_plan'].mean() * 100:.1f}%"
    }

    summary_df = pd.DataFrame([summary])
    print("\n🔎 Evaluation Summary:")
    print(summary_df.to_string(index=False))
    summary_df.to_csv("eval_summary_stats.csv", index=False)

    print("\n🔎 Evaluation Details:")
    print(df)
