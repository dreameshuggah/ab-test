# ab-test
An app for A/B testing.

This Streamlit [app]() can be used to run an A/B test. In non-technical terms, an A/B test is a statistical method that 
can be used to determine whether a hypothesis is true. Check [below](#hypothesis-testing-discussion) for a more detailed discussion.

You can run a demo by checking the "Use example file" checkbox:

![Alt Text](gifs/use_example.gif)

Otherwise, upload your own file and select columns that you want to analyze:

![Alt Text](gifs/upload_file.gif)

The code for this tool was based on the Strealit tutorial example repo, which can be found [here](https://github.com/streamlit/example-app-ab-testing).

## Hypothesis Testing Discussion

In the sample file we have the results of a marketing campaign from a travel website. The campaign tested two variants of the same message, A and B, with the goal of determining whether message B led to more conversions and ultimately, more revenue.

To set up the test, the following data was collected:

* The number of visitors who saw message A $$ \Delta x = x_1 - x_0 $$
* $$ x = {-b \pm \sqrt{b^2-4ac} \over 2a} $$
* The number of visitors who saw message B Nb
* The number of visitors who converted from message A Ca
* The number of visitors who converted from message B Cb

*Other data such as the length of stay and revenue was collected, but is not relevant to this discussion.*

Next, we define the Null and alternative hypotheses:
H0 - The changes did not have a meaningful impact 
Halt - The changes resulted in a meaningful impact 

After defining our hypotheses, we then pick the test statistic alpha:

hi 
low

To test our hypothesis we do the following: 

1. Calculate the conversion rate for each message, that is, the number of conversions divided by the number visitors
2. Calculate the standard error of the conversion rates. The standard error measures the amount of deviation in conversion rates across multiple trials.
It is calculated using the following equation:

Standard Error (std_err) = Square root of (cr * (1-cr) / visitors)

3. Calculate the standard error of the conversion rates. The standard error measures the amount of deviation in conversion rates across multiple trials.
It is calculated using the following equation:

Standard Error (std_err) = Square root of (cr * (1-cr) / visitors)

4. Calculate the z-score. The z-score is used to measure the distance between a data point and the mean using standard deviation. 
It is calculated using the following equation:

((crb - cra) / error) / 100
np.sqrt(sea ** 2 + seb ** 2)

5. Calculate the p-value, which is the probability that the Null hypothesis is correct given the results observed in the test. 
"One-sided" is a statistical hypothesis test set up to
show that the sample mean would be higher or lower than the
population mean, but not both.
"Two-sided" is a statistical hypothesis test in which the
critical area of a distribution is two-sided and tests whether
a sample is greater or less than a range of values.

return 1 - norm().sf(z)
elif hypothesis == "One-sided" and z >= 0:
return norm().sf(z) / 2
else:
return norm().sf(z)

If the p-value is less than the significance level alpha, we say that the results are statistically significant and reject the Null hypothesis.

