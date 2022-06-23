### ACME - Exercise

Exercise description:
The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:


Monday - Friday
- 00:01 - 09:00 25 USD
- 09:01 - 18:00 15 USD
- 18:01 - 00:00 20 USD

Saturday and Sunday
- 00:01 - 09:00 30 USD
- 09:01 - 18:00 20 USD
- 18:01 - 00:00 25 USD


The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

- MO: Monday
- TU: Tuesday
- WE: Wednesday
- TH: Thursday
- FR: Friday
- SA: Saturday
- SU: Sunday


Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

#### Case 1:
**INPUT**: RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

**OUTPUT**: The amount to pay RENE is: 215 USD

#### Case 2:
**INPUT**: ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

**OUTPUT**: The amount to pay ASTRID is: 85 USD

--------

## Implementation

Create the **Calculator** class that is responsible for calculating the corresponding person's salary. For that I made use of another **DayWork** class that has the days worked by the person and has the responsibility of knowing how many hours per day they work and what is the price corresponding to those hours.

On the other hand, I have the **repository** module which is where I have the information stored. I decided to implement it this way as it gives me the possibility to change the storage if necessary.

Finally, I have the **utils** modules where I would store functions that I can use in various parts of my code

#### Test
The tests are implemented with pytest.

Run test locally: 
`pytest ./tests`

You have to install `pytest` and `pytest-mock`

### Run Code locally

`python main.py`

