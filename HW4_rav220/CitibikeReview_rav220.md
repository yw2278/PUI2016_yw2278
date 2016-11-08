## Recommendations for Ian Stuart - Citibike Analysis

#### Z test for difference of proportions*

Study Question:  CitiBike users who are temporary pass holders (User Type = Customer) are more likely to use the service on weekends than users with annual memberships (User Type = Subscriber).

#### H0: The ratio of weekend trips to weekday trips for users of type "Customer" is the same or lower than the same ratio for users of type "Subscriber" (with confidence level .05)

H0 is well formulated and uses appropriate measures to address the question.  The data has been appropriately pre-processed and prepared to address it.

A *Z-Test of proportions* is recommended given the categorical nature of the data and the question asked.  The variables are proportions of counts which generally follow a gausian distribution and lends well to this type of test.

To note:

Unlike gender and age, confounding variables are more likely play a role when using the "User Type" category.  The nature of "Subscriber" and "Customer" data is less "stable".  The terms of these offerings can change, an eniterly new type may be introduced, one may be cancelled, etc.  There might also be seasonality and holidays to account for.  Suggestion would be to diversify the dataset and/or account for these effects directly in the model.

Overall, a thought out and very well prepared analysis.