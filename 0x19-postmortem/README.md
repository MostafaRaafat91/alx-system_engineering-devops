---

# Postmortem: Web Application Outage

## Issue Summary
- **Duration**: May 24, 2024, 10:00 AM to 2:00 PM (UTC-7)
- **Impact**: The e-payment system (PayEasy) experienced a complete outage during peak hours.
  - Users were unable to make payments or access their accounts.
  - Approximately 30% of active users were affected.
- **Root Cause**: A misconfigured database connection pool caused resource exhaustion.

## Timeline
- **10:00 AM**: Issue detected by monitoring alerts. Latency and error rates spiked.
- **10:15 AM**: Engineers noticed the problem and initiated investigation.
- **10:30 AM**: Assumed root cause: Database server overload due to increased traffic.
- **11:00 AM**: Investigated database performance metrics, but no clear evidence.
- **11:30 AM**: Misleading path: Focused on frontend servers, suspecting load balancerCertainly! Let's continue with the postmortem
---

# Postmortem: Web Application Outage (Continued)

## Corrective and Preventative Measures (Continued)
- **Improvements/Fixes**:
  4. **Database Connection Pool Testing**:
     - Implement automated tests to verify connection pool behavior under load.
  5. **Circuit Breaker Pattern**:
     - Introduce a circuit breaker mechanism to prevent cascading failures.
  6. **Graceful Degradation**:
     - Implement fallback mechanisms for critical services during outages.
- **Tasks**:
  - **Documentation Update**:
    - Document the incident, root cause, and resolution for future reference.
  - **Incident Communication**:
    - Notify affected users about the outage and resolution.
  - **Training**:
    - Conduct training sessions on incident response and debugging best practices.
  - **Monitoring Enhancements**:
    - Add monitoring for connection pool health and resource utilization.

---
