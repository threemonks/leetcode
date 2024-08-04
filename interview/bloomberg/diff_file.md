1MB Ram computer
file A - 300TB
file B - 800TB

format
string,       char, double
ticker, field name, field value

B=bid,
T=trade,
A=ask

IBM US Equity,B,43.2
IBM US Equity,A,43.2
IBM US Equity,T,43.2
...
APPL US Equity,T,43.2
...

condition : 
ticker + field name is unique

Some File
IBM US Equity,B,43.2 // ok
IBM US Equity,B,43.21 // NOT ok
IBM US Equity,A,43.2 
IBM US Equity,T,43.2

Some File
IBM US Equity,B,43.2 
IBM US Equity,A,43.2 
//IBM US Equity,T,43.2 // ok

diff report:
File A,IBM US Equity,B,43.2
File B,IBM EU Equity,B,43.2

IBM US A ... IBM EU T
MSFT US A

FileA
A(...) I...M
A  B  CA CB I M

FileB
CA K T

n*log(n)
