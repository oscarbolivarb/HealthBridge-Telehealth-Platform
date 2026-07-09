# Benchmark Report and System Design Justification 

### Benchmark Analysis

The performance testing was completed using Apache JMeter to evaluate the HealthBridge system under two different workloads. The two benchmark tests were completed using the same HTTP request so the results could be compared.  

The first benchmark used 10 users, a 5 second ramp up period and 5 loops which created a total of 50 requests. The second benchmark increased the workload to 50 users a 1 second ramp up period and 10 loops creating a total of 500 requests. 

| Metric | Benchmark 1 | Benchmark 2 |
| --------- |------------------ |------------------ |
| Total Requests | 50 | 500 |
| Average Response Time | 49 ms | 80 ms |
| Throughput | 10.9 requests/sec | 381.7 requests/sec |
| Error Rate | 0.00% | 0.00% |

The test were repeated using the same JMeter test plan to make sure that the results were consistent. The test plan included a thread group, an HTTP request sampler, the summary report and an aggregate listeners to collect the performance results. Both of these test finish with no errors, which showed that the request was handled successfully even with a large number of users.

System Design Justification

The HealthBridge platform is designed to support many patients, healthcare providers and administrators at the same time. To make the system easier to maintain and be able to handle more users, the design uses modular services, database indexing and caching for information that is often requested. These improvements help reduce unnecessary work, improve response time and make future updates easier without affecting the entire system.

Another important aspect in the design is accessibility, since some users can have older devices, slower internet connections or use assistive technologies like screen readers. So a better system, performer can help these users by reducing loading times, but it is also important to make sure that the accessibility features remain available such as keyboard navigation, alternative text for images and clear page layout helps make the system easier for everyone to use. 

One tradeoff is improving performance such as caching, buy at the same time this can make the system more complex and it can require extra maintenance. Even with this additional steps and cost, these improvements are worth it because they allow the system to support more users while it provides a better experience.

In the future, additional benchmarking should be done after additional optimization techniques have been added so that the new results can be compared to the original benchmark to show how the system has improved.    
