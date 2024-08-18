<<<<<<< HEAD
# Postmortem: Web Stack Outage Due to Database Deadlock

## Issue Summary (For the Execs)
+ Duration: 2 hours 30 minutes (felt like an eternity)
+ Start Time: 2024-07-15 09:45 AM PST (when the coffee was still hot)
+ End Time: 2024-07-15 12:15 PM PST (lunch was definitely cold)   

## Impact:
+ Service: E-commerce website (the one that makes us money) was playing hide-and-seek with customers
+ User Experience: Think spinning wheels, failed transactions, and timeouts. Frustration levels? Over 9000!
+ Affected Users: 70% of our lovely customers (we owe them a virtual hug)
+ Root Cause: Database deadlock (imagine a traffic jam inside the database)  


## Timeline (A Quick Recap)
+ 09:45 AM: Customer support phones started ringing like crazy
+ 09:50 AM: Monitoring alerts went off (thank goodness for those!)
+ 09:55 AM: DevOps team jumped in, thinking it was a server or network issue (false alarm!)
+ 10:15 AM: Database metrics started looking suspicious (uh-oh)
+ 10:30 AM: Database team to the rescue!
+ 11:00 AM: Tried some query optimization (didn't work, darn it)
+ 11:30 AM: Escalated to the big bosses (gulp)
+ 12:00 PM: Manually terminated the deadlocked transactions (like untangling a knot)
+ 12:15 PM: Website slowly came back to life (phew!)   


## Root Cause and Resolution (The Nitty-Gritty)
+ Cause: Concurrent transactions were fighting over the same data, causing a deadlock (like two kids fighting over the same toy)
+ Resolution: Killed the deadlocked transactions (sorry, transactions!) and freed up the database   


## Corrective and Preventative Measures (Let's Not Do This Again)  
### Areas for Improvement
+ Database design: Need to make it more deadlock-proof
+ Monitoring and alerting: Let's get notified sooner next time
+ Incident response: Better communication between teams, please!  


### Specific Tasks (TODO List)
+ Code review: Refactor order processing logic (time for some code magic)
+ Database configuration: Tweak some parameters (get those locks under control)
+ Monitoring: Add more metrics (knowledge is power)
+ Alerting: Set up alerts for deadlocks (don't let them sneak up on us)
+ Incident response playbook: Update it with deadlock procedures
+ Training: Let's educate everyone on database best practices
+ Let's learn from this and make our systems even more resilient! 💪


=======
## 0x19-postmortem  
>>>>>>> 22f09c8d3b3f7bf37c493a6f6d3195a4f75d9207
