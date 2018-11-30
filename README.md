# BMI500_Differential_Privacy

This code provides the histogram of original data in white color and histogram of noisy data in blue color for each epsilon, and also provides a plot of error versus values of epsilon entered.

To run the code, run the following command:

```python Differential_Privacy.py path_to_dataset epsilon_value(s)```

Where path_to_dataset is the path to the csv file. If the the csv file is in current directory, path_to_dataset=./adult_age_gender_race_dataset.csv and epsilon_value(s) can be either a single value or multiple values seperated by ','.

For instance, if the csv file is in the current directory ,for a single value of epsilon you can run the following command:

```python Differential_Privacy.py ./adult_age_gender_race_dataset.csv 0.2```

And for multiple values of epsilon run:

```python Differential_Privacy.py ./adult_age_gender_race_dataset.csv 0.1,0.2,0.4,0.6,0.8,1```

