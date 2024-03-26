![Karen Spärck Jones](../../assets/images/heroes/karen_spark_jones.webp)
<p align="right"><sub><a href="https://en.wikipedia.org/wiki/Karen_Sp%C3%A4rck_Jones" target="_blank">Karen Spärck Jones</a> (AI Generated Artwork)</sub></p>

# Engineering Feedback

## The Importance of Submitting Engineering Feedback at Repo Racers

Engineering Feedback is vital for capturing the "voice of the customer." It serves as a crucial mechanism for providing actionable insights, enabling continuous improvement of our platform and services to maximize productivity for all users.

> It's important to note that Engineering Feedback is an asynchronous method for capturing and aggregating common challenges across multiple users and projects. If there's a need to report a service outage or an urgent bug, please submit a support ticket through the appropriate channels and reference this ticket in any subsequent feedback.

Even if feedback has been communicated directly to our team or shared through online platforms, submitting it through Repo Racers Engineering Feedback is essential. This allows us to consolidate feedback from various projects, aiding in prioritization and addressing common concerns effectively.

## When to Submit Engineering Feedback

Providing high-quality, actionable Engineering Feedback is an ongoing responsibility throughout all projects. It's best to submit feedback regularly, rather than waiting to compile it at the end of a project.

You should document feedback when issues or challenges are encountered to capture the details while they're fresh. The project team will then determine the priority and timing for submitting this feedback into our feedback system during each project phase.

## Criteria for High-Quality Engineering Feedback

Effective engineering feedback clearly conveys the customer's challenges, the impact of these issues, and any possible solutions or workarounds. It should be:

- **Goal-Oriented**: Clearly states the objectives the customer is trying to achieve.
- **Specific**: Provides detailed information about the encountered scenario, observation, or challenge.
- **Actionable**: Includes necessary details to understand and address the feedback.

### Examples of Effective Engineering Feedback

Here's how feedback can evolve to meet the standards of high-quality engineering feedback:

| Stage                       | Feedback Evolution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Initial feedback            | Service Bus Trigger is slow for in-order processing scenarios                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Making it **Goal-Oriented** | **A request for batch receiving for the Service Bus trigger with sessions enabled to support higher throughput messaging. The aim is to maximize message processing speed with minimal latency and maintain order.**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Adding **Specifics**        | The scenario involved receiving **250 messages/second from 50 sources, each requiring message order with minimal latency, using a Service Bus topic with sessions for order. Batch receiving, which is not available in the current Service Bus Trigger setup, is needed.**                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Making it **Actionable**    | In a specific scenario, there was a need to process 250 messages/second from 50 sources with message ordering and minimal latency, using a Service Bus topic with sessions. **According to best practices, batch receiving significantly improves performance but is not supported by the current Service Bus Trigger. The impact led to exploring alternatives such as containers over traditional functions. The ideal solution would enable batch and non-batch processing for Service Bus sessions across all supported languages in our platform.**                                                                                                                         |

For more detailed examples, refer to [Feedback Examples](feedback_examples.md).

## How to Submit Engineering Feedback

Please consult the [Engineering Feedback Guidance](feedback_guidance.md) for instructions on submitting thorough and effective feedback, ensuring efficient processing and triage.
