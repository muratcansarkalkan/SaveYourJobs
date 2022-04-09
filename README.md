# SaveYourJobs
An automation script for job parsing where you don't need to click the web page to see what is available.

How it works: Run main.py and just add up the URL. Based on what the job portal is, the script will give an output of job, company and location.
In future I plan to add more scripts for more job portals and offer an Excel creation.

So far: Added LinkedIn Search, LinkedIn Specific Posting and Indeed Specific Posting parsing options.

<h3>Changelog:</h3>
<ul>
  <li>26.03.2022: LinkedIn Search now gives links</li>

<li>27.03.2022: linkedinsearchengine.py added. This script helps you search jobs in LinkedIn. For now there are only 3 parameters (Query, Location, Job Type) but more will be added.</li>

<li>29.03.2022: Added work type option</li>

<li>31.03.2022: Now jobs and links are stored as objects, instead of being printed. This is an important step while this script is converted to an UI-friendly HTML page.</li>

<li>09.04.2022: The script handles jobs better, as it prints a well-formatted JSON output, instead of printing jobs in command line.</li>
</ul>

<h3>Prerequisites:</h3>

<ul>
  <li>Latest Python version, download <a href="https://www.python.org/downloads/">here</a></li>
</ul>

<h3>Steps:</h3>

<ol>
  <li>Download this repository by clicking code, then click Download ZIP.</li>
  <li>Extract the content to anywhere you want.</li>
  <li>Install Python's latest version from the link above.</li>
  <li>After installing Python, press <kbd>Win</kbd> + <kbd>X</kbd>, then click Windows Powershell.</li>
  <li>Either you can extract job name, location, company title, or run a search and find most relevant results.</li>
</ol>

<h4>Job Parser, main.py:</h4>
<ol>
  <li>To run this script, go to the folder where you extracted the repository then open Windows Powershell, type <code>python main.py</code>.</li>
  <li>Paste your job URL (From either Indeed, or LinkedIn!).</li>
  <li>You can extract job title, company, location (only for LinkedIn) and post date.</li>
  <li>You can type <code>quit</code> to quit the parser.</li>
</ol>

<h4>LinkedIn Job Search Engine, linkedinsearchengine.py:</h4>
<ol>
  <li>To run this script, go to the folder where you extracted the repository then open Windows Powershell, type <code>python linkedinsearchengine.py</code>.</li>
  <li>Enter your searching query. If you have none, just press Enter.</li>
  <li>Enter the job type you look for. You can use Capital letters for input, if you don't have any preferred type, press N. If you don't press N, it will keep asking until max. options are reached.</li>
  <li>Enter the work type you look for. You can use numbers for input, if you don't have any preferred type, press N. If you don't press N, it will keep asking until max. options are reached.</li>
  <li>Enter your preferred location.</li>
  <li>You can type <code>quit</code> to quit the parser.</li>
  <li>The output is in this order: Job Title, Company, Location, Link.</li>
</ol>

<h3>Troubleshooting:</h3>

<ol>
  <li><b>Q: </b>I can't do the step 4. It gives an error of <code>The term "pip" is not recognized as the name of a cmdlet, function, script file, or executable program.</code>
    <br></br>
    <b>A: </b>Add Python to PATH variable. <a href="https://www.educative.io/edpresso/how-to-add-python-to-path-variable-in-windows">Here's how.</a>
  </li>
    
</ol>

<h3>Contact:</h3>

<ul>
  <li><b><a href="mailto:muratcansarkalkan@gmail.com">E-mail</a></b>
</ul>
<h3>Extra links that could be useful:</h3>

<ul>
  <li><a href="https://www.youtube.com/watch?v=Kn1HF3oD19c">Tutorial on installing Python</a></li>
</ul>
