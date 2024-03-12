# GDirectly runable at https://replit.com/@travis85002
GiveDirectly Take Home Exercise

Context:
GiveDirectly often does research studies where we want to assess the impact of different payment
configurations (e.g. $100 in 2 payments of $50 vs. 10 payments of $10). To conduct that research, we
might decide up front how many different payment configurations we want to randomize among when
we enter a village and the weight of each payment configuration.
For example, let’s pretend that payment config A represents paying the money over 10 payments, B
represents 5 payments and C represents 1 payment.
We might want a 33.3%-33.3%-33.4% split across A-B-C or we might want a 20%-30%-50% split. The first
means that a third of recipients in a given village get A, a third get B, and a third get C. The second means
that 20% get A, 30% get B and 50% get C.

The assignment:
Writing a Function
Your job will be to write the function, "assign_recipients", that takes as parameters:
1. Map of payment config -> weight that represents the target distribution, where the weight
values sum to 1.0.
2. List of recipients names
And then returns an updated map of recipient -> payment config where every recipient has a payment
config.
For example, see the two parameters below:
# python
target_distribution = {"A" : 0.3,"B" : 0.2, "C" : 0.5}
inputs = [ "Diogo", "Piali", "Solomon", "Gisele", "Jeff", "Falida", "Ade", "Maya", "Meylakh", "Nana"]
And assign_recipients might return something like:
# python
outputs = { "Diogo" : "C", "Piali" : "C", "Falida" : "C", "Gisele" : "C" , "Nana" : "C" , "Solomon" : "B",
"Jeff" : "B", "Ade" : "A", "Meylakh" : "A", "Maya" : "A"}
Please provide brief notes on any major design decisions you made (data structures, algorithms, etc.)
and why you made them.
Testing Your Code
Please provide a list of what test cases you would want to cover for your code. You do not need to
write the tests themselves.
Additional Considerations
You may think of questions or circumstances that we haven’t addressed above. If you do, please
include a list that you’re wondering about and/or incorporate into your code and be explicit about the
assumptions you’re making.
Remaining Work
Lastly, if you had more time, what are other issues or scenarios you'd want to spend more time
ensuring your code can address?
A few general notes:
● Please spend a maximum of 2 hours on the above exercise.
● You can use whatever programming language you feel comfortable with, despite the example
above being Python.
● We’d like your code to compile. Repl.it is an integrated development environment that can run
from your browser and is free to use. If you’re using a language other than Python, R, or Apex;
please include notes on how to run it.
● It is acceptable to google around for syntax but unacceptable to google around for solutions or
solution frameworks.
● Please reply to the email you received with attachments that include your assignment work.
