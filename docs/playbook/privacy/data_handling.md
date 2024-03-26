# Privacy and Data at Repo Racers

## Goal

The aim of this section is to outline best practices in privacy fundamentals for projects with significant data components or sections that might involve data handling.

**What it is not**: This document isn't a comprehensive checklist for how our users or readers should manage data in their environments, nor does it supersede any Repo Racers or user-specific policies for data management, data protection, and information security.

## Introduction

Repo Racers operates on a foundation of trust. Our users entrust us to maintain the highest standards in data handling.
The protection of our users' data is a shared responsibility between Repo Racers and our users;
it is imperative for both parties to collaborate in adhering to the guidelines set forth here.

During projects, developers should follow best practices and guidance for data management across all phases of development. This guidance is not intended to dictate user data management practices. **It does not override**:

- Repo Racers' Information Security Policy
- Any applicable Data Protection Addenda

## 5 W's of Data Handling

When engaged in a project, it's crucial to consider the following 5 **W**'s:

- **Who** – identifies the parties having access to the data, and with whom the data or developed models will be shared.

- **What** – clarifies the data shared with us, under what premises, and expectations. It's essential for users to be explicit about the relevance of their data to the project's overarching goals.

- **Where** – determines the storage location of the data and the legal jurisdiction governing it. This aspect is especially critical in regions with unique privacy laws and when considering legal requests for data access.

- **When** – specifies the duration of data access. Ensuring that access to data doesn't linger post-engagement is key, alongside predefined data retention policies.

- **Why** – underscores the rationale behind data access. Clarifying the purpose and usage restrictions is fundamental to maintaining trust and ensuring data is used solely for its intended purpose.

Adhering to these guidelines ensures that data is utilized appropriately, fostering trust.

## Managing Data in Engagements

Data must always remain within customer-controlled environments. Contractors or project members should not access complete data sets but should work with limited, necessary data, prioritizing the following approaches:

1. Avoid direct work with production data; data should be prepared and anonymized according to the guidelines below before processing.
2. Implement [data minimization](https://www.forbes.com/sites/bernardmarr/2016/03/16/why-data-minimization-is-an-important-concept-in-the-age-of-big-data/#3fb711e91da4) principles to limit the scope of potential errors, working only with the data essential for project objectives.
3. Utilize synthetic data for project requirements. If synthetic data proves insufficient, request anonymized data with minimal re-identification risk.
4. Choose a diverse, limited data set in alignment with Data Minimization principles, minimizing data quantity to meet project needs.

Prior to data work, ensure up-to-date OS patches and proper permission settings, without open internet access.

Repo Racers collaborates with customers to identify necessary data for each engagement. Should production data access become necessary, a review with lead personnel and customer consultation for audit mechanisms is required.

Production data must be restricted to approved project members and must not leave the customer-controlled environment.

Customers should provide Repo Racers with the required data within their managed locations, enabling activity logging to monitor access and actions. Repo Racers will inform the customer upon completion, advising on data destruction if no longer needed.

### Guiding Principles for Data Handling in Engagements

- Direct access to production data is prohibited.
- Clearly define the intended purpose for data usage in the project.
- Ensure only approved team members have access to production data copies.
- Actively manage and dispose of unnecessary data copies.
- Avoid transferring production data out of the customer-controlled environment.
- Limit data to the minimum necessary for project goals.

### Considerations for Data Work

- What data is necessary?
- What legal grounds justify this data processing?
- If acting as a processor, what are our contractually defined responsibilities?
- Are contractual amendments needed?
- How can we limit data proliferation?
- What security measures protect this data?
- What is the protocol for data breaches?
- How does this data usage benefit the data subject?
- What is the data's lifecycle?
- Is it necessary to link this data to individuals?
- Can this data be anonymized for future use?
- How are we ensuring compliance with data subject rights?

## Summary

Focusing only on necessary data for specific objectives is paramount, especially when handling personal data. Being mindful of data adequacy, relevance, and limitations relative to processing purposes aligns with best practices, particularly under regulations like HIPAA, GDPR, and CCPA. Awareness and adherence to any relevant regulations, along with the [seven principles of privacy by design](https://www.onetrust.com/blog/principles-of-privacy-by-design/)
