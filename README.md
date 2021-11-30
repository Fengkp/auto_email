<h1>Automatic Email Sender</h1>
<p>Takes in a .csv file filled with contacts gathered from CDC jobs and then sends emails each contact based on a set of criteria.</p>
<h3>Features</h3>
    <li>Sends an email based on a template to contacts that have never received an email.</li>
    <li>Sends an email based on a template to contacts that haven't received an email within a period of time.</li>
    <li>After sending an email, updates the status and timestamp for the contact.</li>
    <p><br>The goal is to send emails periodically to companies gathered from the Construct Connect website in the hopes of acquiring more customers.<br> 
    Construct Connect provides a .csv file describing a particular job and the companies associated with that job.<br>
    A separate application I've made takes those .csv files and parses out any companies that have bid on that particular project. Those bidding companies are added to a .csv file that keeps track of all the contact information.<br>
    This application uses that contact sheet to send out emails accordingly
<h3>Log</h3>
    <li><i><b>11/30/2021: </b>Emails are sent if status is unsent</i></li>
    <li><i><b>11/30/2021: </b>Wait 20 seconds before sending another email as to not exceed domain limit</i></li>
