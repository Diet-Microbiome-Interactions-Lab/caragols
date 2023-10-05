# Caragols Help Page
Nomenclature: Named after the "escargot" (E-SCience ARGOT) library. Caragols is the Catalan word for a dish similar to escargot.  

## Composition:  
- carp 
	- Common App Reporting Protocol 
- clix  
	- Command Line Invocation eXtension
- condo
	- CONfiguration DOer  

### Commn App Reporting Protocol (CARP)  
**Classes:**  
**ReplyStatus(tuple)**  
This class formalizes reply statuses for the user in order to indicated a range of things from broad Failure/Success markers to exact HTTP response codes.  

**Report**  
This class provides a report version of the ReplyStatus. It can be initialized in two different ways: (i) you can provide a ReplyStatus, data, and body, or (ii) initialization via a class method that directly reports the ReplyStatus and optionally data and a body.   

