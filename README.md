# ab-test
An app for A/B testing.

This Streamlit [app](https://el-grudge-ab-test-app-l2gvyr.streamlit.app/) can be used to run an A/B test. In non-technical terms, an A/B test is a statistical method that can be used to determine whether a hypothesis is true, for example, whether a website's new layout would generate more traffic. Check [below](#hypothesis-testing-discussion) for a more detailed discussion.

You can run a demo by checking the "Use example file" checkbox:

![Alt Text](images/use_example.gif)

Otherwise, upload your own file and select columns that you want to analyze:

![Alt Text](images/upload_file.gif)

The code for this tool was based on the Streamlit example repo, which can be found [here](https://github.com/streamlit/example-app-ab-testing).

## Hypothesis Testing Discussion

In the sample file we have the results of a marketing campaign from a travel website. The campaign tested two variants of the same message, A and B, with the goal of determining whether message B led to more conversions and ultimately, more revenue.

To set up the test, the following data was collected:

* The number of visitors who saw message A $N_a$
* The number of visitors who saw message B $N_b$
* The number of visitors who converted from message A $Cv_a$
* The number of visitors who converted from message B $Cv_b$

*Other data such as the length of stay and revenue was collected, but is not relevant to this discussion.*

Next, we define the null and alternative hypotheses:
* **$H_0$**: The changes did not have a meaningful impact 
* **$H_A$**: The changes resulted in a meaningful impact 

After defining our hypotheses, we then pick the significance threshold $\alpha$. It is common to pick $0.05$ as the significance threshold, however, it is worth noting that increasing $\alpha$ will increase the chance of false positive results, while decreasing it has the converse effect. Choosing the right value is determined by the level of tolerance towards false positives and industry standards. In our case, we will stick with $0.05$.

Now, to test our hypothesis we do the following: 

1. Calculate the conversion rate for each message, that is, the number of conversions divided by the number visitors  

<p align=center>$CR_a = \frac{Cv_a}{N_a}$ & $CR_b = \frac{Cv_a}{N_a}$</p>

2. Calculate the standard error of the conversion rates. The standard error measures the amount of deviation in conversion rates across multiple trials. It is calculated using the following equation:

<p align=center>$SE = \sqrt{(\frac{Cv_a+Cv_b}{N_a+N_b})\times(1 - \frac{Cv_a+Cv_b}{N_a+N_b})\times(\frac{1}{N_a}+\frac{1}{N_b})}$</p>

3. Calculate the z-score. The z-score is used to measure the distance between a data point and the mean using standard deviation. In our case, it is actually the distance between the conversion rate of the new message and that of the original message. It is calculated using the following equation:

<p align=center>$Z = \frac{CR_b - CR_a}{SE}$</p>

4. Calculate the p-value, which is the probability that $H_0$ is correct given the results observed in the test. Consider the below curve:

<p align="center">
  <img src="images/area_under_curve.png" alt="drawing" width="200"/>
</p>

If the p-value is between the shaded areas, then we accept $H_0$. In other words, the difference between the conversion rate of message B and the conversion rate of message A is not large enough for us to determine that it was not random. Conversely, if the p-value falls in either shaded area, then we reject $H_0$, and conclude that the difference is statistically significant. In a one-sided test, we can find out whether the direction of the difference, i.e. whether $CR_b$ is signifianctly less than (left shaded area) or greater than $CR_a$ (right shaded area). On the other hand, a two-sided tests tells whether the difference is large enough (falls under either region), regardless of direction (however, with a positive uplift we can conclude that message B was better). The p-value is determined via lookup tables using the value of the z-score calculated in the previous step, or it can be calculated using code functions such as `pnorm()` in R or `scipy.stats.norm` in Python.

The point at which the shaded area starts is determined by $\alpha$. So, if the p-value is less than the significance level $\alpha$, we say that the results are statistically significant and reject $H_0$.

In this example, p-value was less than $\alpha$, which means that we can safely reject the null hypothesis and determine that the changes in message B could in fact be attributed to an increase in conversion rate.
