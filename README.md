# HubReleases
Checks whether your github release is up to date.

## Requirements
(download via pip)<br/>
- [Requests](http://python-requests.org) ~ ``pip install requests``
- [pyYAML](https://github.com/yaml/pyyaml) ~ ``pip install PyYAML``

## Commands
```hr -h``` Get a list of commands and what they do and gives specific information when used with a command<br/>
```hr list``` List all the programs in the index.<br/>
```hr add``` Add a program to the index.<br/>
```hr del``` Remove a program from the index.<br/>
```hr get [Name]``` Gets the current version of the program in the index.<br/>
```hr check [Name]``` Checks the latest version on Github against the version in the index and opens a URL to download the new version.<br/>
```hr update [Name]``` Update the information of a program manually<br/>

## Misc
### What is "index.yaml"?
A YAML file that stores the values of the name, path, and version of the program.
