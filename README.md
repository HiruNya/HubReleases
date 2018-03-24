# HubReleases
Checks whether your github release is up to date.

## Requirements
(download via pip)<br/>
- Requests ~ ``pip install requests``
- Yaml ~ ``pip install PyYAML``

## Commands
```hr -h``` Get a list of commands and what they do.<br/>
```hr list``` List all the programs in the index.<br/>
```hr add``` Add a program to the index.<br/>
```hr del``` Remove a program from the index.<br/>
```hr get [Name]``` Gets the current version of the program in the index.<br/>
```hr check [Name]``` Checks the latest version on Github against the version in the index and opens a URL to download the new version.<br/>

## Misc
### What is "index.yaml"?
A YAML file that stores the values of the name, path, and version of the program.
