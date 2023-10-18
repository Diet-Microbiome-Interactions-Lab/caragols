# Caragols Help Page

Nomenclature: Named after the "escargot" (E-SCience ARGOT) library. Caragols is the Catalan word for a dish similar to escargot.

## Purpose

The basic idea is to rely on JSON or YAML documents for default and/or complex configuration. The command arguments are interpreted as a sequence of edit commands to the configuration object. The edit commmands are the same syntax and semantics as defined in the app.condo.Condex.sed method.

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

**DEFAULT_CATEGORY_GLOSS**: Ranges from 1 (FYI) - 5 (Fault).  
**DEFAULT_CODE_GLOSS**: Ranges from 100 (FYI) - 50\* (Fault) and is more specific than DEFAULT_CATEGORY_GLOSS.

**Report**  
This class provides a report version of the ReplyStatus. It can be initialized in two different ways: (i) you can provide a ReplyStatus, data, and body, or (ii) initialization via a class method that directly reports the ReplyStatus and optionally data and a body.

### Usage

By default, this looks for configuration files in the following locations:

1. /etc/_app_name_/conf\_\*.yml
2. /Users/_username_/.config/_app_name_/conf\_\*.yml

Once it finds those, it then updates/overrides the default configuration values.
In order to access these configuration variables, you can use the following syntax:

```python
$ print(myapp.conf.get('lab'))
>>> lindeman
$ print(myapp.conf.get('log'))
>>> caragols.lib.condo.CxNode object
$ print(myapp.conf.get('log.level'))
>>> 30
```
