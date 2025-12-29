# Trace-Based Agent Evaluation Examples

This repository contains a set of concrete, trace-based evaluation examples that explore how multi-step AI agents can be evaluated beyond simple pass/fail outcomes. Rather than proposing a formal evaluation framework, the goal of this work is to provide practical, inspectable examples of how agent traces can be used to understand both *what* an agent did and *why* it succeeded or failed.

## Project Overview

The examples are organized into three illustrative phases, each building on the previous one by incorporating richer trace information and more detailed evaluation signals.

### Phase 1 – Execution and Correctness Checks

This phase focuses on basic execution validity and outcome correctness. It verifies that the agent produces a final answer, invokes tools when required, and uses the correct tools for the task. The intent is to ensure that the agent’s output is evaluable and that obvious execution errors are caught early.

### Phase 2 – Trajectory Quality Evaluation

In Phase 2, evaluation moves beyond final answers to examine the agent’s execution trace. An LLM is used as a judge to assess how well the agent’s step-by-step trajectory aligns with expected reasoning or actions. The LLM produces a quality score and an explanation, providing insight into the coherence and appropriateness of the agent’s planning and execution.

### Phase 3 – Multi-Span Task Diagnostics

Phase 3 extends trajectory-based evaluation to tasks composed of multiple conceptual spans. Expected reasoning steps are compared against the agent’s trace to identify issues such as missing steps or structural gaps. Explicit reason codes are attached to these failures to explain *why* a task succeeded or failed, emphasizing interpretability and diagnostic value rather than simple correctness.

## Dataset

All examples use a synthetic, supply-chain-oriented dataset designed to simulate realistic multi-step decision-making tasks. The dataset evolves across phases to include progressively richer trace information, enabling more detailed evaluation and diagnostics.

## Purpose

The purpose of this project is not to define a comprehensive agent evaluation framework, but to demonstrate practical patterns for trace-based evaluation. These examples show how trace data can be progressively enriched to move from basic execution checks to interpretable diagnostics of agent behavior, helping explain why an agent’s outcome was correct or incorrect.
