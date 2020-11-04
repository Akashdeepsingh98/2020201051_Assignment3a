# SSD3a

Github Repo - https://github.com/Akashdeepsingh98/2020201051_Assignment3a
<br>
The branch for Part B programs is named "PartB".

## Question 1
- Input file will be `org.json` as stated in assignment document.
- The json file must have the employee IDs as an integer inside string like `"002"` and `"005"` as stated in assignment document and moodle.
- Assuming the topmost employee is at `L0` in `org.json`.
- Provide the files with employee schedules in a folder named `employees`.
- Input format on terminal as stated on moodle : \<number_of_employees> \<empid 1> \<empid 2> ..... \<empid n>
- Output format as stated on Moodle:
<br>
common leader: \<emp id>
<br>
leader \<empid> is \<n> levels above employee \<empid>

- If the leader is provided in input then output `Leader not found` as stated on Moodle.

### Changes made
- There are significant changes.
- There is a separate condition for either 2,3,4 or 5 employees which, owing to time constraints, could not be made better.
- Part A had a mistake where a level was added to level count between each leader and provided employee. It has been fixed.

<br>
<br>
<br>

## Question 2
- Input file will be `date_calculator.txt` as stated in assignment document.
- Possible formats for dates:
<br>
10th September, 2020
<br>
DD/MM/YYY
<br>
DD-MM-YYYY
<br>
DD.MM.YYYY
<br>
10th Sep, 2020
<br>
MM/DD/YYYY
<br>
MM-DD-YYYY
<br>
MM.DD.YYYY

- To avoid `confusion` between formats like `MM/DD/YYYY` and `DD/MM/YYYY` please `enter the format` in console like MM/DD/YYYY (or whatever other format) for each date in file.
- In case of formats like "10th Sep, 2020" no console input is required to explain format.

- The 2 dates can have different formats.

- Input example: 
<br>
Inside date_calculator.txt
<br>
Date1: 10-9-2020
<br>
Date2: 12.09.2020
<br>
console input: 
<br>
DD-MM-YYYY
<br>
MM.DD.YYYY
<br>
The input has to be exactly like this.

- Output file is `output.txt` and format as stated in assignment document:
<br>
Date Difference: 1 Day
<br>
Date Difference: 3 Days

- The `absolute difference` between the dates is stored.

### Changes made
- 2 lines have been added - line 36 and 37 - for checking if the first character of formats similar to MM/DD/YYYY is 'M' or not.
- It is used for deciding whether the first digits are months or days.

<br>
<br>
<br>

## Question 3
- Input format is as stated in assignment document.
- User must input `slot duration` from `command line` in multiples of `0.5` as stated on Moodle (0.5, 1, 1.5 etc).
- Output file - `output.txt`.
- Output format is as stated in assignment document.
- If no slots available then write `no slot available`.
- output.txt example:
<br>
Available slots: 
<br>
{"Employee1": {"05/10/2020": ["09:00AM - 10:00AM", "11:00AM - 12:30PM", "01:00PM - 04:00PM"]}}
<br>
{"Employee2": {"05/10/2020": ["09:00AM - 10:30AM", "11:30AM - 12:00PM", "01:30PM - 03:30PM", "04:30PM - 05:00PM"]}}
<br>
{"Employee2": {"05/10/2020": ["09:00AM - 10:30AM", "11:30AM - 12:00PM", "01:30PM - 03:30PM", "04:30PM - 05:00PM"]}}
<br>
Slot duration: 0.5 hrs
<br>
{"05/10/2020": ["09:00AM - 09:30AM"]}

- If there are no slots available then the last line is replaced with `no slot available`.

### Changes made
- There are significant changes.
- The method for finding overlapping slots between 2 emloyees has been changed so that it more useful for 3,4,5 employees too.
- There is a diffrerent function for handling 2,3,4 and 5 employees each which owing to time constraints could not be made better.