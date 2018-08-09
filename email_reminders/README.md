# /email_reminders
Scripts that let users scheudle email reminders just by emailing a line of text to an email address
</br>
</br>
Usage: At the top of any email, write "Remind _recipient_ in _time_". The full email will be sent with the subject: "Reminder: _original subject_" and original body to _recipient_, _time_ units of time after the email was recieved. 
</br></br>_Recipient_ can be "me," "all," "everyone," or a specific email. _Time_ can include years, months, weeks, days, and hours. 
</br></br>
There is some flexibility, e.g. the _"in"_ keyword is not nessesarily required, and _","_ and _"and"_ can be used interchangably. However, it is best to stick to the syntax to avoid errors.
</br></br>
Examples:
>“Remind all in 2 hours”</br>
>“Remind me, spark@arborventures.com, and melissa@arborventures.com in 2 weeks”</br>
>“Remind stephanie@arborventures.com in 7 months and 2 days”</br>
>“Remind everyone and lp@bank.com in 7 month, 2 weeks, 2 days”

</br></br>
<b>Important!</b> You must run the following command once before this program can run: ```sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.atrun.plist```

<h3>Files</h3>
```-main.py```: Must be run periodically. It would be easy to set up a <a href="https://ole.michelsen.dk/blog/schedule-jobs-with-crontab-on-mac-osx.html">Cron Job</a> to do this automatically. Checks ```arborventuresdata@gmail.com``` for new messages. Checks for a remind clause, and if there is, ```reminder_functions.py``` is used to parse the reminder. The message is then saved in ```messages.xml```. An ```at``` job is scheduled to run ```remind.py``` at a specific time.</br></br>
```-reminder_functions.py```: Parses reminder clause and determines who to send the reminder to, and when to send it.</br></br>
```-remind.py```: Runs automatically by ```at``` daemon. Sends a specific message stored in ```messages.xml``` to the recipients.</br></br>
```messages.xml```: Stores message information. A unique id is assigned to each message so ```at``` jobs can be scheduled to send specific messages at specific times. Each message contains ```<to>```, ```<subject>```, and ```<body>```. 


