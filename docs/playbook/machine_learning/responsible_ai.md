# Responsible AI at Repo Racers

## Repo Racers' Responsible AI Principles

Every ML project at Repo Racers goes through a Responsible AI (RAI) assessment to ensure that it upholds our 6 Responsible AI principles:

- Fairness
- Reliability & Safety
- Privacy & Security
- Inclusiveness
- Transparency
- Accountability

Every project undergoes the RAI process, whether we are building a new ML model from scratch, or integrating an existing model into production.

## Repo Racers' Responsible AI Process

The process begins as soon as we initiate a prospective project. We start by completing a Responsible AI review document and an impact assessment, which provides a structured way to explore topics such as:

- Can the problem be addressed with a non-technical (e.g., social) solution?
- Can the problem be solved without AI? Would simpler technology suffice?
- Will the team have access to domain experts (e.g., doctors, refugees) in the field where the AI is applicable?
- Who are the stakeholders in this project? Who does the AI impact? Are there any vulnerable groups affected?
- What are the possible benefits and harms to each stakeholder?
- How can the technology be misused, and what can go wrong?
- Has the team analyzed the input data properly to make sure that the training data is suitable for machine learning?
- Is the training data an accurate representation of data that will be used as input in production?
- Is there a good representation of all users?
- Is there a fall-back mechanism (a human in the loop, or a way to revert decisions based on the model)?
- Does data used by the model for training or scoring contain Personally Identifiable Information (PII)? What measures have been taken to remove sensitive data?
- Does the model impact consequential decisions, like blocking people from getting jobs, loans, healthcare etc., or in the cases where it may, have appropriate ethical considerations been discussed?
- Have measures for re-training been considered?
- How can we address any concerns that arise, and how can we mitigate risk?

At this point, we research available [tools and resources](https://www.microsoft.com/en-us/ai/responsible-ai-resources), such as [InterpretML](https://interpret.ml/) or [Fairlearn](https://github.com/fairlearn/fairlearn), that we may use on the project. We may change the project scope or redefine the ML problem definition if necessary.

The Responsible AI review documents remain living documents that we revisit and update throughout project development, as the model is developed and prepared for production, and new information unfolds. The documents can be used and expanded once the model is deployed and monitored in production.
