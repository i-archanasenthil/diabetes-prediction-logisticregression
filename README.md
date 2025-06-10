## Logistic Regression

**Logistic regression** is a supervised machine learning algorithm used for binary classification problems. Unlike linear regression, it predicts the **probability** that a given input belongs to a particular category, using the **logistic (sigmoid) function** to map any real-valued number into the range between 0 and 1.

This probability is then compared to a **decision threshold** (default is 0.5) to assign a final class label (0 or 1).

### Assumption Testing

Before fitting the logistic regression model, several assumptions were evaluated:

- **No multicollinearity**: Checked using a correlation matrix and Variance Inflation Factor (VIF).

- **Linearity of independent variables with log odds**: Assessed using box plots and logit plots.

- **No extreme outliers**: Handled using interquartile range filtering.

- **Large sample size**: The dataset has enough records to ensure statistical power.

Though logistic regression is more robust to some assumptions compared to linear regression, these checks ensure reliability and interpretability of the results.

### Threshold Tuning

Logistic regression outputs probabilities, and the default decision threshold is 0.5. However, depending on the application, this threshold can be **adjusted to control the trade-off between precision and recall.**

In this project:

Lowering the threshold improves **recall** (fewer false negatives), which is essential in medical diagnosis where missing a positive case is costly.

Raising the threshold improves **precision** (fewer false positives), useful when treatment or intervention cost is high.

The **precision-recall curve** was plotted, and an **F1 score** was calculated to identify the optimal threshold that balances both metrics.
