Feature: sorting by ABS without lambda
Scenario: sorting by ABS without lambda
Given data
When sorting data: my_sort_without_lambda
Then data was sorted