# HubReleases
Checks whether your github release is up to date.

## Requirements
(download via pip)<br/>
- Requests ~ ``pip install requests``
- Yaml ~ ``pip install PyYAML``

## Commands
```hb -h``` Get a list of commands and what they do.<br/>
```hb list``` List all the programs in the index.<br/>
```hb add``` Add a program to the index.<br/>
```hb del``` Remove a program from the index.<br/>
```hb get [Name]``` Gets the current version of the program in the index.<br/>
```hb check [Name]``` Checks the latest version on Github against the version in the index and opens a URL to download the new version.<br/>

## Misc
### What is "index.yaml"?
A YAML file that stores the values of the name, path, and version of the program.
