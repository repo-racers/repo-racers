# Machine Learning Fundamentals at ISE

This guideline documents the Machine Learning (ML) practices in ISE. ISE works with customers on developing ML models and putting them in production, with an emphasis on engineering and research best practices throughout the project's life cycle.

## Goals

* Provide a set of ML practices to follow in an ML project.
* Provide clarity on ML process and how it fits within a software engineering project.
* Provide best practices for the different stages of an ML project.

## How to use these fundamentals

* If you are starting a new ML project, consider reading through the [general guidance documents](#general_guidance).
* For specific aspects of an ML project, refer to the guidelines for different [project phases](#ml_project_phases).

## ML Project phases

The diagram below shows different phases in an ideal ML project. Due to practical constraints and requirements, it might not always be possible to have a project structured in such a manner, however best practices should be followed for each individual phase.

![Project flow](images/flow.png)

* **[Envisioning](ml_problem_formulation_envisioning.md)**: Initial problem understanding, customer goals and objectives.
* **[Feasibility Study](ml_feasibility_study.md)**: Assess whether the problem in question is feasible to solve satisfactorily using ML with the available data.
* **Model Milestone**: There is a basic model that is achieving the minimum required performance, both in terms of ML performance and system performance. Using the knowledge gathered to this milestone, define the scope, objectives, high-level architecture, definition of done and plan for the entire project.
* **[Model(s) experimentation](ml_experimentation.md)**: Tools and best practices for conducting successful model experimentation.
* **Model(s) Operationalization**: [Model readiness for production](ml_model_checklist.md) checklist.

## General guidance

* [ML Process Guidance](ml_proposed_process.md)
* [ML Fundamentals checklist](ml_fundamentals_checklist.md)
* [Data Exploration](ml_data_exploration.md)
* [Agile ML development](ml_project_management.md)
* [Testing Data Science and ML Ops code](ml_testing.md)
* [Profiling Machine Learning and ML Ops code](ml_profiling.md)
* [Responsible AI](responsible_ai.md)
* [Program Management for ML projects](ml_tpm_guidance.md)

## References

* [Model Operationalization](https://github.com/Microsoft/MLOps)
