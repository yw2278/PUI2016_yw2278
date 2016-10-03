## Test Recommendations -- Citibike

#### Z test for difference of proportions*

Your question states the following:  "CitiBike users who are temporary pass holders (User Type = Customer) are more likely to use the service on weekends than users with annual memberships (User Type = Subscriber)".

Your null hypothesis states the following:

#### H0: The ratio of weekend trips to weekday trips for users of type "Customer" is the same or lower than the same ratio for users of type "Subscriber" (with confidence level .05)

It is well formulated and uses appropriate measures to address your question.  In turn, your data is pre-processed well and sets up the right information to address your H0.  And given the type of data and the question you ask of it, I propose a *Z-test of proportions* .  Your variables are proportions of counts, and proportions generally follow a gaustrian distribution which lends well to a Z-test.

A few things to note:

Unlike categories such as gender or age, the User Type category is more likely to be prone to confounding factors.  The nature of "Subscriber" and "Customer" offerings might change given how dynamic business is.  Prices may change, a offering may be fully discarded, a new type of service may be inrtroducced, etc.  I also imagine seasons and holdiays can effect results as well.  That being said, I would suggest diversifying your data over timeframes to control for these factors and/or include them directly into your analysis.

We of course did this project within a certain context of the classroom so of course my suggsetions are more acedemic.  It looks like you did a superior job.