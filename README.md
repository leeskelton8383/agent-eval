# Trace-Based Agent Evaluation Examples

This repository demonstrates two complementary approaches to evaluating multi-step AI agents:

1. **Notebook-Based Proof of Concept (Phases 1–3)**: A progressive exploration of trace-based evaluation strategies, showcasing increasingly detailed analysis across execution, trajectory, and multi-span diagnostics.
2. **Reusable Evaluation Harness**: A standalone Python library and script (`run_eval.py`) that can evaluate structured agent traces against expected outcomes using clear assertion logic.

---

## Notebook-Based Exploration (Phases 1–3)

Notebook: eval_demo.ipynb.
These examples provide inspectable, narrative-style evaluations across three phases, each building on the prior with richer insights.

### Phase 1 – Execution and Correctness Checks

* Ensures the agent produces a final answer
* Verifies whether tools are used when required
* Detects basic execution errors early

### Phase 2 – Trajectory Quality Evaluation / LLM-as-Judge

* Examines whether the agent's actions follow a coherent and appropriate step-by-step plan
* Uses an LLM to score and explain reasoning quality

### Phase 3 – Multi-Span Task Diagnostics

* Analyzes complex tasks composed of multiple conceptual spans
* Compares actual trace against an expected step plan
* Assigns reason codes to identify structural or logical gaps

---

## Reusable Evaluation Harness

The `run_eval.py` script evaluates a batch of structured agent traces stored in a single JSON file. It applies deterministic assertions to each trace and outputs both detailed and summary results.

### 🔧 Core Assertions (in `agent_eval_core/assertions.py`)

* `assert_correct_final_answer()`
* `assert_tool_used()`
* `assert_trace_follows_plan()`

### 🧪 Dataset Format (see `examples/example_dataset.json`)

Each trace is a dictionary with:

* `task_id`, `question`, `expected_answer`, `final_answer`
* `steps`: list of actions with tool use and observations
* `plan`: expected sequence of reasoning steps
* `expected_tools`: expected tool usage for task

### 📊 Output

* `eval_summary.csv`: Per-task evaluation results
* `eval_summary_stats.csv`: Overall summary (accuracy, plan adherence, tool use)

### 🧠 Optional Agent Integration

* You may use real or stub agents to produce traces dynamically.
* Example format and utilities are provided to simulate or log execution traces.

---

## Getting Started

1. Inspect and run the notebooks to understand different evaluation dimensions.
2. Run the harness script or example notebook:

```bash
python run_eval.py or eval_harness_test.ipynb

```
